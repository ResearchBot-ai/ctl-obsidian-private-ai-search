---
title: "Vision Content Proper Separation of Concerns (CORRECTED)"
description: "Correct allocation of Vision content across VISION_STANDARD.md and PROCESS-vision-01 following pure separation principles"
doc_type: "architecture-analysis"
author: "Claude (AI Assistant)"
version: "2.0"
last_updated: "2025-11-23"
status: "active"
category: "standards-refactoring"
tags: ["separation-of-concerns", "vision-standard", "process-vision-01", "architecture"]
---

# Vision Content Proper Separation of Concerns (CORRECTED)

## Core Principle: Structure vs. Process

**STANDARD = WHAT IT IS (Structure, Schema, States)**
**PROCESS = HOW TO DO IT (Steps, Formulas, Decisions)**

This principle is ABSOLUTE and applies to ALL content allocation decisions.

---

## Understanding INDEX.md vs README.md (CRITICAL)

### INDEX.md Purpose
**Primary Question:** "What files are available and how do I navigate them?"
**Content Focus:** File listings, categorization, cross-references, workflow paths
**Structure:** Organized, categorical, link-heavy navigation

### README.md Purpose
**Primary Question:** "What is DIRECTORY's purpose and why should I care?"
**Content Focus:** Context, purpose, getting started, background concepts
**Structure:** Conversational, explanatory, tutorial-style

### CRITICAL MISTAKE IN v1.0
The original analysis proposed creating `enterprise/chl-standards/INDEX.md` with:
- Artifact catalog table
- Confidence thresholds summary
- Agent orchestration chain
- Evidence flow diagram
- Migration guide

**THIS IS WRONG.** That content is conceptual/educational (README content), NOT navigation (INDEX content).

---

## Corrected Understanding: Where Meta-Framework Content Lives

### WORK_STANDARD.md IS the legacy Meta-Framework Overview
**Current status:** WORK_STANDARD.md exists and contains:
- Evidence flow relationships (Section 3)
- Confidence propagation (Section 4)
- Agent orchestration (Section 5)
- Confidence formulas (Section 9)
- Lifecycle matrix (Section 12)

**Strategy:** SLOWLY decompose WORK_STANDARD.md by moving content to individual standards/processes over time.

**NOT:** Delete/deprecate/archive WORK_STANDARD.md immediately
**NOT:** Replace it with INDEX.md (wrong file type)
**NOT:** Add deprecation notices

### What Happens to Meta-Framework Content

Keep WORK_STANDARD.md as the meta-framework overview for any processes that have not been explicitly decomposed into process documents
**MOVE** all Structure, Schema, States content for a **VISION** from WORK_STANDARD.md to the **VISION_STANDARD.md**
**MOVE** all Steps, Formulas, Decisions for a **VISION** from the WORK_STANDARD.md to the **PROCESS-vision-01**

---

## From WORK_STANDARD.md Vision Content Analysis

### Line 82: Vision Covey Context
```markdown
| **Vision** | 2 | What progress should we enable? | Viability / Strategic Alignment | `agent.vision.orchestrator` |
```

**Content Type:** STRUCTURE (What horizon, what question, what evidence types)

**Current Location:** WORK_STANDARD.md Section 3 (Evidence Flow Relationships)

**Move To:** VISION_STANDARD.md Section 1 (Overview)

**Rationale:** This defines WHAT the Vision artifact addresses (horizon, primary question, evidence types) - it's structural context.

**Action:** Add to VISION_STANDARD.md Section 1:
```markdown
## 1. Overview
...

**Artifact Context:**
- **Horizon:** 2 (Strategy)
- **Primary Question:** What progress should we enable?
- **Key Evidence Types:** Viability, Strategic Alignment
- **Orchestrator:** agent.vision.orchestrator
```

**WORK_STANDARD.md:** Remove Vision row from Section 3 table once moved

---

### Line 100: Vision Confidence Threshold
```markdown
| Vision | Persona | ≥ 0.75 |
```

**Content Type:** PROCESS (How to decide if Vision ready to promote from Persona)

**Current Location:** WORK_STANDARD.md Section 4 (Readiness and Confidence Propagation) Line 100

**Move To:** PROCESS-vision-01 Section 4.1 and Section 6.1

**Rationale:** This threshold is an operational rule (WHEN/HOW to decide Vision ready to promote) - this is process logic for Vision specifically.

