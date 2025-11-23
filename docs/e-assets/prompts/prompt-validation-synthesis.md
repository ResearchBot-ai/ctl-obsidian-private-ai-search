---
title: "Prompt: Market Validation Evidence Synthesis"
description: "AI agent prompt for synthesizing all market validation evidence and making final signal promotion decision"
doc_type: "agent-prompt"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "validation"
tags: ["prompt", "synthesis", "validation-decision", "signal-validation", "evidence-synthesis"]
agent_target: ["validation", "lifecycle"]
content_scope: "project-specific"
automation_type: "prompt"
workflow_stage: "validation"
related_docs: ["../../01-research/signals/signal-01-knowledge-worker-rag-demand.md", "../../01-research/signals/README.md"]
signal_reference: "signal-01-knowledge-worker-rag-demand"
validation_dimension: "comprehensive-synthesis"
---

# Prompt: Market Validation Evidence Synthesis

## Objective

Synthesize all gathered market validation evidence from Forum, GitHub, Discord, and Reddit analyses to make a final determination on whether signal-01-knowledge-worker-rag-demand should be promoted to `trusted` state. Calculate updated confidence score and create comprehensive validation decision record.

## Agent Target

- **Primary:** `agent.lifecycle.signal`
- **Supporting:** `agent.signal.validation`, `agent.evidence.signal`

## Context Requirements

### Signal Being Validated
**Signal-01:** Knowledge Worker RAG Demand
- **Current State:** `quality-assessed` (assumed after quality assessment)
- **Current Confidence:** ~1.0 (capped after quality assessment)
- **Required for Trusted:** Confidence ≥ 0.70 + validation evidence

### Input Documents Required

**Validation Reports:**
1. Forum Validation Report: `docs/01-research/signals/validation-evidence/forum-validation-report-YYYY-MM-DD.md`
2. GitHub Validation Report: `docs/01-research/signals/validation-evidence/github-validation-report-YYYY-MM-DD.md`
3. Discord Validation Report: `docs/01-research/signals/validation-evidence/discord-validation-report-YYYY-MM-DD.md`
4. Reddit Validation Report: `docs/01-research/signals/validation-evidence/reddit-validation-report-YYYY-MM-DD.md`

**Source Signal:**
- Signal-01 document: `docs/01-research/signals/signal-01-knowledge-worker-rag-demand.md`

### Validation Success Criteria (from Signal-01)

**Required Evidence:**
1. **Corroboration:** Find 3+ independent sources expressing similar needs
2. **Market Evidence:** Confirm demand in Obsidian community (forum posts, GitHub issues)
3. **Technical Validation:** Verify feasibility of privacy-preserving RAG architecture
4. **Segment Confirmation:** Identify similar user profiles beyond initial research subject
5. **Competitive Confirmation:** Validate gap in current market offerings

**Target Confidence:** ≥ 0.70 for `trusted` state

## Synthesis Framework

### Phase 1: Evidence Aggregation

**For Each Validation Source (Forum, GitHub, Discord, Reddit):**

1. **Extract Key Metrics**
   - Total relevant items found (threads/issues/posts/conversations)
   - Total unique users expressing need
   - Total engagement (upvotes/reactions/comments)
   - Alignment distribution (DIRECT/HIGH/MEDIUM/LOW)
   - Evidence quality (STRONG/MODERATE/WEAK)
   - Confidence impact calculated (+/- score)

2. **Extract Key Themes**
   - Pain points identified
   - Features requested
   - Privacy concerns
   - User profile patterns
   - Existing solution gaps

3. **Extract Timeline Data**
   - Date range of evidence
   - Trend (increasing/stable/decreasing)
   - Recent activity level

### Phase 2: Cross-Source Validation

**Corroboration Analysis:**
- How many independent sources confirm signal-01 claims?
- Are pain points consistently described across sources?
- Are feature needs aligned across platforms?
- Do privacy concerns repeat across sources?

**Triangulation:**
- Do all sources point to same core need?
- Where do sources diverge or conflict?
- How do different platforms' user bases align?

