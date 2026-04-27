# The Daily Reflection Tree

A deterministic, psychology-grounded reflection tool that walks employees through structured self-inquiry across three axes: **Locus of Control**, **Contribution Orientation**, and **Radius of Concern**.

---

## Files in This Submission

- **`reflection-tree.json`** — The complete tree structure (140+ nodes, fully traversable)
- **`reflection_agent.py`** — Python agent that loads and executes the tree
- **`WRITE_UP.md`** — Design rationale, psychological grounding, trade-offs
- **`TRANSCRIPTS.md`** — Two sample walkthroughs (victim vs. victor mindset paths)
- **`README.md`** — This file

---

## Quick Start

### Prerequisites
- Python 3.7+
- No external dependencies (uses only `json` and `os` from stdlib)

### Running the Agent

```bash
python3 reflection_agent.py
```

The agent will:
1. Load `reflection-tree.json`
2. Walk you through 6 core scenarios with follow-up questions
3. Track your answers and accumulate signals across the three axes
4. Display a reflection summary at the end
5. Show your axis scores

**Expected time:** 10-15 minutes

---

## Understanding the Tree

### Tree Structure

The tree is stored as **JSON** with nodes of the following types:

| Type | Purpose | Has User Input? |
|------|---------|-----------------|
| `start` | Opens session | No |
| `question` | Asks scenario with 3-4 fixed options | Yes |
| `decision` | Routes based on answer (invisible to user) | No |
| `reflection` | Reframes or insight based on path | No |
| `bridge` | Transitions between axes | No |
| `summary` | End-of-session synthesis | No |
| `end` | Closes session | No |

### How It Works

Each node has:
- **`id`** — Unique identifier
- **`parentId`** — Which node leads here
- **`type`** — Node type (above)
- **`text`** — What the user sees
- **`options`** — For questions: fixed choices. For decisions: routing rules like `answer=A:NODE1;answer=B:NODE2`
- **`signal`** — Axis signal recorded at this node (e.g., `axis1:internal`)
- **`target`** — Next node (for non-question nodes)

### Example: A Single Branch

Question: *"You saw something inspiring. What went through your head?"*

Options:
- A) Think about what I'd need
- B) Feel fired up, start now
- C) Think 'someday'

**If you pick A:**
- Router sends you to `Q1a_RESOURCES`
- Which asks: *"What could you start without?"*
- Your answer there branches to one of three reflections
- Each reflection records a signal (`axis1:internal` or `axis1:external`)

**If you pick C:**
- Router sends you to `Q1c_SOMEDAY`
- Which asks: *"Will someday actually come?"*
- Answers branch to reflections that all record `axis1:external`

---

## The Three Axes Explained

### Axis 1: Locus of Control

**Internal:** "My choices shape outcomes. I see my agency."
**External:** "Circumstances or others determine what happens."

Measured by questions about:
- Starting projects despite imperfect conditions
- Owning your reactions vs. blaming external factors
- Seeing growth as buildable vs. fixed

### Axis 2: Contribution vs. Entitlement

**Contribution:** "What did I give or help with today?"
**Entitlement:** "What did I get / deserve / was I overlooked for?"

Measured by questions about:
- Communicating needs vs. expecting others to read your mind
- Fairness to strangers vs. favoring friends
- Taking responsibility for your stress vs. expecting others to manage it

### Axis 3: Self-Centric vs. Other-Centric

**Self-Centric:** "How does this affect me?"
**Other-Centric:** "How does this affect us? The system? Others I don't see?"

Measured by questions about:
- Creating for yourself vs. for an audience
- Choosing time alone vs. choosing connection
- Comparing yourself with envy vs. admiration
- Making choices for friends vs. thinking about fairness

---

## Sample Runs

See **`TRANSCRIPTS.md`** for two complete walkthroughs:

1. **Persona 1 (Victim/Self-Centric):** External locus, entitlement-leaning, self-focused. Scores high on external/entitlement/self signals.

2. **Persona 2 (Victor/Other-Centric):** Internal locus, contribution-minded, other-focused. Scores high on internal/contribution/other signals.

Same tree, different paths, different reflections. Both end with synthesis but with different resonance.

---

## How the Agent Works (For Developers)

### Loading the Tree
```python
agent = ReflectionAgent('reflection-tree.json')
agent.walk_tree()
```

