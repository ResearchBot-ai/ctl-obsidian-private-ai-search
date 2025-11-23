---
title: "Signal Quality Assessment Guide"
description: "Criteria and procedures for assessing signal quality and promoting signals from ingested to quality-assessed state"
doc_type: "process-guide"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "quality-assessment"
tags: ["quality", "assessment", "signals", "process", "validation"]
related_docs: ["README.md", "INDEX.md", "../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md"]
---

# Signal Quality Assessment Guide

## Purpose

This guide defines the criteria and procedures for assessing signal quality according to the enterprise signal lifecycle process (`PROCESS-signal-01-signal-lifecycle.md`). Quality assessment determines whether a signal in `ingested` state is eligible for promotion to `quality-assessed` state and subsequent validation.

## Quality Assessment Overview

### Responsible Agent
**`agent.signal.quality.assessment`** - Evaluates signal source trust, completeness, noise, and basic consistency

### Decision Authority
**`agent.lifecycle.signal`** - Approves or rejects lifecycle transitions based on quality assessment recommendations

### Process Flow
```
ingested → [Quality Assessment] → quality-assessed OR needs-review/rejected
```

## Quality Dimensions

Quality assessment evaluates four key dimensions:

### 1. Source Trust
**Definition:** Reliability and credibility of the signal source

**Evaluation Criteria:**

**HIGH Trust Sources:**
- Direct primary research (user interviews, surveys with methodology)
- Verified official data (government statistics, regulatory filings)
- Peer-reviewed academic research
- Expert analysis from recognized authorities
- First-hand operational telemetry
- **Confidence Impact:** +0.2 to +0.3

**MEDIUM Trust Sources:**
- Community feedback with multiple data points
- Secondary analysis from reputable sources
- Aggregated market data from known providers
- Industry reports from established firms
- Professional analyst opinions
- **Confidence Impact:** +0.1 to +0.2

**LOW Trust Sources:**
- Single anecdotal reports
- Unverified social media posts
- Rumor or speculation
- Sources with known bias or conflicts of interest
- Outdated or superseded information
- **Confidence Impact:** -0.1 to 0.0 (may block promotion)

**Assessment Questions:**
- Who produced this signal?
- What is their expertise and track record?
- What methodology was used?
- Are there potential biases or conflicts of interest?
- How recent is the source?

### 2. Completeness
**Definition:** Sufficient detail and context for actionability

**Evaluation Criteria:**

**COMPLETE Signals:**
- ✓ Problem/opportunity clearly defined
- ✓ Supporting evidence documented
- ✓ Context and constraints identified
- ✓ Impact quantified or estimated
- ✓ Actionability clear (what could be done)
- ✓ Relevant stakeholders/personas identified
- **Confidence Impact:** +0.1 to +0.2

**PARTIAL Signals:**
- ✓ Core issue identified
- ~ Some supporting evidence
- ~ Limited context
- ~ Impact mentioned but not quantified
- ~ Possible actions hinted at
- **Confidence Impact:** 0.0 to +0.1 (may require enrichment)

**INCOMPLETE Signals:**
- ✗ Vague problem statement
- ✗ Little or no evidence
- ✗ Missing context
- ✗ Impact unknown
- ✗ No clear actionability
- **Confidence Impact:** -0.2 to 0.0 (blocks promotion)

**Assessment Questions:**
- Is the problem/opportunity well-defined?
- Is there sufficient evidence to understand the signal?
- Do we know the context and constraints?
- Can we quantify or estimate the impact?
- Is it clear what actions this signal suggests?
- Are gaps documentable and addressable?

### 3. Noise Level
**Definition:** Ratio of relevant signal content to irrelevant information

**Evaluation Criteria:**

**LOW Noise (High Signal-to-Noise):**
- Focused, specific findings
- Relevant details only
- Clear cause-effect relationships
- Consistent narrative
- Minimal speculation or tangents
- **Confidence Impact:** +0.1 to +0.2

**MEDIUM Noise:**
- Mix of relevant and tangential information
- Some speculation or hypotheses
- Occasional inconsistencies
- Requires filtering to extract core signal
- **Confidence Impact:** 0.0 to +0.1

**HIGH Noise (Low Signal-to-Noise):**
- Mostly irrelevant information
- Heavy speculation or conjecture
- Contradictory statements
- Difficult to extract actionable insight
- **Confidence Impact:** -0.2 to 0.0 (may block promotion)

