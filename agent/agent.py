import csv
import re
from collections import defaultdict

class ReflectionAgent:
    def __init__(self, tree_file):
        self.nodes = {}
        self.children = defaultdict(list)
        self.state = {
            "answers": {},
            "axis1": defaultdict(int),
            "axis2": defaultdict(int),
            "axis3": defaultdict(int),
        }
        self.load_tree(tree_file)

    def load_tree(self, file_path):
        with open(file_path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                self.nodes[row["id"]] = row
                parent = row["parentId"]
                if parent and parent != "null":
                    self.children[parent].append(row["id"])

    def interpolate(self, text):
        # Replace {node.answer}
        for key, val in self.state["answers"].items():
            text = text.replace(f"{{{key}.answer}}", val)

        # Replace axis summaries
        for axis in ["axis1", "axis2", "axis3"]:
            if self.state[axis]:
                dominant = max(self.state[axis], key=self.state[axis].get)
                text = text.replace(f"{{{axis}.dominant}}", dominant)
        return text

    def apply_signal(self, signal):
        if not signal:
            return
        parts = signal.split(":")
        if len(parts) == 2:
            axis, value = parts
            if axis in self.state:
                self.state[axis][value] += 1

    def run(self):
        current = "START"

        while True:
            node = self.nodes[current]
            node_type = node["type"]
            text = self.interpolate(node["text"])
            signal = node["signal"]

            if signal:
                self.apply_signal(signal)

            if node_type == "start":
                print("\n" + text)
                current = self.get_next(current)

            elif node_type == "question":
                print("\n" + text)
                options = node["options"].split("|")

                for i, opt in enumerate(options, 1):
                    print(f"{i}. {opt}")

                choice = self.get_choice(len(options))
                answer = options[choice - 1]
                self.state["answers"][current] = answer

                current = self.get_next(current)

            elif node_type == "decision":
                current = self.evaluate_decision(node)

            elif node_type == "reflection":
                print("\n" + text)
                input("\nPress Enter to continue...")
                current = self.get_next(current)

            elif node_type == "bridge":
                print("\n" + text)
                current = node["target"]

            elif node_type == "summary":
                print("\n--- Reflection Summary ---")
                print(self.interpolate(node["text"]))
                current = self.get_next(current)

            elif node_type == "end":
                print("\n" + text)
                break

    def get_next(self, current):
        children = self.children.get(current, [])
        return children[0] if children else None

    def evaluate_decision(self, node):
        rules = node["options"].split(";")

        for rule in rules:
            match = re.match(r"answer=(.+?):(.+)", rule)
            if match:
                answers, target = match.groups()
                answers = answers.split("|")

                # get parent answer
                parent_id = node["parentId"]
                parent_answer = self.state["answers"].get(parent_id)

                if parent_answer in answers:
                    return target

        raise Exception(f"No decision rule matched for node {node['id']}")

    def get_choice(self, max_val):
        while True:
            try:
                choice = int(input("Select option: "))
                if 1 <= choice <= max_val:
                    return choice
            except:
                pass
            print("Invalid input. Try again.")


if __name__ == "__main__":
    agent = ReflectionAgent("../tree/reflection-tree.tsv")
    agent.run()