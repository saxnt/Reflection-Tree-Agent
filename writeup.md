# Design Rationale: The Daily Reflection Tree

## Overview

The Daily Reflection Tree is a deterministic, decision-tree-based reflection tool designed to help employees process their day through three psychological axes: **Locus of Control**, **Contribution vs. Entitlement**, and **Self-Centric vs. Other-Centric Orientation**.

The tool asks 6 core scenarios covering different domains of daily experience (creative ambition, interpersonal conflict, friendship, family dynamics, talent/growth, and fairness/ethics). Each scenario branches into follow-up questions based on the employee's initial response, accumulating psychological signals across the three axes.

**Goal:** By evening's reflection, the employee sees a pattern — not as judgment, but as data about how they showed up today.

---

## The Three Axes: Psychological Grounding

### Axis 1: Locus of Control (Rotter, 1954)

**The Theory:**
Julian Rotter's locus of control measures the degree to which people believe their outcomes are determined by their own actions (internal) versus external factors (luck, others, circumstances).

- **Internal:** "My choices shaped what happened. I see where I had agency."
- **External:** "Things happened to me. Circumstances or others determined the outcome."

**Why It Matters:**
People with internal locus tend to learn faster, adapt better, and feel more ownership. People who slip into external locus often feel helpless and attribute failure to unchangeable factors.

**How the Tree Surfaces It:**
- Q1 (Filmmaking): "Did you see starting as possible, or did you wait for conditions?"
- Q2 (Snapping at mom): "Did you recognize your choice to react, or blame their words / your stress?"
- Q5 (Reel comparison): "Do you see talent as built (internal agency) or fixed (external trait)?"
- Q6 (Internship favor): "Did you make a deliberate choice about fairness, or defer to 'that's how it works'?"

**Design Choice:**
The questions never ask "Do you have agency?" (too direct, too easy to lie). Instead, they ask about real moments where agency was ambiguous — did you start a project, did you own your reaction, did you take action? The answer reveals whether the person is waking up to agency or sleeping in passivity.

---

### Axis 2: Contribution vs. Entitlement (Organ, 1988; Campbell et al., 2004)

**The Theory:**
Organizational Citizenship Behavior (OCB) measures discretionary effort — helping beyond job requirements, improving processes, mentoring.

Psychological Entitlement (inverse of OCB) is the belief that one deserves more than others, independent of contribution.

- **Contribution:** "What extra did I do today? Who did I help? What went beyond duty?"
- **Entitlement:** "Did I get what I deserve? Did others pull their weight? Did I get credit for my work?"

**Why It Matters:**
Entitled employees often feel resentful even when compensated fairly. They focus on the gap between what they received and what they believe they're owed. Contribution-minded employees feel grateful for what they gave, even when undercompensated.

**How the Tree Surfaces It:**
- Q2 (Snapping at mom): "Did you expect her to understand without you communicating? Did you blame her for not managing your stress?"
- Q3 (Walk with friend): "Did you sacrifice your decompression for connection, or balance both? And do you even notice when you do?"
- Q4 (Mom ranting + ego work): "Were you trying to prove your worth to her, or owning your value independently?"
- Q6 (Internship favor): "Are you helping your friend because it's right, or because the system is 'flexible anyway'?"

**Design Choice:**
Entitlement is invisible to the person holding it. So the tree doesn't ask "Are you entitled?" It asks about moments where the person might be shifting blame, expecting grace without communication, or playing a game they know is unfair. The realization comes from their own answers, not from being told.

---

### Axis 3: Self-Centric vs. Other-Centric Orientation (Maslow, 1969)

**The Theory:**
Maslow's hierarchy has five levels. Most stop at self-actualization ("being your best self"). But Maslow's 1969 work added **self-transcendence** — the shift from "What do I need?" to "What does the world need from me?"

Other-centric doesn't mean self-denial. It means the frame of reference widens. Instead of "How does this affect me?" you ask "How does this affect us? The team? The system?"

**Why It Matters:**
Self-focused people often feel more pain (they notice every slight) and less meaning (everything is relative to them). Other-focused people contextualize struggles within something larger, which paradoxically reduces suffering and increases meaning.

**How the Tree Surfaces It:**
- Q1 (Filmmaking): "Are you thinking about your creative spark, or about creating something others will see?"
- Q3 (Walk with friend): "Did you isolate for self-care, or connect for their sake? Can you do both?"
- Q4 (Mom ranting): "Are you trying to prove your worth to her, or living for your own standards?"
- Q5 (Reel comparison): "Are you envious of what they have, or inspired by what they're building? Do you want to learn from them?"
- Q6 (Internship favor): "Are you thinking about your friend's need, or about fairness to people you'll never meet?"

**Design Choice:**
The tree doesn't villainize self-focus — it's necessary. But it asks: *Who's in your frame?* Just you? You and the people close to you? The whole system? Each level is valid at different times, but the healthiest people expand their radius as needed.

---

## Scenario Selection: Why These Six?

Each scenario was chosen to isolate a specific axis while remaining emotionally real and relatable.

