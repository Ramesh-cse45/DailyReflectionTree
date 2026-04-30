# Design Rationale

This reflection tree is designed to guide users through three progressive psychological shifts:

---

## 1. Agency (Axis 1)

The first axis focuses on **locus of control**, helping users reflect on whether they operated from an internal (agency-driven) or external (circumstance-driven) mindset.

- Questions distinguish between internal vs external locus using real behavioral cues (e.g., reactions to success or failure).
- Branching ensures:
  - High-agency users reinforce ownership and intentionality
  - Low-agency users are gently nudged to notice where they still had choice

---

## 2. Contribution (Axis 2)

The second axis shifts focus from control to **value creation**.

- Questions surface:
  - **Contribution mindset** (helping others, taking initiative)
  - **Entitlement mindset** (focus on recognition, fairness, or unmet expectations)

**Design choice:**  
Avoid moral judgment. Instead, entitlement is framed as a natural but improvable tendency, encouraging reflection rather than defensiveness.

---

## 3. Radius (Axis 3)

The third axis expands perspective from self to others.

- Uses progressive framing:
  - Self → Team → Individual → Customer
- Encourages users to move beyond self-centered thinking

This aligns with **self-transcendence theory**, where meaning increases as attention shifts outward.

---

# Key Design Decisions

## 1. Deterministic Branching

- All decisions use explicit answer mapping
- No ambiguity or probabilistic scoring
- Same inputs always produce the same outputs

---

## 2. Fixed Options Only

Each option is designed to be:
- Mutually exclusive
- Psychologically meaningful
- Realistic for users at the end of a workday

---

## 3. Reflection Tone

- Non-judgmental
- Observational rather than prescriptive
- Designed to feel like a **“wise colleague”**, not a manager or therapist

---

## 4. Progressive Flow

Each axis builds naturally on the previous:

- Agency → enables Contribution  
- Contribution → enables Perspective expansion  

This ensures the experience feels like a single coherent conversation, not separate assessments.

---

# Sources Used

- **Julian Rotter** — Locus of Control  
- **Carol Dweck** — Growth Mindset  
- **Dennis Organ** — Organizational Citizenship Behavior  
- **Abraham Maslow (1969)** — Self-Transcendence  
- **C. Daniel Batson** — Perspective Taking  

---

# Trade-offs

- Prioritized **clarity over complexity** (avoided deep nested branching)
- Limited number of nodes per axis to maintain usability
- Avoided over-personalization to preserve determinism and consistency

---

# Improvements (If More Time)

- Add deeper sub-branches for handling mixed or ambiguous signals
- Introduce pattern-based summaries across multiple days
- Support adaptive session length (short vs extended reflection paths)
- Enhance summary personalization using richer state variables

---