**Status:** ✅ ALREADY MOVED - PROCESS-vision-01 has threshold ≥0.75 at Section 4.1 and 6.1

**WORK_STANDARD.md:** Remove ONLY the Vision row (`Vision | Persona | ≥ 0.75`) from Section 4 table once confirmed in PROCESS-vision-01

**Note:** Line 101 (`UXJ | Vision | ≥ 0.75`) stays in WORK_STANDARD.md - it's UXJ content, not Vision content

---

### Line 116: Agent Chain
```markdown
| Personas | Vision | `agent.vision.orchestrator` |
```

**Content Type:** STRUCTURE (What agent orchestrates this transition)

**Current Location:** WORK_STANDARD.md Section 5 (Agent Orchestration)

**Move To:** VISION_STANDARD.md Section 10/14 (Agent Orchestration Context / Related Processes)

**Rationale:** Identifying WHICH agent handles the transition is structural (WHAT agent), not HOW the agent works.

**Status:** ✅ ALREADY MOVED - VISION_STANDARD.md lists agent.vision.orchestrator in Sections 10 and 14

**WORK_STANDARD.md:** Remove Persona→Vision agent chain row from Section 5 table once confirmed in VISION_STANDARD.md

---

### Line 586: Confidence Formula
```python
vision.confidence = mean(persona.confidence for linked_personas)
```

**Content Type:** PROCESS (How to calculate confidence)

**Current Location:** WORK_STANDARD.md Section 9 (Confidence Formulas)

**Move To:** PROCESS-vision-01 Section 6.2 (Confidence Calculations)

**Rationale:** Formulas are calculation methods (HOW to compute) - operational procedure, not structure.

**Status:** ⚠️ PARTIALLY MOVED - PROCESS-vision-01 Section 6.2 has seed-based formulas but MISSING persona-based aggregation

**Action:** Add to PROCESS-vision-01 Section 6.2 as Method 4:
```markdown
#### Method 4: Multiple Personas Aggregation

When synthesizing Vision from multiple Personas (each Persona already has aggregated confidence from its seeds):

\```python
# Step 1: Each Persona has aggregated confidence from its seeds
persona_01.confidence = 0.85
persona_02.confidence = 0.80

# Step 2: Aggregate across Personas (simple mean)
vision.confidence = mean([persona.confidence for persona in linked_personas])
# Example: (0.85 + 0.80) / 2 = 0.825
\```
```

**WORK_STANDARD.md:** Remove Vision formula from Section 9 once added to PROCESS-vision-01

---

### Line 631: Experiments and Evidence Steward
```markdown
| Vision | `agent.vision.orchestrator` | `viability`, `strategic-alignment`, `market` | `agent.evidence.vision` |
```

**Content Type:** MIXED
- Experiment types (`viability`, `strategic-alignment`, `market`) = PROCESS (what experiments validate the Vision)
- Evidence steward agent (`agent.evidence.vision`) = STRUCTURE (what agent manages evidence)

**Current Location:** WORK_STANDARD.md Section (Experiments)

**Move To:**
- Experiment types → PROCESS-vision-01 Section 5 Phase 2 (Experimental Context)
- Evidence steward agent → VISION_STANDARD.md Section 10 (Agent Orchestration Context)

**Rationale:**
- Experiment types define HOW the Vision is validated (process)
- Agent identity defines WHAT agent has a role (structure)

**Status:** ✅ ALREADY MOVED
- Experiments listed in PROCESS-vision-01 Phase 2
- agent.evidence.vision listed in VISION_STANDARD.md Section 10

**WORK_STANDARD.md:** Remove Vision experiment row from experiments table once confirmed in both files

---

### Line 678: Lifecycle States
```markdown
| Vision | `seeded → hypothesized → validated → guiding → monitored` | Vision Seeds ≥1 |
```

**Content Type:** MIXED
- State names/sequence (`seeded → hypothesized → validated → guiding → monitored`) = STRUCTURE (what states exist)
- Transition criterion (`Vision Seeds ≥1`) = PROCESS (when to transition)

**Current Location:** WORK_STANDARD.md Section 12 (Lifecycle Matrix)

**Move To:**
- State names/sequence → VISION_STANDARD.md Section 9 (Lifecycle States)
- Transition criteria → PROCESS-vision-01 (Phase transitions)

**Rationale:**
- State NAMES and SEQUENCE define WHAT states exist (structure)
- Transition criteria define WHEN to move between states (process logic)

