---
title: "Prompt: GitHub Issues Market Validation Analysis"
description: "AI agent prompt for analyzing Obsidian GitHub repository issues to validate demand for RAG and AI search features"
doc_type: "agent-prompt"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "validation"
tags: ["prompt", "market-validation", "github", "signal-validation", "feature-requests"]
agent_target: ["validation", "research"]
content_scope: "project-specific"
automation_type: "prompt"
workflow_stage: "validation"
related_docs: ["../../01-research/signals/signal-01-knowledge-worker-rag-demand.md", "../../01-research/signals/README.md"]
signal_reference: "signal-01-knowledge-worker-rag-demand"
validation_dimension: "market-demand"
---

# Prompt: GitHub Issues Market Validation Analysis

## Objective

Analyze the Obsidian GitHub repository issues and feature requests to gather corroborating evidence for signal-01-knowledge-worker-rag-demand. Identify feature requests, bug reports, and discussions related to AI-powered search, RAG capabilities, semantic search, and intelligent knowledge retrieval.

## Target Repository

**Obsidian Releases Repository**: https://github.com/obsidianmd/obsidian-releases

**Note:** The Obsidian team uses this repository for:
- Feature requests
- Bug reports
- Plugin submissions
- Community discussions

## Agent Target

- **Primary:** `agent.signal.validation`
- **Supporting:** `agent.research.market`, `agent.evidence.signal`

## Context Requirements

### Background
Signal-01 proposes strong demand for RAG-enabled Obsidian plugin based on single-user research. Validation requires finding independent GitHub issues/requests expressing similar needs for:
- AI-powered contextual search
- Semantic/intelligent search capabilities
- Knowledge synthesis across vault
- Privacy-preserving AI integration
- Better search beyond "find in files"

### Validation Hypothesis
If signal-01 represents broad demand, we expect GitHub issues showing:
1. Feature requests for AI/semantic search
2. Reports of current search limitations
3. Community upvotes/reactions on AI-related requests
4. Technical discussions about implementation approaches
5. Privacy/security concerns in feature discussions

## Search Parameters

### GitHub Search Queries

**AI and Intelligent Search:**
```
repo:obsidianmd/obsidian-releases "AI search"
repo:obsidianmd/obsidian-releases "semantic search"
repo:obsidianmd/obsidian-releases "intelligent search"
repo:obsidianmd/obsidian-releases "smart search"
repo:obsidianmd/obsidian-releases "contextual search"
repo:obsidianmd/obsidian-releases "RAG"
repo:obsidianmd/obsidian-releases "vector search"
repo:obsidianmd/obsidian-releases "embeddings"
repo:obsidianmd/obsidian-releases "natural language search"
```

**LLM and Chat:**
```
repo:obsidianmd/obsidian-releases "ChatGPT"
repo:obsidianmd/obsidian-releases "GPT"
repo:obsidianmd/obsidian-releases "LLM"
repo:obsidianmd/obsidian-releases "chat with notes"
repo:obsidianmd/obsidian-releases "AI assistant"
repo:obsidianmd/obsidian-releases "ask vault"
```

**Search Limitations:**
```
repo:obsidianmd/obsidian-releases "search" "limitation"
repo:obsidianmd/obsidian-releases "search" "improve"
repo:obsidianmd/obsidian-releases "search" "better"
repo:obsidianmd/obsidian-releases "search results" "too many"
repo:obsidianmd/obsidian-releases "search" "irrelevant"
repo:obsidianmd/obsidian-releases "find notes"
```

**Knowledge Synthesis:**
```
repo:obsidianmd/obsidian-releases "synthesize notes"
repo:obsidianmd/obsidian-releases "connect notes"
repo:obsidianmd/obsidian-releases "related notes"
repo:obsidianmd/obsidian-releases "knowledge graph" "AI"
```

**Privacy:**
```
repo:obsidianmd/obsidian-releases "AI" "privacy"
repo:obsidianmd/obsidian-releases "AI" "local"
repo:obsidianmd/obsidian-releases "AI" "offline"
repo:obsidianmd/obsidian-releases "AI" "secure"
```

### Issue Labels to Check

- `feature-request`
- `plugin-idea`
- `enhancement`
- `search`
- `AI` (if exists)
- `high priority`
- `highly voted`

### Issue States

- **Open Issues:** Current unmet needs
- **Closed Issues:** Check if rejected or implemented
- **Both:** For comprehensive understanding

## Analysis Framework

### For Each Relevant Issue

**Metadata to Capture:**
- Issue number
- Issue title
- URL
- Creation date
- Status (open/closed)
- Number of comments
- Number of reactions (👍 +1, ❤️ heart, 🚀 rocket, etc.)
- Labels applied
- Author (anonymize if needed)