### State Accumulation
```python
state = {
    'answers': {},    # {node_id: answer_letter}
    'path': [],       # [node_id, node_id, ...]
    'axis1': {'internal': 0, 'external': 0},
    'axis2': {'contribution': 0, 'entitlement': 0},
    'axis3': {'self': 0, 'other': 0}
}
```

### Routing Logic
Questions route to decision nodes. Decision nodes parse rules:
```
"answer=A:Q1a_RESOURCES;answer=B:Q1b_IMPATIENT;answer=C:Q1c_SOMEDAY"
```
If you pick option A, you go to `Q1a_RESOURCES`. If B, to `Q1b_IMPATIENT`. Etc.

### Signals
When you land on a reflection node with `signal: "axis1:internal"`, the state tally increments:
```python
state['axis1']['internal'] += 1
```

By the end, you have counts across all six poles. The summary interprets these.

---

## Extending the Tree

To add new scenarios:

1. **Create question node:**
   ```json
   {
     "id": "Q7_YOUR_SCENARIO",
     "parentId": "PREVIOUS_NODE",
     "type": "question",
     "text": "Your question here?",
     "options": ["A) Option 1", "B) Option 2", "C) Option 3"],
     "target": null,
     "signal": null
   }
   ```

2. **Create decision node** (same id + `_DECISION`):
   ```json
   {
     "id": "Q7_YOUR_SCENARIO_DECISION",
     "parentId": "Q7_YOUR_SCENARIO",
     "type": "decision",
     "text": "",
     "options": "answer=A:Q7a_PATH;answer=B:Q7b_PATH;answer=C:Q7c_PATH",
     "target": null,
     "signal": null
   }
   ```

3. **Create follow-up and reflection nodes** for each branch.

4. **Update bridge or parent nodes** to route to `Q7_YOUR_SCENARIO`.

The agent will automatically pick up new nodes from the JSON.

---

## Design Philosophy

This tree embodies a specific philosophy:

1. **Deterministic, not generative.** No LLM at runtime. Every answer follows a known path.

2. **Structured, not free-form.** Users choose from fixed options, which forces designers to capture real distinctions.

3. **Reflecting, not coaching.** The tool asks questions and reframes; it doesn't prescribe actions.

4. **Non-judgmental.** Both "victim" and "victor" paths are met with understanding, not shame.

5. **Psychologically grounded.** Based on Rotter, Dweck, Organ, Campbell, Maslow — not self-help folklore.

---

## Limitations and Future Work

### Current Limitations

- **6 core scenarios** — covers major life domains but not comprehensive
- **No personalization** — same tree for all users
- **No data persistence** — sessions aren't saved for pattern tracking
- **No adaptive branching** — doesn't adjust difficulty based on user insight

### Future Enhancements

- Add 4-6 more scenarios (health, finances, learning, spirituality)
- Implement week-over-week pattern tracking
- Create role-specific variants (engineer, manager, designer)
- Add team/org version with anonymized collective patterns
- Build mobile-first interface with offline support
- Integrate with journaling or calendar systems

---

## Testing

The tree has been walked through two complete personas to verify:
- ✓ All nodes are reachable
- ✓ Routing works correctly
- ✓ Signals accumulate properly
- ✓ Reflections are coherent and non-judgmental
- ✓ Summary synthesizes without repeating

See `TRANSCRIPTS.md` for full test walkthroughs.

---

## FAQ

**Q: Why no free text input?**
A: Fixed options force better question design. If users can say anything, designers get lazy with options.

**Q: Why deterministic instead of LLM-based?**
A: Determinism = trust. Users know they'll get the same reflection every time, which is auditable and predictable.

**Q: Is this therapy?**
A: No. It's structured self-inquiry. Therapy requires a licensed human. This is a thinking tool.

**Q: How long does a session take?**
A: 10-15 minutes at normal pace. Faster if you know yourself well, slower if you're genuinely uncertain.

**Q: Can I cheat by always picking the "good" answer?**
A: You can, but you'd be cheating yourself. The power of reflection comes from honesty.

---

## Contact & Feedback

This tree was designed as part of a DeepThought Fellowship assignment. It represents one person's attempt to encode psychological insight into navigable structure.

If you find it useful, or if you see gaps, consider:
- Adding more scenarios
- Testing with real users
- Refining reflections based on feedback
- Creating variants for specific contexts

The code is clean and the JSON is readable — extend it.