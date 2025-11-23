---
title: "Signal-01 Market Validation Prompts Index"
description: "Complete guide to market validation prompts for signal-01-knowledge-worker-rag-demand"
doc_type: "index"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "validation"
tags: ["prompts", "validation", "market-research", "signal-validation", "workflow"]
related_docs: ["../../01-research/signals/signal-01-knowledge-worker-rag-demand.md", "README.md", "INDEX.md"]
---

# Signal-01 Market Validation Prompts Index

## Overview

This index provides a complete guide to the market validation prompts created for validating signal-01-knowledge-worker-rag-demand. These prompts enable systematic evidence gathering from multiple independent sources to corroborate or contradict the signal's claims about market demand for RAG-enabled Obsidian plugins.

## Validation Workflow

```
Phase 1: Parallel Evidence Gathering
├── [Forum Validation] ────┐
├── [GitHub Validation] ───┤
├── [Discord Validation] ──┤──> Phase 2: Synthesis
└── [Reddit Validation] ───┘         │
                                     ├──> Confidence Calculation
                                     ├──> Decision Logic
                                     └──> Promote/Hold/Reject
```

**Estimated Total Effort:** 23-28 hours (can be parallelized)

## Prompt Catalog

### 1. Forum Validation Prompt
**File:** [prompt-obsidian-forum-validation.md](./prompt-obsidian-forum-validation.md)

