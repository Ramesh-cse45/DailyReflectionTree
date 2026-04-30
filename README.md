# Daily Reflection Tree (Deterministic Agent)

## Overview
This project implements a deterministic reflection system based on three axes:
1. Agency (Victim vs Victor)
2. Contribution (Entitlement vs Contribution)
3. Perspective (Self vs Others)

## How to Use
- Load `reflection-tree.tsv`
- Traverse nodes sequentially
- At each `question`, select an option
- Follow decision rules
- Display reflections and summary

## Key Properties
- No LLM at runtime
- Fully deterministic
- Fixed options only
- State-driven branching

## Files
- /tree/reflection-tree.tsv → Core logic
- /tree/tree-diagram.md → Visual structure
- write-up.md → Design explanation

## Optional Extension
You can build a CLI agent to execute the tree.