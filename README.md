# DFA_example
# Forest Fire Simulation Modeled as a Cellular Automaton with DFA-like State Transitions

This wildfire simulation models forest dynamics using cellular automata, where each cell transitions between states akin to a Deterministic Finite Automaton (DFA). The rules governing state transitions are as follows:

---

## State Definitions for Cells
1. **Empty Cell**: No tree (`tree = None`).
2. **Tree States**:
   - **Growing**: Tree is alive and not on fire (`on_fire = False`, `is_dead = False`).
   - **Ready to Ignite**: Tree will catch fire in the next frame (`going_fire = True`).
   - **On Fire**: Tree is actively burning (`on_fire = True`).
   - **Burned Out**: Tree is dead and removed (`is_dead = True`).

---

## State Transition Rules
### ① Lightning Strike (Global Event)
- With a probability of `thunder_rate`, lightning strikes a random cell.
- If the struck cell contains a living tree, it ignites (`on_fire = True`).

---

### ② Per-Cell Updates (Applied Every Frame)
For each cell in the grid:
1. **Empty Cell**:
   - A new tree grows with probability `tree_born_rate` (via `tree_born()`).

2. **Cell with Tree**:
   - **If neighbors are not on fire**:
     - Update tree state via `tree_life()`:
       - If burning (`on_fire = True`), reduce `weight` by `fire_rate`. When `weight ≤ 0`, mark as `is_dead`.
       - If growing, increase `weight` by `growth_rate` (capped at `max_weight`).
   - **If any adjacent neighbor is on fire**:
     - Mark the tree as `going_fire = True` (to ignite in the next frame).

---

### ③ State Propagation
- After all cells are processed, `going_fire` is resolved:
  - Trees marked `going_fire` transition to `on_fire = True`.
  - Dead trees (`is_dead = True`) are removed (`tree = None`).

---

## DFA/NFA Analogy
- **States**: Empty, Growing, Ready to Ignite, On Fire, Burned Out.
- **Transitions**: Triggered by neighbor states (fire spread) or stochastic events (lightning/tree growth).
- **Determinism**: Transitions follow explicit rules, resembling a DFA, but stochastic elements (e.g., lightning) introduce non-determinism akin to an NFA.

---
![gif](/output.gif)

This model demonstrates how simple local rules and state transitions can simulate complex emergent behavior, mirroring finite automaton principles.
