---
title: "Signals Directory"
description: "Repository for normalized signals following the signal lifecycle process from ingestion through quality assessment and validation to trusted status"
doc_type: "readme"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "signals"
tags: ["signals", "lifecycle", "evidence", "validation"]
related_docs: ["INDEX.md", "../README.md", "../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md"]
---

# Signals Directory

## Purpose

This directory contains normalized signals that follow the enterprise signal lifecycle process defined in `PROCESS-signal-01-signal-lifecycle.md`. Signals represent external inputs (market, regulatory, technology, user research, etc.) that have been detected, normalized, quality-assessed, and validated before consumption by downstream coveys.

## Signal Lifecycle

Signals progress through the following lifecycle states:

```
ingested → quality-assessed → trusted → retired
```

### Lifecycle States

- **`ingested`** - Signal received and normalized into standard schema, awaiting quality assessment
- **`quality-assessed`** - Signal passed basic quality checks and is eligible for validation
- **`trusted`** - Signal passed validation and can be consumed by downstream coveys (personas, vision, epics)
- **retired` - Signal is stale, superseded, or no longer relevant

### Quality Gates

**Quality Assessment (`ingested → quality-assessed`):**
- Source trust evaluation
- Completeness check
- Noise level assessment
- Basic consistency verification

**Validation (`quality-assessed → trusted`):**
- Cross-checking against other evidence
- Corroboration from multiple independent sources
- Consistency and timeliness verification
- Conflict detection and resolution

## Signal Categories

Signals are classified by collection agent category:

### Bibliographic Signals (`agent.signal.collection.bibliographic`)
- User research and interview findings
- Academic papers and whitepapers
- Industry reports and analyses
- News articles and publications
- **Example:** `signal-01-knowledge-worker-rag-demand.md`

### Market Signals (`agent.signal.collection.market`)
- Financial data and pricing
- Supply chain information
- Economic indicators
- Market trends

### Regulatory Signals (`agent.signal.collection.regulatory`)
- Laws and regulations
- Compliance updates
- Policy changes
- Legal filings

### Technology Signals (`agent.signal.collection.technology`)
- Patents and innovations
- Research breakthroughs
- Product releases
- Technical standards

### Environmental Signals (`agent.signal.collection.environmental`)
- Climate data
- Pollution metrics
- Ecosystem health indicators
- Environmental policy

### Social Signals (`agent.signal.collection.social`)
- Social media trends
- Community feedback
- NGO reports
- Public sentiment

### Operational Signals (`agent.signal.collection.operational`)
- Runtime telemetry
- System performance
- Operational metrics
- Infrastructure status

### Manual Signals (`agent.signal.collection.manual`)
- Analyst-curated inputs
- Expert observations
- Human-entered events
- Qualitative annotations

## Signal Structure

Each signal document includes:

### Required Frontmatter
- `artifact_type: "signal"`
- `signal_type` - Classification (user-research, market-demand, etc.)
- `signal_category` - Collection category
- `lifecycle_state` - Current state in lifecycle
- `confidence` - Evidence-based confidence score (0-1)
- `source` - Source metadata and reliability
- `responsible_agents` - Agent responsibilities
- `quality_assessment` - Quality evaluation status
- `validation` - Validation requirements and status

### Content Sections
1. **Signal Summary** - Brief description of the signal
2. **Signal Classification** - Type, category, domain, horizon
3. **Signal Strength Indicators** - Salience, urgency, impact, readiness
4. **Detailed Findings** - Comprehensive analysis
5. **Quality Assessment Status** - Completeness, trust, noise, consistency
6. **Validation Requirements** - Corroboration needs and conflict checks
7. **Linked Evidence** - Source documents and related research
8. **Next Steps** - Quality assessment and validation actions
9. **Evidence Ledger** - Confidence evolution tracking
10. **Lifecycle Decision Records** - State transition history

## Usage

### Adding New Signals

1. **Detect and Normalize**
   - Identify external input requiring normalization
   - Create signal document with standard structure
   - Set lifecycle state to `ingested`
   - Assign initial confidence score (typically 0.3-0.6)

2. **Quality Assessment**
   - Evaluate source trust, completeness, noise, consistency
   - Document quality assessment findings
   - If passes: update state to `quality-assessed`
   - If fails: mark for review or rejection

3. **Validation**
   - Gather corroborating evidence from independent sources
   - Cross-check for conflicts with existing trusted signals
   - Verify timeliness and relevance
   - Document validation evidence
   - If passes: update state to `trusted` with confidence ≥ 0.70

4. **Downstream Consumption**
   - Only `trusted` signals are consumed by default
   - Link signals to personas, vision seeds, epics
   - Track downstream artifact usage

### Signal Naming Convention

```
signal-[##]-[brief-descriptive-name].md
```

Examples:
- `signal-01-knowledge-worker-rag-demand.md`
- `signal-02-obsidian-market-growth.md`
- `signal-03-privacy-regulation-change.md`

## Responsible Agents

### Detection and Normalization
- **`agent.meta.signal.orchestrator`** - Coordinates signal processing workflows
- **`agent.signal.detection`** - Receives and normalizes raw signals
- **Collection agents** - Interface with specific external sources

### Quality and Validation
- **`agent.signal.quality.assessment`** - Evaluates signal quality
- **`agent.signal.validation`** - Cross-checks and validates signals
- **`agent.evidence.signal`** - Stores normalized signals and evidence

### Lifecycle Management
- **`agent.lifecycle.signal`** - Owns state machine and approves transitions

### Overlays and Analysis
- **`agent.signal.critic`** - Audits evidence and quality decisions
- **`agent.signal.salience`** - Analyzes trends and computes salience scores
- **`agent.signal.noise.gate`** - Filters and prioritizes signals

## Integration with Downstream Coveys

### Signal → Persona
- Personas synthesize insights from trusted signals
- Minimum signal confidence required: 0.70
- Personas track originating signals in frontmatter

### Signal → Vision
- Vision seeds emerge from convergent signals across personas
- Signals inform strategic opportunity identification
- Vision documents reference supporting signals

### Signal → Epic
- Epics validate against market/regulatory/technology signals
- Signals provide feasibility and viability evidence
- Epic confidence influenced by supporting signal strength

## Quality Standards

### Source Trust Levels
- **High:** Direct research, verified data sources, expert analysis
- **Medium:** Community feedback, secondary sources, aggregated data
- **Low:** Unverified reports, single-source claims, anecdotal evidence

### Completeness Criteria
- Problem/opportunity clearly defined
- Supporting evidence documented
- Context and constraints identified
- Impact quantified or estimated
- Actionability assessed

### Validation Evidence Requirements
- Minimum 3 independent corroborating sources for `trusted` state
- No unresolved conflicts with existing trusted signals
- Timeliness verified (not stale or outdated)
- Relevance to strategic objectives confirmed

## Examples

### Current Signals
- [signal-01-knowledge-worker-rag-demand](signal-01-knowledge-worker-rag-demand.md) - User research on RAG plugin demand (State: `ingested`)

## Next Steps

### For Current Signals
1. Perform quality assessment on `signal-01`
2. Gather validation evidence from Obsidian community
3. Validate technical feasibility
4. Promote to `trusted` state if criteria met

### For New Signals
1. Identify additional signals from market analysis
2. Detect regulatory signals affecting privacy/AI
3. Monitor technology signals for RAG advancements
4. Collect social signals from Obsidian community

## Related Documents

- [Signals Index](INDEX.md) - Navigation guide for signals
- [Research Directory](../README.md) - Parent research context
- [Signal Lifecycle Process](../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md) - Governing process
- [Work Standard](../../../../../enterprise/chl-standards/standards/WORK_STANDARD.md) - Meta-framework
- [Personas Directory](../../02-personas/README.md) - Downstream consumption
