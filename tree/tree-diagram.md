graph TD
START --> A1_OPEN
A1_OPEN --> A1_D1
A1_D1 -->|High| A1_Q1_HIGH
A1_D1 -->|Low| A1_Q1_LOW
A1_Q1_HIGH --> A1_Q2 --> A1_R_INT
A1_Q1_LOW --> A1_Q2B --> A1_R_EXT
A1_R_INT --> BRIDGE_1_2 --> A2_OPEN
A1_R_EXT --> BRIDGE_1_2B --> A2_OPEN

A2_OPEN --> A2_D1
A2_D1 -->|Contribution| A2_Q1_HIGH
A2_D1 -->|Entitlement| A2_Q1_LOW
A2_Q1_HIGH --> A2_Q2 --> A2_R_CON
A2_Q1_LOW --> A2_Q2B --> A2_R_ENT
A2_R_CON --> BRIDGE_2_3 --> A3_OPEN
A2_R_ENT --> BRIDGE_2_3B --> A3_OPEN

A3_OPEN --> A3_D1
A3_D1 -->|Self| A3_Q1_SELF
A3_D1 -->|Other| A3_Q1_ALT
A3_Q1_SELF --> A3_Q2 --> A3_R_SELF --> SUMMARY --> END
A3_Q1_ALT --> A3_Q2B --> A3_R_ALT --> SUMMARY2 --> END2