**Content Analysis:**

1. **Feature Request Details**
   - What specific capability is requested?
   - How does user describe the need?
   - What use case is presented?
   - How does it align with signal-01?

2. **Problem Statement**
   - What current limitation is described?
   - How does user quantify impact?
   - What workarounds are mentioned as inadequate?

3. **Community Engagement**
   - How many users commented with support?
   - What is the total reaction count?
   - Are additional use cases mentioned in comments?
   - Any maintainer responses?

4. **Technical Discussion**
   - Are implementation approaches discussed?
   - What technical concerns are raised?
   - Are feasibility questions addressed?
   - Links to existing plugins or solutions?

5. **Privacy and Security**
   - Are privacy concerns mentioned?
   - Is local/offline processing requested?
   - Data security requirements specified?

6. **Status and Resolution**
   - If closed: Why? (implemented, duplicate, won't fix, etc.)
   - If implemented: What plugin/feature satisfied it?
   - If open: How long has it been open?
   - Priority level (if indicated)?

### Classification Schema

**Alignment with Signal-01:**
- **DIRECT:** Explicitly requests RAG/AI search/semantic features
- **HIGH:** Describes same pain points and needs
- **MEDIUM:** Related problem, different emphasis
- **LOW:** Tangentially related
- **NONE:** Not relevant

**Evidence Strength:**
- **STRONG:** Detailed request, high engagement, aligns perfectly
- **MODERATE:** Clear need, some engagement, partial alignment
- **WEAK:** Vague request, low engagement, loose alignment

**Community Priority:**
- **CRITICAL:** 100+ reactions, many comments, long discussion
- **HIGH:** 50-99 reactions, active discussion
- **MEDIUM:** 10-49 reactions, moderate discussion
- **LOW:** <10 reactions, minimal discussion

## Expected Outputs

### 1. Issues Evidence Table

| Issue # | Title | Created | Status | Reactions | Comments | Alignment | Strength | Priority | Key Points |
|---------|-------|---------|--------|-----------|----------|-----------|----------|----------|------------|
| #1234 | [Title] | YYYY-MM-DD | Open/Closed | ## 👍 ## ❤️ | ## | DIRECT/HIGH/MED/LOW | STRONG/MOD/WEAK | CRIT/HIGH/MED/LOW | Brief summary |

### 2. Feature Request Patterns

**Most Requested AI/Search Features:**
1. [Feature name] - ## issues, ### total reactions
2. [Feature name] - ## issues, ### total reactions
3. [Feature name] - ## issues, ### total reactions

**Categorized Requests:**

```markdown
### Category: AI-Powered Search
- **Total Issues:** ##
- **Total Reactions:** ###
- **Date Range:** YYYY-MM-DD to YYYY-MM-DD
- **Top Issues:**
  - #1234: [Title] (### reactions, ## comments)
  - #5678: [Title] (### reactions, ## comments)
- **Common Themes:**
  - [Theme 1]
  - [Theme 2]
- **Signal-01 Alignment:** DIRECT / HIGH / MEDIUM

### Category: Search Limitations
[Same structure]

### Category: Knowledge Synthesis
[Same structure]

### Category: Privacy-Preserving AI
[Same structure]
```

### 3. Timeline Analysis

**Request Frequency Over Time:**
- Issues per year/quarter
- Trend: Increasing / Stable / Decreasing
- Notable spikes (why?)

**Example:**
```markdown
2021: ## AI/search related issues
2022: ## AI/search related issues
2023: ## AI/search related issues
2024: ## AI/search related issues
2025: ## AI/search related issues (partial year)

Trend: INCREASING (suggests growing demand)
```

### 4. Community Sentiment Analysis

**Maintainer Responses:**
- How many issues have official responses?
- What is the general stance? (open to idea, not planned, considering, etc.)
- Any implementation timeline hints?

**Community Consensus:**
- Issues with broad support (50+ reactions)
- Issues with debate/mixed reactions
- Common objections or concerns raised

### 5. Implementation Status

**Already Implemented:**
- Which requests led to core features?
- Which are satisfied by community plugins?
- Which plugins address these needs?

**Still Open:**
- Long-standing open requests (> 1 year)
- Recently opened requests (< 6 months)
- Priority indicators

**Closed Without Implementation:**
- Reasons for closure
- Alternative solutions suggested
- Lessons for signal-01

### 6. Technical Feasibility Insights

**Implementation Discussions:**
- Technical approaches mentioned (RAG, embeddings, vector DBs)
- Plugin API limitations discussed
- Performance concerns raised
- Cross-platform challenges noted

**Existing Plugin Mentions:**
- Smart Connections
- Text Generator
- Copilot
- Other AI-related plugins
- Gaps in current solutions

### 7. Privacy and Security Patterns

**Privacy Requirements:**
- Frequency of privacy mentions: ##
- Local-first vs. cloud preferences
- Data security concerns
- Acceptable trade-offs discussed

## Validation Success Criteria

### Minimum Corroboration Threshold
To support signal-01 validation:
- **Minimum 3 independent issues** with HIGH or DIRECT alignment
- **At least 100 total reactions** across related issues
- **Evidence from multiple years** (not just recent)
- **At least 1 high-priority issue** (50+ reactions)

### Confidence Scoring Impact

**If Found:**
- **5+ direct alignment issues:** +0.15 confidence
- **200+ total reactions on AI/search issues:** +0.10 confidence
- **Increasing trend over time:** +0.05 confidence
- **Privacy concerns in 3+ issues:** +0.05 confidence
- **Active discussions (not stale):** +0.05 confidence

**If NOT Found:**
- **<3 related issues:** -0.10 confidence
- **All issues closed as won't-fix:** -0.10 confidence
- **Low engagement (<50 total reactions):** -0.05 confidence
- **No issues in last 12 months:** -0.05 confidence

## Deliverable Format

### Document Structure

```markdown
# GitHub Issues Market Validation Report

## Executive Summary
- Total issues analyzed: ##
- Direct/high-alignment issues: ##
- Total community reactions: ###
- Demand trend: INCREASING / STABLE / DECREASING
- Validation outcome: SUPPORTS / PARTIAL / CONTRADICTS signal-01
- Confidence impact: +/- ##

## Issues Evidence Summary
[Evidence table of all relevant issues]

## Feature Request Patterns
[Categorized analysis with metrics]

## Timeline Analysis
[Trend analysis and frequency]

## Community Sentiment
[Maintainer responses and consensus]

## Implementation Status
[What's implemented, open, closed]

## Technical Feasibility Insights
[Technical discussions and challenges]

## Privacy and Security Findings
[Privacy requirement patterns]

## Validation Decision
[Clear statement: Do GitHub issues support signal-01?]
[Confidence adjustment recommendation]
[Supporting rationale]

## Appendix: Detailed Issue Summaries
[Full analysis of each relevant issue]
```

### File Naming
Save output as:
`docs/01-research/signals/validation-evidence/github-validation-report-YYYY-MM-DD.md`

## Execution Instructions

### Phase 1: Search and Collect (Estimated: 3-4 hours)
1. Run each GitHub search query
2. Review all results (scan titles first)
3. Open and read relevant issues + comments
4. Capture metadata, reactions, key quotes
5. Tag with alignment, strength, priority
6. Note maintainer responses
7. Track implementation status

### Phase 2: Analyze and Synthesize (Estimated: 2 hours)
1. Categorize issues by theme
2. Calculate quantitative metrics
3. Analyze timeline trends
4. Assess community sentiment
5. Document implementation status
6. Extract technical insights

### Phase 3: Validate and Report (Estimated: 1 hour)
1. Compare findings to signal-01
2. Assess threshold criteria
3. Calculate confidence impact
4. Write validation report
5. Make clear recommendation

**Total Estimated Effort:** 6-7 hours

## Quality Assurance

### Verification Checklist
- [ ] All search queries executed
- [ ] At least 30 issues reviewed total
- [ ] Evidence table includes issue numbers and URLs
- [ ] Reaction counts are accurate
- [ ] Dates verified
- [ ] Maintainer responses noted
- [ ] Implementation status checked for each issue
- [ ] Confidence calculation follows framework
- [ ] Clear validation decision provided

### Bias Mitigation
- Include both open and closed issues
- Note if closed issues were implemented vs. rejected
- Consider recency bias (older issues still valid)
- Distinguish between vocal minority and broad support
- Note if engagement concentrated in specific period

## GitHub API Usage (Optional)

For automated analysis, use GitHub REST API:

```bash
# Get issues with label
GET /repos/obsidianmd/obsidian-releases/issues?labels=feature-request&state=all

# Search issues
GET /search/issues?q=repo:obsidianmd/obsidian-releases+AI+search

# Get issue reactions
GET /repos/obsidianmd/obsidian-releases/issues/{issue_number}/reactions
```

**Rate Limits:** 60 requests/hour unauthenticated, 5000/hour authenticated

## Related Documents

- [Signal-01](../../01-research/signals/signal-01-knowledge-worker-rag-demand.md) - Signal being validated
- [Signal Lifecycle Process](../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md) - Governing process
- [Forum Validation Prompt](./prompt-obsidian-forum-validation.md) - Complementary forum analysis