| Scenario | Primary Axis | Secondary | Why This One |
|----------|-------------|-----------|------------|
| Filmmaking reel | Axis 1 (Locus) | Axis 3 | Creative inspiration often reveals whether we see ourselves as creators or consumers. Do we defer to external barriers, or do we see agency? |
| Snapping at mom | Axis 1 + Axis 2 | - | Family conflict under stress is where people often abdicate responsibility ("I was stressed, they should understand") or take it ("I didn't manage my reaction"). |
| Walk with friend | Axis 3 (Radius) | Axis 1 | Self-care vs. connection reveals whether someone is widening their concern. Can they do both? Do they notice the choice? |
| Mom ranting + ego work | Axis 2 (Contribution) | Axis 3 | Responding to criticism by proving yourself (vs. owning your value independently) reveals whether you're contributing to your own growth or performing for others' approval. |
| Reel comparison | Axis 1 + Axis 3 | - | Comparing yourself to others reveals both growth mindset (internal locus: "I can learn") and whether you admire from resentment (self-focused) or inspiration (other-focused). |
| Internship favor | Axis 1 + Axis 2 + Axis 3 | - | Ethical decision-making reveals all three: agency (do you own the choice?), contribution (fairness vs. favoritism), and radius (friend vs. strangers waiting). |

---

## The Branching Logic

Each main question branches on the first response, then some branches branch again. This creates a **decision tree with ~25+ nodes**, allowing different paths for different people.

**Example: Filmmaking (Q1)**

```
Q1: "What went through your head?"
├─ A (Think about needs) → Q1a: "What could you start without?"
│   ├─ A (Start with phone) → [Internal locus signal]
│   ├─ B (Need gear/quality) → [External locus signal]
│   └─ C (Not sure) → [External locus signal]
├─ B (Fired up, start now) → Q1b: "What if you did it imperfectly?"
│   ├─ A (That's freeing) → [Internal locus signal]
│   ├─ B (Feels cheap) → [External locus signal]
│   └─ C (Get frustrated) → [External locus signal]
└─ C (Someday) → Q1c: "Will someday actually come?"
    ├─ A (When life slows down) → [External locus signal]
    ├─ B (I'm avoiding) → [External locus signal]
    └─ C (Lower priority) → [Internal locus signal — recognizing choice]
```

**Trade-off:** The tree doesn't cover every possible life experience. It samples across domains (ambition, conflict, relationships, growth, ethics) to give a **representative sketch**, not a complete picture. More scenarios would be more comprehensive but also exponentially more complex.

---

## No Moralizing

The tree's tone is crucial. **It does not judge.**

When someone reveals entitlement ("I wasn't told to do it, so why should I?"), the reflection doesn't say "That's selfish." It says:

> "You expected them to read your mind. That's tough — because people aren't mind readers. You asked for understanding without actually asking for it."

This **acknowledges** the pattern without shaming. It's what a wise colleague would say after hearing your story.

The tree also doesn't pretend both paths are equally valid. If someone is stuck in external locus, the reflection gently points to what's possible: "You see the gap. That means you could close it with effort."

---

## Psychological Validity

All three axes are grounded in published research:

1. **Rotter, J. (1954).** "Social learning and clinical psychology." – The original locus of control work.
2. **Dweck, C. (2006).** "Mindset: The new psychology of success." – Growth vs. fixed mindset, which maps to internal vs. external locus.
3. **Organ, D. (1988).** "Organizational citizenship behavior: The good soldier syndrome." – OCB, the foundation for Axis 2.
4. **Campbell, M. et al. (2004).** "The psychology of entitlement." – How entitlement forms and persists.
5. **Maslow, A. (1969).** "Toward a psychology of being" (2nd ed.). – Self-transcendence, the theoretical foundation for Axis 3.

The questions themselves don't require expertise to answer — they're concrete moments from daily life. But the branching logic assumes the psychological principles above.

---

## What This Tree Does Well

1. **Captures patterns without being prescriptive.** It asks questions that reveal how someone is thinking, not how they should think.

2. **Sequences axes thoughtfully.** Axis 1 → Axis 2 → Axis 3 follows a natural progression: see your agency, then ask what you're doing with it, then ask who else is in your frame.

3. **Deterministic and auditable.** Every path is traceable. The same answers always lead to the same reflection. No randomness, no AI hallucination.

4. **Tone-aware.** Reflections are reframes, not lectures. They're what someone with emotional intelligence and perspective would say to a friend.

---

## Trade-offs and Limitations

1. **Limited coverage.** Six scenarios can't cover all of life. A more comprehensive tree might have 12-15 scenarios across more domains (health, learning, finances, creativity, spirituality).

2. **No follow-up beyond the session.** The tool creates awareness but doesn't track change. A future version could save session data and track patterns week-over-week.

3. **No personalization.** The tree is the same for everyone. A future version might adapt questions based on industry or role (e.g., engineer vs. manager).

4. **Requires honest self-reflection.** If someone is defending or lying to themselves, the tree won't catch it. It assumes good faith.

---

## If You Built This Yourself

If given more time, I would:

1. **Add 4-6 more scenarios** covering additional domains (physical health, learning, finances, creative expression).

2. **Implement variant branching** — some questions have 4 options instead of 3 for finer granularity.

3. **Add a data-export feature** so users could save their session and compare patterns over weeks/months.

4. **Create a manager or team version** where reflection is voluntary but shared (with privacy), revealing team patterns.

5. **Build narrative closure.** Currently, the summary is generic. A better version would reference specific answers: "You said X about your mom and Y about your friend. Notice the pattern..."

---

## Conclusion

The Daily Reflection Tree is a **structured conversation with yourself**. It's not therapy, not a quiz, not a judgment. It's an opportunity to notice — at 7pm, when you're tired and reflective — how you showed up today.

The power is in the noticing. Change comes after.