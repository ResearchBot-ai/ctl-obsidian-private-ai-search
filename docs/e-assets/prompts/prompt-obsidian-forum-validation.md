---
title: "Prompt: Obsidian Forum Market Validation Analysis"
description: "AI agent prompt for analyzing Obsidian community forums to validate demand for RAG-enabled AI search features"
doc_type: "agent-prompt"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "validation"
tags: ["prompt", "market-validation", "obsidian-forum", "signal-validation", "community-analysis"]
agent_target: ["validation", "research"]
content_scope: "project-specific"
automation_type: "prompt"
workflow_stage: "validation"
related_docs: ["../../01-research/signals/signal-01-knowledge-worker-rag-demand.md", "../../01-research/signals/README.md"]
signal_reference: "signal-01-knowledge-worker-rag-demand"
validation_dimension: "market-demand"
---

# Prompt: Obsidian Forum Market Validation Analysis

## Objective

Analyze the Obsidian community forums to gather corroborating evidence for signal-01-knowledge-worker-rag-demand. Specifically, identify discussions, feature requests, and user pain points related to AI-powered search, RAG capabilities, semantic search, and contextual knowledge retrieval in Obsidian.

## Target Platform

**Obsidian Community Forum**: https://forum.obsidian.md

## Agent Target

- **Primary:** `agent.signal.validation`
- **Supporting:** `agent.research.market`, `agent.evidence.signal`

## Context Requirements

### Background
Signal-01 proposes strong user demand for a RAG-enabled Obsidian plugin based on single-user research (N=1). This research identified:
- 2-3 hours daily productivity loss from inefficient knowledge navigation
- Current search is basic "find in files" leading to information overload
- Need for contextual AI search across full knowledge base
- Privacy-first architecture requirements
- Cross-device synchronization needs

### Validation Hypothesis
If signal-01 accurately represents broader market demand, we expect to find:
1. Multiple independent forum posts expressing similar pain points
2. Feature requests for AI/semantic/contextual search capabilities
3. Discussions about current search limitations
4. Interest in RAG or similar AI-powered knowledge retrieval
5. Privacy concerns related to AI plugins
6. Cross-device workflow challenges

## Search Parameters

### Primary Search Terms

**AI and Search Related:**
- "AI search"
- "semantic search"
- "contextual search"
- "intelligent search"
- "smart search"
- "RAG" (Retrieval-Augmented Generation)
- "vector search"
- "embeddings"
- "natural language search"

**Problem and Pain Points:**
- "search limitations"
- "search not working"
- "too many results"
- "can't find notes"
- "search overwhelming"
- "knowledge synthesis"
- "connect notes"
- "find related"

**Feature Requests:**
- "AI plugin"
- "ChatGPT integration"
- "LLM plugin"
- "AI assistant"
- "chat with notes"
- "ask my vault"
- "query knowledge base"

**Privacy Related:**
- "local AI"
- "privacy AI"
- "offline AI"
- "private AI"
- "data privacy"
- "secure AI"

### Forum Sections to Search

**High Priority:**
- Feature Requests
- Plugin Ideas
- General Discussion
- Help and Support (for pain points)

**Medium Priority:**
- Plugins (for existing solutions discussion)
- Mobile (for cross-device concerns)
- API (for technical feasibility discussions)

## Analysis Framework

### For Each Relevant Thread/Post

**Metadata to Capture:**
- Thread title
- URL
- Post date
- Number of replies
- Number of likes/votes
- Author (anonymize if needed)
- Forum section

**Content Analysis:**
1. **Pain Point Identification**
   - What specific problem is described?
   - How does the user quantify impact (time, frustration, productivity)?
   - What workarounds are mentioned?

2. **Feature Request Details**
   - What specific capabilities are requested?
   - How does it align with signal-01 features?
   - What use cases are described?

3. **Privacy and Security Concerns**
   - Are privacy requirements mentioned?
   - Is local/offline processing requested?
   - Are data security concerns raised?

4. **Technical Sophistication**
   - What is the user's technical level?
   - Are specific technologies mentioned (RAG, embeddings, LLMs)?
   - What integration points are discussed?

5. **Workflow Context**
   - How does the user describe their workflow?
   - What knowledge management frameworks are mentioned?
   - What volume/scale challenges are described?

6. **Community Response**
   - How many users engaged with the thread?
   - What is the sentiment (positive, negative, neutral)?
   - Are similar needs expressed by others?

### Categorization Schema

**Alignment with Signal-01:**
- **HIGH:** Directly describes same pain points and feature needs
- **MEDIUM:** Related problem/need but different emphasis
- **LOW:** Tangentially related
- **NONE:** Not relevant to signal validation

**Evidence Quality:**
- **STRONG:** Specific, detailed, quantified impact
- **MODERATE:** Clear problem statement, some detail
- **WEAK:** Vague or general mention

## Expected Outputs

### 1. Evidence Summary Table

| Thread Title | URL | Date | Votes | Alignment | Quality | Key Quote | Notes |
|--------------|-----|------|-------|-----------|---------|-----------|-------|
| [Title] | [URL] | YYYY-MM-DD | ## | HIGH/MED/LOW | STRONG/MOD/WEAK | "Direct quote" | Brief notes |

### 2. Thematic Analysis

**Theme Clusters:**
- Group similar pain points and requests
- Identify frequency of each theme
- Note variations in how needs are expressed
- Document common use cases