**Status:** ✅ ALREADY MOVED
- VISION_STANDARD.md Section 9 lists state names/sequence (Entry/Exit criteria removed today)
- PROCESS-vision-01 defines transition criteria throughout process phases

**WORK_STANDARD.md:** Remove Vision row from Section 12 Lifecycle Matrix once confirmed properly split between VISION_STANDARD.md and PROCESS-vision-01

---

## What ACTUALLY Belongs in VISION_STANDARD.md

### Keep (Structure - WHAT IT IS):
1. ✅ **YAML Frontmatter Schema** (Section 3) - What fields exist, their types
2. ✅ **Vision Hypothesis Template** (Section 5) - What sections/format the hypothesis uses
3. ✅ **Evidence Ledger Schema** (Section 8) - What fields exist in evidence entries
4. ✅ **Lifecycle States** (Section 9) - What states exist, their names, sequence
5. ✅ **Agent Orchestration Context** (Section 10) - What agents exist, their roles (not HOW they work)
6. ✅ **File Naming Convention** (Section 12) - What the file naming pattern is
7. ✅ **Integration with Other Standards** (Section 13) - What other standards relate
8. ✅ **Related Processes** (Section 14) - What process files exist

### Consider Adding (Structure):
- **Horizon/Primary Question** (Section 1) - What horizon/question this artifact addresses

### Remove if Exists (Process - HOW TO DO IT):
- ❌ Confidence thresholds (HOW to decide if ready)
- ❌ Confidence formulas (HOW to calculate)
- ❌ Step-by-step procedures (HOW to create)
- ❌ Quality gates (HOW to validate)
- ❌ Promotion criteria (WHEN to advance)
- ❌ Entry/Exit criteria for states (WHEN to transition)

---

## What ACTUALLY Belongs in PROCESS-vision-01

### Keep (Process - HOW TO DO IT):
1. ✅ **Promotion Decision Criteria** (Section 4) - WHEN seeds are ready
2. ✅ **All 8 Process Phases** (Section 5) - HOW to execute promotion
3. ✅ **Confidence Thresholds** (Section 6.1) - What minimum confidence is required
4. ✅ **Confidence Calculation Methods** (Section 6.2) - HOW to calculate confidence
5. ✅ **Synthesis Patterns** (Section 7) - HOW to synthesize multiple seeds
6. ✅ **Decision Points** (Section 8) - WHEN to make specific decisions
7. ✅ **Quality Gates** (Section 9) - HOW to validate quality
8. ✅ **Governance** (Section 10) - HOW consent circles work

### Add (Missing Process):
1. ✅ **Experimental context** (Phase 2) - DONE
2. **Multi-persona confidence aggregation** (Section 6.2 Method 4) - PENDING

---

## What Happens to WORK_STANDARD.md

### Current Strategy (User's Direction)
**"We are slowly moving each work item out of the WORK_STANDARD.md"**

This means:
1. WORK_STANDARD.md continues to exist as the **legacy** meta-framework overview
2. For each artifact (Vision, Epic, Feature, etc.), content is **MOVED** to individual STANDARD and PROCESS files
3. WORK_STANDARD.md is NOT deprecated/archived yet - it holds content for artifacts not yet decomposed
4. References to WORK_STANDARD.md should be REMOVED from individual PROCESS files (they must be self-contained)

### What Happens to Vision Content in WORK_STANDARD.md

**MOVE** to VISION_STANDARD.md:
- Line 82: Vision Covey Context (Horizon, Primary Question, Evidence Types, Orchestrator)
- Line 116: Agent Chain (Persona → Vision orchestrator)
- Line 678: Lifecycle State names/sequence

**MOVE** to PROCESS-vision-01:
- Lines 100-101: Confidence thresholds
- Line 586: Confidence formula (persona aggregation)
- Line 631: Experiment types
- Line 678: Lifecycle transition criteria

**REMOVE** from WORK_STANDARD.md:
Once all Vision content is confirmed moved/distributed, remove Vision rows from WORK_STANDARD.md tables

### What NOT to Do
- ❌ Add deprecation notice to WORK_STANDARD.md
- ❌ Archive WORK_STANDARD.md now
- ❌ Create INDEX.md to replace WORK_STANDARD.md (wrong file type)
- ❌ Move WORK_STANDARD.md content to INDEX.md (conceptual content ≠ navigation)