**Assessment Questions:**
- How much of the content is directly relevant?
- Are there contradictions or inconsistencies?
- Is speculation clearly separated from facts?
- Can core insights be easily extracted?
- Would additional filtering improve clarity?

### 4. Basic Consistency
**Definition:** Internal coherence and alignment with known facts

**Evaluation Criteria:**

**HIGHLY Consistent:**
- Internal logic sound
- No contradictions within the signal
- Aligns with established facts
- Plausible cause-effect relationships
- Consistent with domain knowledge
- **Confidence Impact:** +0.1 to +0.2

**MOSTLY Consistent:**
- Generally logical but with minor questions
- Few internal contradictions (explainable)
- Mostly aligns with known facts
- Some relationships need clarification
- **Confidence Impact:** 0.0 to +0.1

**INCONSISTENT:**
- Internal contradictions
- Conflicts with well-established facts
- Illogical relationships
- Implausible claims without justification
- **Confidence Impact:** -0.2 to 0.0 (blocks promotion)

**Assessment Questions:**
- Are there internal contradictions?
- Does this align with established facts?
- Are cause-effect relationships plausible?
- Do claims align with domain knowledge?
- Are inconsistencies explainable or concerning?

## Quality Assessment Procedure

### Step 1: Review Signal Document

**Actions:**
1. Read signal summary and detailed findings
2. Review source metadata and methodology
3. Check evidence references
4. Note initial impressions

**Outputs:**
- Understanding of signal content
- Identification of potential quality issues
- List of areas requiring deeper assessment

### Step 2: Evaluate Each Quality Dimension

**Actions:**
1. **Source Trust:** Assess source reliability using criteria above
2. **Completeness:** Check for required information and gaps
3. **Noise Level:** Evaluate signal-to-noise ratio
4. **Basic Consistency:** Verify internal coherence and factual alignment

**Outputs:**
- Rating for each dimension (High/Medium/Low)
- Confidence impact score for each dimension
- Documentation of assessment rationale

### Step 3: Calculate Quality Score

**Formula:**
```
Quality Score = (Source Trust Rating + Completeness Rating + (1 - Noise Level) + Consistency Rating) / 4
```

**Rating Scale:**
- High: 1.0
- Medium: 0.5
- Low: 0.0

**Example:**
- Source Trust: HIGH (1.0)
- Completeness: MEDIUM (0.5)
- Noise Level: LOW (inverted = 1.0)
- Consistency: HIGH (1.0)
- **Quality Score:** (1.0 + 0.5 + 1.0 + 1.0) / 4 = **0.875**

### Step 4: Determine Quality Threshold

**Promotion Thresholds:**
- **Quality Score ≥ 0.70:** Eligible for promotion to `quality-assessed`
- **Quality Score 0.50-0.69:** Needs enrichment before promotion
- **Quality Score < 0.50:** Not eligible (needs-review or rejected)

**Special Cases:**
- Any dimension rated "LOW" with blocking impact → automatic rejection
- Critical gaps in completeness → needs enrichment
- High noise obscuring core signal → needs filtering

### Step 5: Update Confidence Score

**Confidence Adjustment:**
```
New Confidence = Current Confidence + Sum(Dimension Impacts)
```

**Bounds:**
- Minimum: 0.0
- Maximum: 1.0 (at this stage; full validation can exceed)

**Example (signal-01):**
- Current: 0.55
- Source Trust: +0.2 (HIGH)
- Completeness: +0.05 (MODERATE - single source)
- Noise: +0.15 (LOW noise)
- Consistency: +0.15 (HIGH)
- **New Confidence:** 0.55 + 0.55 = **1.0** (capped)

### Step 6: Document Quality Assessment

**Required Documentation:**

```yaml
quality_assessment:
  assessed_by: "agent.signal.quality.assessment"
  assessed_at: "2025-11-23T15:30:00Z"
  quality_score: 0.875
  dimensions:
    source_trust:
      rating: "high"
      confidence_impact: 0.2
      rationale: "Direct user research with detailed methodology"
    completeness:
      rating: "medium"
      confidence_impact: 0.05
      rationale: "Comprehensive detail but single user source (N=1)"
      gaps: ["Market size validation", "Additional user interviews"]
    noise_level:
      rating: "low"
      confidence_impact: 0.15
      rationale: "Highly specific and actionable findings"
    consistency:
      rating: "high"
      confidence_impact: 0.15
      rationale: "Coherent narrative, aligns with domain knowledge"
  decision: "promote-to-quality-assessed"
  confidence_update:
    before: 0.55
    after: 1.0
    capped: true
  next_steps: ["Gather validation evidence", "Corroborate with community signals"]
```