**Example Matrix:**
```markdown
| Finding | Forum | GitHub | Discord | Reddit | Corroborated? |
|---------|-------|--------|---------|--------|---------------|
| Search overload pain point | ✓ (##) | ✓ (##) | ✓ (##) | ✓ (##) | YES (4/4) |
| AI/semantic search request | ✓ (##) | ✓ (##) | ✓ (##) | ✓ (##) | YES (4/4) |
| Privacy concerns | ✓ (##) | ~ (##) | ✓ (##) | ✓ (##) | MOSTLY (3/4) |
| 2-3 hour productivity loss | ✗ | ✗ | ~ | ✗ | NO (0/4) |
```

### Phase 3: Validation Criteria Assessment

**Criterion 1: Corroboration (3+ independent sources)**
- **Required:** ≥ 3 sources confirming core signal claims
- **Found:** [Forum: Y/N, GitHub: Y/N, Discord: Y/N, Reddit: Y/N]
- **Count:** ##/4 sources corroborate
- **Assessment:** MET / NOT MET
- **Confidence Impact:** +/- ##

**Criterion 2: Market Evidence (community demand)**
- **Required:** Clear demand in Obsidian community
- **Forum Evidence:** ## threads, ### votes, [HIGH/MED/LOW demand]
- **GitHub Evidence:** ## issues, ### reactions, [HIGH/MED/LOW demand]
- **Discord Evidence:** ## conversations, ## users, [HIGH/MED/LOW demand]
- **Reddit Evidence:** ## posts, ### upvotes, [HIGH/MED/LOW demand]
- **Overall Assessment:** STRONG / MODERATE / WEAK market demand
- **Confidence Impact:** +/- ##

**Criterion 3: Technical Validation (feasibility)**
- **Required:** Verify RAG architecture feasibility
- **Technical Discussions Found:** ##
- **Implementation Approaches Mentioned:** [List]
- **Existing Plugins with Similar Tech:** [List]
- **Feasibility Blockers Identified:** [List]
- **Assessment:** FEASIBLE / CHALLENGING / INFEASIBLE
- **Confidence Impact:** +/- ##

**Criterion 4: Segment Confirmation (user profiles)**
- **Required:** Similar users beyond N=1 original research
- **Forum User Profiles:** ## matching signal-01 profile
- **GitHub User Profiles:** ## matching signal-01 profile
- **Discord User Profiles:** ## matching signal-01 profile
- **Reddit User Profiles:** ## matching signal-01 profile
- **Total Similar Users:** ###
- **Assessment:** CONFIRMED / PARTIAL / NOT CONFIRMED
- **Confidence Impact:** +/- ##

**Criterion 5: Competitive Confirmation (market gap)**
- **Required:** Validate gap in current offerings
- **Existing Plugins Discussed:** [List]
- **Limitations Identified:** [List]
- **Unmet Needs:** [List]
- **Gap Assessment:** SIGNIFICANT / MODERATE / MINIMAL
- **Confidence Impact:** +/- ##

### Phase 4: Confidence Calculation

**Starting Confidence:** Current signal-01 confidence (post-quality-assessment)

**Aggregated Confidence Adjustments:**
```
Forum Impact:        +/- ##
GitHub Impact:       +/- ##
Discord Impact:      +/- ##
Reddit Impact:       +/- ##
Cross-validation:    +/- ## (bonus for corroboration across sources)
------------------
Total Adjustment:    +/- ##

New Confidence = Starting + Total Adjustment
New Confidence = ## + ## = ##
```

**Bounds Check:**
- Minimum: 0.0
- Maximum: 1.0
- Final Confidence: ##

### Phase 5: Contradictory Evidence Analysis

**Conflicts or Concerns Found:**
- List any evidence contradicting signal-01 claims
- Note skepticism or opposition in community
- Identify barriers or concerns not in original signal
- Assess severity of contradictions

**Resolution:**
- Can contradictions be explained?
- Are they minority views or significant concerns?
- Do they invalidate core signal or just nuance it?
- Impact on validation decision?

### Phase 6: Validation Decision