**Target:** Obsidian Community Forums (https://forum.obsidian.md)

**Purpose:** Analyze formal community discussions, feature requests, and pain points

**Key Sections:**
- Feature Requests
- General Discussion
- Help and Support
- Plugins

**Search Terms:**
- AI search, semantic search, RAG
- Search limitations, can't find notes
- Privacy concerns with AI

**Outputs:**
- Evidence summary table (threads, votes, alignment)
- Thematic analysis by cluster
- Quantitative metrics (demand indicators)
- User profile patterns
- Privacy sentiment analysis

**Estimated Effort:** 4-6 hours

**Confidence Impact:** Up to +0.40 if strong evidence

### 2. GitHub Issues Validation Prompt
**File:** [prompt-github-issues-validation.md](./prompt-github-issues-validation.md)

**Target:** Obsidian Releases Repository (https://github.com/obsidianmd/obsidian-releases)

**Purpose:** Analyze feature requests, bug reports, and community voting patterns

**Key Metrics:**
- Issue count with AI/search labels
- Reaction counts (👍 ❤️ 🚀)
- Comment engagement
- Maintainer responses

**Search Queries:**
- repo:obsidianmd/obsidian-releases "AI search"
- repo:obsidianmd/obsidian-releases "semantic search"
- repo:obsidianmd/obsidian-releases "RAG"
- And 20+ additional targeted queries

**Outputs:**
- Issues evidence table with reactions
- Feature request patterns (categorized)
- Timeline analysis (trend over years)
- Implementation status (open/closed/satisfied)
- Technical feasibility insights

**Estimated Effort:** 6-7 hours

**Confidence Impact:** Up to +0.40 if strong evidence

**API Option:** GitHub REST API for automated collection

### 3. Discord Validation Prompt
**File:** [prompt-discord-validation.md](./prompt-discord-validation.md)

**Target:** Obsidian Discord Server (https://discord.gg/obsidianmd)

**Purpose:** Capture real-time organic community sentiment and discussions

**Key Channels:**
- #plugin-ideas
- #feature-requests
- #help (pain points)
- #general
- #development (technical feasibility)

**Focus:** Last 6-12 months for current sentiment

**Outputs:**
- Message evidence table (reactions, threads)
- Thematic analysis (pain points + feature requests)
- Community sentiment summary (HIGH/MED/LOW demand)
- Existing plugin feedback and gaps
- Privacy discussion patterns
- Real-time trend indicators

**Estimated Effort:** 7-8 hours

**Confidence Impact:** Up to +0.35 if strong evidence

**Special Considerations:** Real-time, informal conversations; may show urgent needs not in formal requests

### 4. Reddit Validation Prompt
**File:** [prompt-reddit-validation.md](./prompt-reddit-validation.md)

**Target:** r/ObsidianMD and related subreddits

**Purpose:** Analyze public community discussions with voting mechanisms showing agreement

**Search Strategy:**
- subreddit:ObsidianMD with 15+ targeted keywords
- Time filters: Last 12 months primary, 24 months secondary
- Sort by: Top, New, Comments

**Outputs:**
- Post evidence table (upvotes, comments, alignment)
- Thematic grouping (pain points + features)
- Community consensus analysis (highly upvoted needs)
- Plugin discussion insights (gaps in solutions)
- User profile patterns
- Temporal trend analysis (posts per quarter)
- Privacy sentiment

**Estimated Effort:** 6-7 hours

**Confidence Impact:** Up to +0.35 if strong evidence

**API Option:** Reddit API/PRAW for automated collection

### 5. Validation Synthesis Prompt
**File:** [prompt-validation-synthesis.md](./prompt-validation-synthesis.md)

**Target:** All validation reports combined

**Purpose:** Synthesize evidence, calculate confidence, and make promotion decision

**Inputs Required:**
- Forum validation report
- GitHub validation report
- Discord validation report
- Reddit validation report
- Original signal-01 document

**Analysis Framework:**
1. **Evidence Aggregation** - Collect metrics from all sources
2. **Cross-Source Validation** - Corroboration matrix
3. **Validation Criteria Assessment** - Evaluate 5 success criteria
4. **Confidence Calculation** - Sum impacts from all sources
5. **Contradictory Evidence Analysis** - Resolve conflicts
6. **Validation Decision** - Apply decision logic

**Outputs:**
- Comprehensive synthesis report
- Lifecycle decision record (YAML)
- Signal document updates
- Promotion decision: PROMOTE / HOLD / RETURN / REJECT

**Estimated Effort:** 5 hours

**Decision Criteria:**
- Corroboration: ≥ 3 sources confirming claims
- Market evidence: MODERATE or higher demand
- Technical feasibility: Not INFEASIBLE
- Segment confirmation: At least PARTIAL
- Competitive gap: MODERATE or higher
- Final confidence: ≥ 0.70

## Execution Strategy

### Parallel Execution (Recommended)

**Week 1: Evidence Gathering**
- Run all four validation prompts in parallel
- Different team members or time blocks
- Each produces independent validation report

**Week 2: Synthesis**
- Collect all four reports
- Run synthesis prompt
- Make promotion decision
- Update signal document

**Timeline:** 2 weeks total

### Sequential Execution (Alternative)

**Days 1-2:** Forum validation (4-6 hours)
**Days 3-5:** GitHub validation (6-7 hours)
**Days 6-8:** Discord validation (7-8 hours)
**Days 9-11:** Reddit validation (6-7 hours)
**Days 12-13:** Synthesis (5 hours)

**Timeline:** 2-3 weeks total

## Success Criteria Summary

### Minimum Thresholds (from signal-01)

**Corroboration:**
- Minimum 3 independent sources confirming need
- At least 1 source with DIRECT alignment

**Community Demand:**
- Forum: 5+ threads, 100+ votes
- GitHub: 3+ issues, 100+ reactions
- Discord: 5+ conversations, 10+ users
- Reddit: 5+ posts, 200+ upvotes

**User Segment:**
- 10+ users matching signal-01 profile across all sources

**Privacy Confirmation:**
- 3+ mentions of privacy concerns across sources

**Final Confidence:**
- Must reach ≥ 0.70 after all validation adjustments

### Expected Confidence Impact Range

**Optimistic Scenario:** +0.40 to +0.50
- Strong evidence across all sources
- High corroboration
- Clear market demand
- Segment well-represented

**Moderate Scenario:** +0.20 to +0.40
- Good evidence from 3/4 sources
- Moderate corroboration
- Clear but not overwhelming demand
- Segment partially represented

**Weak Scenario:** -0.10 to +0.20
- Mixed evidence
- Limited corroboration
- Unclear demand
- May not reach 0.70 threshold

## Quality Assurance

### For Each Validation Prompt:
- [ ] All search terms/queries executed
- [ ] Minimum evidence items reviewed (see individual prompts)
- [ ] Evidence tables include verification links
- [ ] Dates and metrics accurate
- [ ] Alignment and quality ratings applied
- [ ] Confidence impact calculated per framework
- [ ] Clear support/contradiction statement
- [ ] Report follows deliverable format

### For Synthesis:
- [ ] All four validation reports reviewed
- [ ] Evidence aggregation table complete
- [ ] Corroboration matrix cross-references sources
- [ ] All five validation criteria assessed
- [ ] Confidence calculation documented step-by-step
- [ ] Decision logic clearly applied
- [ ] Lifecycle decision record created
- [ ] Next steps specified

## Deliverables

### Validation Reports (4 files)
1. `forum-validation-report-YYYY-MM-DD.md`
2. `github-validation-report-YYYY-MM-DD.md`
3. `discord-validation-report-YYYY-MM-DD.md`
4. `reddit-validation-report-YYYY-MM-DD.md`

**Location:** `docs/01-research/signals/validation-evidence/`

### Synthesis Report (1 file)
5. `validation-synthesis-report-YYYY-MM-DD.md`

**Location:** `docs/01-research/signals/validation-evidence/`

### Updated Signal Document
- `signal-01-knowledge-worker-rag-demand.md` (updated in place)
- Lifecycle state updated to `trusted` (if promoted)
- Confidence score updated
- Validation section completed
- Evidence ledger updated

## Tools and Resources

### Search Tools
- **Forum:** Obsidian forum search (https://forum.obsidian.md)
- **GitHub:** GitHub advanced search, GitHub REST API
- **Discord:** Discord search (server-specific), manual channel review
- **Reddit:** Reddit search, Reddit API, PRAW (Python)

### Analysis Tools
- Spreadsheet for evidence aggregation
- Markdown editor for report creation
- YAML validator for decision records

### Reference Documents
- [Signal Lifecycle Process](../../../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md)
- [Signal-01 Document](../../01-research/signals/signal-01-knowledge-worker-rag-demand.md)
- [Quality Assessment Guide](../../01-research/signals/QUALITY_ASSESSMENT_GUIDE.md)

## Next Steps After Validation

### If PROMOTED to Trusted:
1. Update signal-01 lifecycle state and confidence
2. Create persona-01 in `docs/02-personas/`
3. Link persona to trusted signal
4. Begin persona quality evolution process
5. Extract vision seeds from persona

### If HELD in Quality-Assessed:
1. Document gaps requiring additional evidence
2. Plan follow-up research or validation
3. Set timeline for re-evaluation
4. Maintain signal in current state

### If RETURNED to Needs-Review:
1. Document specific issues found
2. Plan research to address gaps
3. May require additional user interviews
4. Re-run validation when ready

### If REJECTED:
1. Document contradictory evidence
2. Archive signal with rejection rationale
3. Consider alternative signals
4. Learn from validation process

## Related Documents

- [Signal-01](../../01-research/signals/signal-01-knowledge-worker-rag-demand.md) - Signal being validated
- [Signal Creation Summary](../../01-research/SIGNAL_CREATION_SUMMARY.md) - Context and roadmap
- [Signals INDEX](../../01-research/signals/INDEX.md) - All signals navigation
- [Prompts README](./README.md) - Prompts directory overview
