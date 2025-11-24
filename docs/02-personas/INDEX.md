---
title: "Personas Index"
description: "Navigation guide for personas - validated user archetypes derived from signals and evidence"
doc_type: "index"
author: "Devin Hedge"
version: "1.1"
last_updated: "2025-11-23"
status: "active"
category: "navigation"
tags: ["index", "navigation", "personas", "user-research"]
related_docs: ["README.md", "../01-research/signals/signal-01-knowledge-worker-rag-demand.md"]
---

# Personas Index

## Directory Purpose

User personas and empathy mapping artifacts that capture validated behavioral, motivational, and contextual insights about user segments. Personas are evidence-driven knowledge containers that inform vision synthesis, UX journey mapping, and product development.

## Quick Navigation

### Active Personas

#### Validated (Ready for UXJ and Epic Development)

1. **[persona-01-advanced-knowledge-worker](./persona-01-advanced-knowledge-worker.md)**
   - **Segment:** Advanced knowledge workers with large Obsidian vaults (1000+ notes) and strict privacy requirements
   - **State:** validated
   - **Confidence:** 0.85 (high)
   - **Created:** 2025-11-23
   - **Originating Signal:** [signal-01-knowledge-worker-rag-demand](../01-research/signals/signal-01-knowledge-worker-rag-demand.md) (trusted, confidence 1.00)
   - **Key Characteristics:**
     - Privacy-focused professional in critical infrastructure domains
     - Uses sophisticated knowledge management frameworks (PARRA, C-O-D-E)
     - Seeks to reclaim 2-3 hours daily through AI-powered knowledge synthesis
     - Technical sophistication with advanced tools (LangGraph, vector databases)
     - Non-negotiable data sovereignty and privacy requirements
   - **Pain Points:**
     - Search overload and synthesis inefficiency (costs 2-3 hours daily)
     - Privacy-performance trade-off with existing AI plugins
     - Workflow bottleneck at organization and distillation phases
   - **Vision Seeds:**
     - VISION-SEED-01: Privacy-First-RAG (confidence 0.90)
     - VISION-SEED-02: Knowledge-Synthesis-Assistant (confidence 0.85)
     - VISION-SEED-03: Semantic-Knowledge-Graph (confidence 0.75)
   - **Next Steps:** UX journey mapping, epic planning, vision seed promotion

### Persona Lifecycle States

This project follows the USER_PERSONA_STANDARD.md lifecycle:
- `draft` - Initial persona creation
- `in discovery` - Active data collection and validation
- `partially-defined` - Some sections validated (≥50% confidence)
- `validated` - Core sections complete (≥0.80 confidence) - READY FOR UXJ/EPIC WORK
- `vision-seeding` - Contributing to vision emergence
- `monitored` - Active telemetry maintaining persona state
- `needs-revision` - Conflicting or outdated data detected
- `archived` - Persona retired or merged

### Persona Categories (00-99 System)

This project follows the enterprise standard persona numbering:
- **00:** Shared/Cross-cutting personas
- **01-09:** Paying customers (excluding internal users)
- **10-19:** Administrative users
- **20-29:** Business users
- **30-39:** Executive users
- **40-49:** Technical users
- **50-59:** AI/System agents
- **90-99:** Special/Edge cases

Current personas in this project:
- **01:** Advanced knowledge worker (category 01-09: paying customer)

### Adding Content

When adding personas to this directory:

1. **Follow naming convention:** `persona-[##]-[descriptive-name].md`
2. **Use enterprise template:** Reference `../../../../../enterprise/chl-standards/templates/template-user-persona.md`
3. **Link to originating signal:** All personas MUST trace to trusted signals
4. **Include YAML frontmatter:** Complete all required metadata fields
5. **Populate evidence ledger:** All assertions MUST be backed by evidence sources
6. **Update this INDEX.md:** Add persona to appropriate section based on lifecycle state
7. **Follow governance rules:** Evidence-backed sections, qualitative foundation for readiness, summary-not-source rule

## Evidence and Validation

### Evidence Requirements

Per USER_PERSONA_STANDARD.md governance rules:
- **Evidence-backed sections:** All populated sections MUST have corresponding evidence ledger entries
- **Qualitative foundation:** Advancing beyond `draft` REQUIRES qualitative or experimental evidence for core sections (identity, psychographics, pain points, JTBD)
- **Summary-not-source:** Persona prose MUST summarize underlying research artifacts, not introduce new claims
- **Research separation:** Raw research lives in `../01-research/user-insights/`, not embedded in personas

### Confidence Thresholds

Per WORK_STANDARD.md:
- **Persona from Signal:** ≥0.70 confidence required
- **Vision from Persona:** ≥0.75 confidence required (downstream)
- **UXJ from Vision:** ≥0.75 confidence required (downstream)

## File Organization

Files in this directory follow:
- **USER_PERSONA_STANDARD.md** - Persona structure and lifecycle management
- **DOCUMENTATION_STANDARD.md** - General documentation requirements
- **WORK_STANDARD.md** - Evidence-driven work framework

## Related Documents

### Project Context
- [Directory Purpose and Usage](README.md) - Detailed information about this directory
- [Project Index](../../INDEX.md) - Root project navigation
- [Research Directory](../01-research/README.md) - Evidence and signals

### Enterprise Standards
- [User Persona Standard](../../../../../enterprise/chl-standards/standards/USER_PERSONA_STANDARD.md) - Persona specification
- [Persona Template](../../../../../enterprise/chl-standards/templates/template-user-persona.md) - Template for new personas
- [Work Standard](../../../../../enterprise/chl-standards/standards/WORK_STANDARD.md) - Work decomposition framework

### Signals and Evidence
- [signal-01-knowledge-worker-rag-demand](../01-research/signals/signal-01-knowledge-worker-rag-demand.md) - Trusted signal (confidence 1.00) for persona-01

### Downstream Artifacts
- [Vision Directory](../03-vision/README.md) - Vision seeds and strategic direction
- [UX Journeys Directory](../04-ux-journeys/README.md) - User experience journeys (to be created)
- [Epics Directory](../05-epics/README.md) - Epic planning (to be created)
