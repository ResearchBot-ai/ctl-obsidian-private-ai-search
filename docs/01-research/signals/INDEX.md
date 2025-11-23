---
title: "Signals Index"
description: "Navigation guide for signals following the enterprise signal lifecycle"
doc_type: "index"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "navigation"
tags: ["index", "navigation", "signals", "lifecycle"]
related_docs: ["README.md", "../INDEX.md"]
---

# Signals Index

## Directory Purpose

This directory contains normalized signals that follow the enterprise signal lifecycle process. Signals progress from `ingested` → `quality-assessed` → `trusted` → `retired` states, with each transition governed by evidence-based quality gates.

## Quick Navigation

### Current Signals by Lifecycle State

#### Ingested (Awaiting Quality Assessment)
- [signal-01-knowledge-worker-rag-demand.md](signal-01-knowledge-worker-rag-demand.md) - User research on RAG plugin demand
  - **Type:** User Research / Bibliographic
  - **Confidence:** 0.55
  - **Status:** Requires quality assessment
  - **Next Step:** Evaluate completeness, source trust, noise level, consistency

#### Quality-Assessed (Awaiting Validation)
*No signals currently in this state*

#### Trusted (Available for Downstream Consumption)
*No signals currently in this state*

#### Retired (Archived)
*No signals currently in this state*

## Signal Categories

### By Collection Agent

**Bibliographic Signals** (`agent.signal.collection.bibliographic`)
- signal-01-knowledge-worker-rag-demand.md (ingested)

**Market Signals** (`agent.signal.collection.market`)
- *None yet*

**Regulatory Signals** (`agent.signal.collection.regulatory`)
- *None yet*

**Technology Signals** (`agent.signal.collection.technology`)
- *None yet*

**Environmental Signals** (`agent.signal.collection.environmental`)
- *None yet*

**Social Signals** (`agent.signal.collection.social`)
- *None yet*

**Operational Signals** (`agent.signal.collection.operational`)
- *None yet*

**Manual Signals** (`agent.signal.collection.manual`)
- *None yet*

### By Signal Type

**User Research**
- signal-01-knowledge-worker-rag-demand.md

**Market Demand**
- *None yet*

**Regulatory Change**
- *None yet*

**Technology Innovation**
- *None yet*

## Signal Lifecycle Process

### Ingestion Phase
New signals enter at `ingested` state after normalization by `agent.signal.detection`.

**Current Tasks:**
- [ ] Quality assess signal-01-knowledge-worker-rag-demand
- [ ] Document quality assessment findings
- [ ] Decide on promotion to `quality-assessed`

### Quality Assessment Phase
Signals in `quality-assessed` state have passed initial quality checks and are eligible for validation.

**Quality Criteria:**
- Source trust level confirmed
- Completeness requirements met
- Noise level acceptable
- Basic consistency verified

### Validation Phase
Signals undergo corroboration, conflict checking, and market validation before reaching `trusted` state.

**Validation Requirements:**
- Minimum 3 independent corroborating sources
- No conflicts with existing trusted signals
- Technical feasibility confirmed
- Market relevance validated

### Trusted State
Only `trusted` signals are consumed by downstream coveys (Personas, Vision, Epics).

**Consumption Pattern:**
- Personas synthesize insights from trusted signals (confidence ≥ 0.70)
- Vision seeds emerge from convergent signals
- Epics validate against market/regulatory/technology signals

## Adding New Signals

### Signal Creation Workflow

1. **Detection and Normalization**
   - Identify external input requiring signal processing
   - Create signal document using standard structure
   - Set lifecycle state to `ingested`
   - Assign initial confidence (typically 0.3-0.6)
   - Document source and metadata

2. **Quality Assessment**
   - Evaluate completeness, trust, noise, consistency
   - Document quality assessment findings
   - Update state to `quality-assessed` if criteria met
   - Record quality decision in evidence ledger

3. **Validation**
   - Gather corroborating evidence
   - Cross-check for conflicts
   - Verify timeliness and relevance
   - Update state to `trusted` with confidence ≥ 0.70
   - Record validation decision

4. **Downstream Linking**
   - Link to consuming personas
   - Track in vision seeds
   - Reference in epics and features

### Naming Convention

```
signal-[##]-[brief-descriptive-name].md
```

Use sequential numbering and descriptive names that capture the signal essence.

## Responsible Agents

### Signal Processing
- **`agent.meta.signal.orchestrator`** - Workflow coordination
- **`agent.signal.detection`** - Normalization and ingestion
- **`agent.signal.quality.assessment`** - Quality evaluation
- **`agent.signal.validation`** - Evidence validation

### Evidence and Lifecycle
- **`agent.evidence.signal`** - Evidence storage
- **`agent.lifecycle.signal`** - State machine ownership

### Analysis and Overlays
- **`agent.signal.critic`** - Quality auditing
- **`agent.signal.salience`** - Trend analysis
- **`agent.signal.noise.gate`** - Filtering and prioritization

## Work Queue

### Immediate Actions Needed

**Signal-01: Knowledge Worker RAG Demand**
1. ✓ Signal created and normalized
2. ⏳ Quality assessment pending
3. ⏳ Validation evidence gathering needed
4. ⏳ Promotion to trusted state pending

### Upcoming Signals to Create

**Market Analysis Signals**
- Obsidian market growth and user demographics
- PKM tool competitive landscape
- AI plugin adoption rates

**Technology Signals**
- RAG architecture advancements
- Privacy-preserving AI technologies
- Cross-device synchronization solutions

**Social Signals**
- Obsidian community sentiment analysis
- Feature request patterns
- User pain point discussions

**Regulatory Signals**
- AI privacy regulations affecting plugin development
- Data sovereignty requirements
- Compliance frameworks for knowledge management tools

## Quality Metrics Dashboard

### Overall Signal Health

| Metric | Count | Target |
|--------|-------|--------|
| Total Signals | 1 | - |
| Ingested | 1 | < 30% of total |
| Quality-Assessed | 0 | < 20% of total |
| Trusted | 0 | > 50% of total |
| Retired | 0 | < 10% of total |

### Average Confidence by State
- Ingested: 0.55
- Quality-Assessed: N/A
- Trusted: N/A (target: ≥ 0.70)

### Validation Success Rate
- Signals promoted to trusted: 0/0 (N/A)
- Signals rejected or held: 0/0 (N/A)

## Related Documents

- [Signals Directory Purpose](README.md) - Comprehensive signal documentation
- [Research Index](../INDEX.md) - Parent research navigation
- [Signal Lifecycle Process](../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md) - Governing process
- [Work Standard](../../../../../enterprise/chl-standards/standards/WORK_STANDARD.md) - Meta-framework
- [Personas Directory](../../02-personas/INDEX.md) - Downstream consumption
- [Vision Directory](../../03-vision/INDEX.md) - Strategic synthesis