**Decision Logic:**
```
IF:
  - Corroboration criterion: MET
  - Market Evidence criterion: STRONG or MODERATE
  - Technical Validation criterion: FEASIBLE or CHALLENGING (not INFEASIBLE)
  - Segment Confirmation criterion: CONFIRMED or PARTIAL
  - Competitive Confirmation criterion: SIGNIFICANT or MODERATE
  - Final Confidence: ≥ 0.70
  - No blocking contradictory evidence
THEN:
  Decision = PROMOTE to `trusted`
ELSE:
  Decision = HOLD in `quality-assessed` or RETURN to `needs-review`
```

**Decision Outcome:**
- [ ] PROMOTE to `trusted` - Evidence strongly supports signal
- [ ] CONDITIONAL PROMOTE - Evidence supports with caveats
- [ ] HOLD - Evidence is promising but insufficient
- [ ] RETURN to `needs-review` - Significant gaps or contradictions
- [ ] REJECT - Evidence contradicts signal claims

## Expected Outputs

### 1. Validation Evidence Summary

```markdown
# Market Validation Evidence Synthesis Report
## Signal: signal-01-knowledge-worker-rag-demand

### Executive Summary
- **Validation Sources:** 4 (Forum, GitHub, Discord, Reddit)
- **Total Evidence Items:** ### (threads + issues + conversations + posts)
- **Total Unique Users:** ###
- **Total Engagement:** #### (votes/reactions/comments)
- **Overall Market Demand:** HIGH / MEDIUM / LOW
- **Validation Decision:** PROMOTE / HOLD / RETURN / REJECT
- **Final Confidence:** ##
- **Confidence Change:** +/- ## from ##

### Evidence Aggregation

| Source | Items | Users | Engagement | Alignment | Quality | Impact |
|--------|-------|-------|------------|-----------|---------|--------|
| Forum | ## | ## | ### | HIGH | STRONG | +## |
| GitHub | ## | ## | ### | DIRECT | STRONG | +## |
| Discord | ## | ## | ### | HIGH | MODERATE | +## |
| Reddit | ## | ## | ### | HIGH | MODERATE | +## |
| **Total** | **###** | **###** | **####** | - | - | **+##** |

### Corroboration Matrix
[Cross-source validation table]

### Validation Criteria Assessment
[Each criterion with MET/NOT MET and rationale]

### Confidence Calculation
[Detailed calculation with all adjustments]

### Contradictory Evidence
[Any conflicts found and resolution]

### Validation Decision
**Decision: [PROMOTE / HOLD / RETURN / REJECT]**

**Rationale:**
[3-5 sentences explaining the decision based on evidence]

**Final Confidence: ##**

**Next Steps:**
[What happens next based on decision]
```

### 2. Lifecycle Decision Record

```yaml
lifecycle_events:
  - signal_id: "signal-01-knowledge-worker-rag-demand"
    from_state: "quality-assessed"
    to_state: "trusted"  # or "needs-review" if not promoted
    decided_at: "2025-11-23T16:00:00Z"
    proposed_by: "agent.signal.validation"
    decision_maker: "agent.lifecycle.signal"
    validation_summary:
      sources_analyzed: 4
      total_evidence_items: ###
      total_unique_users: ###
      total_engagement: ####
      corroboration_level: "STRONG"  # or MODERATE, WEAK
      market_demand: "HIGH"  # or MEDIUM, LOW
      technical_feasibility: "FEASIBLE"  # or CHALLENGING, INFEASIBLE
      segment_confirmation: "CONFIRMED"  # or PARTIAL, NOT CONFIRMED
      competitive_gap: "SIGNIFICANT"  # or MODERATE, MINIMAL
    validation_criteria:
      corroboration: "MET"
      market_evidence: "MET"
      technical_validation: "MET"
      segment_confirmation: "MET"
      competitive_confirmation: "MET"
    confidence_evolution:
      before_validation: ##
      forum_impact: +##
      github_impact: +##
      discord_impact: +##
      reddit_impact: +##
      cross_validation_bonus: +##
      after_validation: ##
    contradictory_evidence:
      found: true/false
      severity: "NONE" / "MINOR" / "MODERATE" / "MAJOR"
      resolution: "Explained / Noted / Blocking"
    decision_rationale: |
      [Multi-line rationale for the decision]
    next_steps:
      - "Update signal document with new confidence"
      - "Link validation reports to signal"
      - "Update INDEX.md with new state"
      - "Begin persona development" (if promoted)
```