### Step 7: Create Lifecycle Decision Record

**Structure:**

```yaml
lifecycle_events:
  - signal_id: "signal-01-knowledge-worker-rag-demand"
    from_state: "ingested"
    to_state: "quality-assessed"
    decided_at: "2025-11-23T15:30:00Z"
    proposed_by: "agent.signal.quality.assessment"
    decision_maker: "agent.lifecycle.signal"
    quality_gate:
      quality_score: 0.875
      threshold_met: true
      blocking_issues: []
    rationale: "Signal meets quality thresholds for validation phase"
    confidence_change:
      before: 0.55
      after: 1.0
    next_phase: "validation"
    validation_requirements:
      - "Corroborate with Obsidian community signals"
      - "Validate market size and demand"
      - "Assess technical feasibility"
      - "Confirm user segment representation"
```

## Quality Assessment Examples

### Example 1: signal-01-knowledge-worker-rag-demand

**Signal Context:**
- Source: Direct user research (interview + profile)
- Sample size: N=1
- Detail level: High
- Specificity: Very specific findings

**Quality Assessment:**

**Source Trust: HIGH (1.0)**
- Direct primary research
- Detailed methodology documented
- Consistent, specific responses
- Technical depth validates expertise
- **Impact:** +0.2

**Completeness: MEDIUM (0.5)**
- ✓ Clear problem definition
- ✓ Detailed evidence
- ✓ Context documented
- ✓ Impact quantified (2-3 hours daily)
- ⚠ Single user source (N=1)
- ⚠ No market size validation
- **Impact:** +0.05 (reduced due to single source)

**Noise Level: LOW (1.0)**
- Focused, actionable findings
- Clear feature prioritization
- Minimal tangents
- Consistent narrative
- **Impact:** +0.15

**Consistency: HIGH (1.0)**
- No internal contradictions
- Aligns with known Obsidian limitations
- Privacy concerns match industry trends
- Workflow frameworks properly referenced
- **Impact:** +0.15

**Quality Score:** (1.0 + 0.5 + 1.0 + 1.0) / 4 = **0.875**

**Decision:** PROMOTE to `quality-assessed`

**Confidence Update:** 0.55 + 0.55 = **1.0** (capped)

**Next Steps:**
1. Gather corroborating evidence from Obsidian community
2. Validate market demand with additional sources
3. Assess technical feasibility
4. Confirm user segment size and representation

## Quality Improvement Actions

### For Signals Needing Enrichment (Score 0.50-0.69)

**Completeness Gaps:**
- Conduct additional research to fill information gaps
- Interview additional users or stakeholders
- Gather quantitative data to supplement qualitative insights
- Document constraints and context more thoroughly

**Source Trust Issues:**
- Seek corroborating sources
- Verify methodology
- Cross-reference with authoritative sources
- Document source provenance

**Noise Reduction:**
- Filter tangential information
- Focus narrative on core insights
- Separate speculation from facts
- Clarify ambiguous statements

**Consistency Improvements:**
- Resolve internal contradictions
- Verify alignment with known facts
- Clarify cause-effect relationships
- Document assumptions and limitations

### For Signals Requiring Rejection (Score < 0.50)

**Low Source Trust:**
- Signal may be unreliable or biased
- **Action:** Reject or downgrade until better source found

**Critical Incompleteness:**
- Insufficient information for actionability
- **Action:** Return to detection phase for additional data gathering

**High Noise:**
- Core signal obscured by irrelevant information
- **Action:** Attempt filtering; if unsuccessful, reject

**Severe Inconsistency:**
- Conflicts with established facts or internal logic flawed
- **Action:** Investigate contradictions; reject if unresolvable

## Related Documents

- [Signals Directory README](README.md) - Signal directory overview
- [Signals Index](INDEX.md) - Signal navigation
- [Signal Lifecycle Process](../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md) - Governing lifecycle process
- [Work Standard](../../../../../enterprise/chl-standards/standards/WORK_STANDARD.md) - Meta-framework and confidence thresholds