### What TO Do
- ✅ Remove WORK_STANDARD.md references from PROCESS files (make them self-contained)
- ✅ **MOVE** Structure/Schema/States from WORK_STANDARD.md to STANDARD files
- ✅ **MOVE** Steps/Formulas/Decisions from WORK_STANDARD.md to PROCESS files
- ✅ Keep WORK_STANDARD.md as legacy overview until all artifacts decomposed
- ✅ Eventually: WORK_STANDARD.md can be deprecated once all content moved

---

## Corrected Action Plan

### 1. PROCESS-vision-01 Updates (HOW TO DO IT)
- [x] Section 5 Phase 2: Add experimental context ✅ DONE
- [x] Remove all references to "per WORK_STANDARD.md" ✅ DONE
- [ ] Section 6.2: Add Method 4 (multi-persona aggregation from WORK_STANDARD line 586) - **REQUIRED**

### 2. VISION_STANDARD.md Updates (WHAT IT IS)
- [x] Section 9: Remove Entry/Exit criteria (keep only state names/descriptions) ✅ DONE
- [ ] Section 1: Add Artifact Context (Horizon, Primary Question, Evidence Types, Orchestrator from WORK_STANDARD line 82) - **OPTIONAL**

### 3. WORK_STANDARD.md Vision Content Removal
- [ ] Once Vision content confirmed moved, remove Vision rows from:
  - Section 3 (Evidence Flow) - Vision Covey Context
  - Section 4 (Confidence Propagation) - Vision threshold
  - Section 5 (Agent Orchestration) - Persona→Vision chain
  - Section 9 (Confidence Formulas) - Vision formula
  - Section 12 (Lifecycle Matrix) - Vision lifecycle
- [ ] WORK_STANDARD.md continues to hold content for artifacts NOT yet decomposed (Persona, UXJ, Epic, Feature, Story, Task, etc.)
- [ ] DO NOT deprecate or archive WORK_STANDARD.md yet

### 4. INDEX.md Decision
- ❌ Do NOT create `enterprise/chl-standards/INDEX.md` with artifact catalog
- ✅ INDEX files are ONLY for file navigation ("what files exist and how to navigate")
- ✅ Artifact catalog/confidence chains/evidence flow are conceptual content
- ✅ Conceptual content stays in WORK_STANDARD.md (for non-decomposed artifacts) or individual STANDARD Section 1 (for decomposed artifacts)

---

## Summary

### File Type Separation

**VISION_STANDARD.md (STANDARD file) - WHAT IT IS**
- Vision artifact structure (YAML schema, sections, states)
- Agent roles (which agents, not how they work)
- File naming conventions
- Template structures
- Receives STRUCTURE content moved FROM WORK_STANDARD.md

**PROCESS-vision-01 (PROCESS file) - HOW TO DO IT**
- Vision Seeds promotion process (8 phases)
- Confidence calculations (formulas, thresholds)
- Quality gates and decision points
- Synthesis patterns and governance
- Receives PROCESS content moved FROM WORK_STANDARD.md
- Self-contained (no WORK_STANDARD references)

**WORK_STANDARD.md (Legacy Meta-Framework Overview)**
- Holds content for artifacts NOT yet decomposed
- Vision content being MOVED OUT to VISION_STANDARD.md and PROCESS-vision-01
- Remains for Persona, UXJ, Epic, Feature, Story, Task content
- Eventually deprecated once all artifacts decomposed

**INDEX.md (NOT APPLICABLE HERE)**
- INDEX files are ONLY for file navigation ("what files exist and how to navigate")
- NOT for conceptual content (artifact catalogs, confidence chains, evidence flow)
- Original v1.0 plan to create INDEX.md with artifact catalog was WRONG

### Principle Applied Correctly

**STANDARD = WHAT IT IS** (Structure, Schema, States)
**PROCESS = HOW TO DO IT** (Steps, Formulas, Decisions)
**README = WHY IT MATTERS** (Context, Purpose, Background)
**INDEX = WHERE TO FIND IT** (File Listings, Navigation)

### Migration Pattern for Vision

```
WORK_STANDARD.md (Vision content)
    ├─→ VISION_STANDARD.md (Structure/Schema/States)
    └─→ PROCESS-vision-01 (Steps/Formulas/Decisions)

Then: Remove Vision rows from WORK_STANDARD.md tables
```

This same pattern applies to ALL artifacts as they're decomposed.

---

*Corrected analysis v2.0 with proper understanding of MOVE directive and file type purposes*