### 3. Signal Document Updates

**Updates to signal-01-knowledge-worker-rag-demand.md:**

```yaml
# In frontmatter:
lifecycle_state: "trusted"  # Updated from quality-assessed
confidence: ##  # Updated with new calculated value

# In validation section:
validation:
  status: "completed"
  validated_at: "2025-11-23T16:00:00Z"
  validation_sources:
    - "Forum: forum-validation-report-2025-11-23.md"
    - "GitHub: github-validation-report-2025-11-23.md"
    - "Discord: discord-validation-report-2025-11-23.md"
    - "Reddit: reddit-validation-report-2025-11-23.md"
  corroboration_achieved: true
  market_demand_confirmed: true
  segment_confirmed: true

# In evidence ledger:
| 2025-11-23 | Validation completed | ## | 4 sources (Forum, GitHub, Discord, Reddit) | Promoted to trusted based on strong corroboration across all validation sources |
```

## Execution Instructions

### Phase 1: Gather and Review (Estimated: 1 hour)
1. Collect all four validation reports
2. Read each report thoroughly
3. Note key findings from each
4. Identify any missing information

### Phase 2: Synthesize Evidence (Estimated: 2 hours)
1. Create evidence aggregation table
2. Build corroboration matrix
3. Assess each validation criterion
4. Document any contradictory evidence
5. Note cross-source patterns

### Phase 3: Calculate and Decide (Estimated: 1 hour)
1. Calculate confidence adjustments from each source
2. Sum total confidence impact
3. Apply bounds and calculate final confidence
4. Evaluate decision logic
5. Make promotion decision

### Phase 4: Document Decision (Estimated: 1 hour)
1. Write comprehensive synthesis report
2. Create lifecycle decision record
3. Update signal-01 document
4. Update INDEX.md
5. Prepare next-step recommendations

**Total Estimated Effort:** 5 hours

## Quality Assurance

### Verification Checklist
- [ ] All four validation reports reviewed
- [ ] Evidence aggregation table complete
- [ ] Corroboration matrix shows cross-source analysis
- [ ] All five validation criteria assessed
- [ ] Confidence calculation documented step-by-step
- [ ] Contradictory evidence addressed
- [ ] Decision logic clearly applied
- [ ] Lifecycle decision record created
- [ ] Signal document updates specified
- [ ] Next steps documented

### Decision Quality Gates

**Before PROMOTE decision:**
- [ ] At least 3/4 sources corroborate core claims
- [ ] Market demand is MODERATE or higher across sources
- [ ] Technical feasibility is not INFEASIBLE
- [ ] Segment confirmation is at least PARTIAL
- [ ] Final confidence is ≥ 0.70
- [ ] Any contradictory evidence is resolved or minor

**Before REJECT decision:**
- [ ] Clear contradictory evidence from multiple sources
- [ ] Core signal claims unsubstantiated
- [ ] Confidence calculation shows net negative impact
- [ ] Decision rationale documents why rejection is appropriate

## File Naming

Save synthesis report as:
`docs/01-research/signals/validation-evidence/validation-synthesis-report-YYYY-MM-DD.md`

## Related Documents

- [Signal-01](../../01-research/signals/signal-01-knowledge-worker-rag-demand.md) - Signal being validated
- [Signal Lifecycle Process](../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md) - Governing lifecycle
- [Forum Validation Prompt](./prompt-obsidian-forum-validation.md)
- [GitHub Validation Prompt](./prompt-github-issues-validation.md)
- [Discord Validation Prompt](./prompt-discord-validation.md)
- [Reddit Validation Prompt](./prompt-reddit-validation.md)