**Example Structure:**
```markdown
### Theme: Search Overload and Irrelevance
- **Frequency:** ## mentions across ## threads
- **Key Pain Points:**
  - Too many irrelevant results
  - Cannot synthesize across notes
  - Basic "find in files" insufficient
- **Representative Quotes:**
  - "[Quote from thread]" - [URL]
- **Signal-01 Alignment:** HIGH
```

### 3. Quantitative Metrics

**Community Demand Indicators:**
- Total threads discussing AI/semantic/contextual search: ##
- Total unique users expressing similar needs: ##
- Total votes/likes on related threads: ##
- Date range of discussions: YYYY-MM-DD to YYYY-MM-DD
- Trend: Increasing / Stable / Decreasing

**Feature Request Patterns:**
- Most requested features (ranked by frequency)
- Most voted feature requests
- Most discussed threads

### 4. User Profile Patterns

**Demographics (if discernible):**
- Technical sophistication levels
- Knowledge management approaches mentioned
- Vault sizes/complexity described
- Use cases (academic, professional, personal)

**Alignment with Signal-01 User Profile:**
- Number of users matching "advanced knowledge worker" profile: ##
- Number mentioning privacy concerns: ##
- Number describing high-volume workflows: ##

### 5. Competitive Context

**Existing Solutions Mentioned:**
- What plugins or tools are users currently trying?
- What are reported limitations of existing solutions?
- What gaps remain unfilled?

### 6. Technical Feasibility Insights

**Community Technical Discussions:**
- Mentions of technical approaches (RAG, embeddings, etc.)
- Discussion of implementation challenges
- References to successful implementations elsewhere

### 7. Privacy and Security Sentiment

**Privacy Concerns:**
- Frequency of privacy mentions: ##
- Types of privacy concerns raised
- Acceptable vs. unacceptable trade-offs discussed
- Local-first vs. cloud preferences

## Validation Success Criteria

### Minimum Corroboration Threshold
To support signal-01 validation:
- **Minimum 3 independent sources** expressing similar pain points
- **At least 1 highly aligned thread** (HIGH alignment + STRONG quality)
- **Evidence of ongoing demand** (discussions within last 6 months)

### Confidence Scoring Impact

**If Found:**
- **5+ high-alignment threads:** +0.15 confidence
- **10+ medium-alignment threads:** +0.10 confidence
- **100+ total community votes on related threads:** +0.05 confidence
- **Privacy concerns mentioned by 3+ users:** +0.05 confidence
- **Technical discussions showing feasibility:** +0.05 confidence

**If NOT Found:**
- **<3 related threads:** -0.10 confidence (signal may be outlier)
- **No discussions in last 12 months:** -0.05 confidence (timing concern)
- **Strong contradictory evidence:** -0.15 confidence

## Deliverable Format

### Document Structure

```markdown
# Obsidian Forum Market Validation Report

## Executive Summary
- Total threads analyzed: ##
- High-alignment evidence found: ## threads
- Community demand assessment: HIGH / MEDIUM / LOW
- Validation outcome: SUPPORTS / PARTIAL / CONTRADICTS signal-01
- Confidence impact: +/- ##

## Evidence Summary
[Summary table of all relevant threads]

## Thematic Analysis
[Detailed theme clusters with examples]

## Quantitative Metrics
[All numerical indicators]

## User Profile Analysis
[Demographics and alignment with signal-01 profile]

## Privacy and Security Findings
[Privacy concern analysis]

## Competitive Context
[Existing solutions and gaps]

## Validation Decision
[Clear statement: Does forum evidence support signal-01?]
[Confidence adjustment recommendation]
[Supporting rationale]

## Appendix: Full Thread Summaries
[Detailed notes on each relevant thread]
```

### File Naming
Save output as:
`docs/01-research/signals/validation-evidence/forum-validation-report-YYYY-MM-DD.md`

## Execution Instructions

### Phase 1: Search and Collect (Estimated: 2-3 hours)
1. Access Obsidian forum: https://forum.obsidian.md
2. Use forum search with each primary search term
3. Review results for relevance (scan titles first)
4. Open and read relevant threads completely
5. Capture metadata and quotes in evidence table
6. Tag each with alignment and quality ratings

### Phase 2: Analyze and Synthesize (Estimated: 1-2 hours)
1. Group evidence by themes
2. Calculate quantitative metrics
3. Identify user profile patterns
4. Assess privacy sentiment
5. Document competitive context

### Phase 3: Validate and Report (Estimated: 1 hour)
1. Compare findings to signal-01 claims
2. Assess whether minimum thresholds met
3. Calculate confidence impact
4. Write validation report
5. Make clear recommendation

**Total Estimated Effort:** 4-6 hours

## Quality Assurance

### Verification Checklist
- [ ] All forum sections searched with primary terms
- [ ] At least 20 threads reviewed (even if not all relevant)
- [ ] Evidence table includes URLs for verification
- [ ] Quotes are verbatim with proper attribution
- [ ] Dates and metrics are accurate
- [ ] Confidence impact calculation follows framework
- [ ] Clear validation decision provided
- [ ] Report follows deliverable format

### Bias Mitigation
- Search both positive and negative sentiment terms
- Include contradictory evidence if found
- Distinguish between majority and vocal minority
- Note if evidence is concentrated in specific time period
- Consider whether active forum users represent broader user base

## Related Documents

- [Signal-01](../../01-research/signals/signal-01-knowledge-worker-rag-demand.md) - Signal being validated
- [Signal Lifecycle Process](../../../../../enterprise/chl-standards/processes/PROCESS-signal-01-signal-lifecycle.md) - Governing process
- [Quality Assessment Guide](../../01-research/signals/QUALITY_ASSESSMENT_GUIDE.md) - Quality framework
