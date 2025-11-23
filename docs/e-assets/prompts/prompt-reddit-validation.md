---
title: "Prompt: Reddit r/ObsidianMD Market Validation Analysis"
description: "AI agent prompt for analyzing Reddit r/ObsidianMD community to validate demand for RAG and AI search features"
doc_type: "agent-prompt"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "validation"
tags: ["prompt", "market-validation", "reddit", "signal-validation", "community-analysis"]
agent_target: ["validation", "research"]
content_scope: "project-specific"
automation_type: "prompt"
workflow_stage: "validation"
related_docs: ["../../01-research/signals/signal-01-knowledge-worker-rag-demand.md", "../../01-research/signals/README.md"]
signal_reference: "signal-01-knowledge-worker-rag-demand"
validation_dimension: "market-demand"
---

# Prompt: Reddit r/ObsidianMD Market Validation Analysis

## Objective

Analyze the r/ObsidianMD subreddit to gather public community evidence validating signal-01-knowledge-worker-rag-demand. Capture user discussions, pain points, feature requests, and community sentiment regarding AI-powered search, RAG capabilities, and knowledge management challenges.

## Target Platform

**Subreddit:** r/ObsidianMD (https://reddit.com/r/ObsidianMD)

**Related Subreddits (Secondary):**
- r/PKMS (Personal Knowledge Management Systems)
- r/Zettelkasten
- r/productivity (Obsidian-specific posts)

## Agent Target

- **Primary:** `agent.signal.validation`
- **Supporting:** `agent.research.market`, `agent.evidence.signal`, `agent.community.sentiment`

## Context Requirements

### Background
Reddit provides public community discussions with voting mechanisms that indicate community agreement/interest. r/ObsidianMD hosts diverse users from beginners to power users, offering broad market validation perspective.

### Validation Hypothesis
Reddit posts should reveal:
1. User pain points with current search functionality
2. Feature requests for AI/semantic search capabilities
3. Community upvoting of related needs
4. Discussions of existing plugin limitations
5. Privacy concerns in AI integration discussions
6. Workflow challenges requiring better search/synthesis

## Search Strategy

### Reddit Search Queries

**Direct Search on r/ObsidianMD:**
```
subreddit:ObsidianMD AI search
subreddit:ObsidianMD semantic search
subreddit:ObsidianMD RAG
subreddit:ObsidianMD ChatGPT
subreddit:ObsidianMD LLM
subreddit:ObsidianMD "smart search"
subreddit:ObsidianMD "intelligent search"
subreddit:ObsidianMD "contextual search"
subreddit:ObsidianMD "search limitation"
subreddit:ObsidianMD "search not working"
subreddit:ObsidianMD "can't find notes"
subreddit:ObsidianMD "AI plugin"
subreddit:ObsidianMD "chat with vault"
subreddit:ObsidianMD "ask my notes"
```

**Knowledge Management Focus:**
```
subreddit:ObsidianMD "knowledge synthesis"
subreddit:ObsidianMD "connect notes"
subreddit:ObsidianMD "related notes"
subreddit:ObsidianMD "find connections"
subreddit:ObsidianMD "knowledge graph" AI
```

**Privacy Focus:**
```
subreddit:ObsidianMD AI privacy
subreddit:ObsidianMD "local AI"
subreddit:ObsidianMD "offline AI"
subreddit:ObsidianMD "private AI"
```

### Time Filters
- **Primary:** Last 12 months (recent sentiment)
- **Secondary:** Last 24 months (trend analysis)
- **Comparison:** All time (historical context)

### Sorting Options
- **Top:** Most upvoted (community agreement)
- **New:** Recent discussions
- **Comments:** Most discussed topics

## Analysis Framework

### For Each Relevant Post

**Metadata to Capture:**
- Post title
- URL (reddit.com/r/ObsidianMD/comments/...)
- Post date
- Author (anonymize or note as "[deleted]")
- Upvote count
- Upvote ratio (% upvoted)
- Number of comments
- Post flair (if any)
- Awards received

**Content Analysis:**

1. **Post Type**
   - Question/Help Request
   - Feature Request
   - Discussion/Opinion
   - Plugin Review/Comparison
   - Workflow Sharing
   - Problem Report

2. **Problem/Need Identification**
   - What pain point is described?
   - How severe (based on language used)?
   - Quantified impact mentioned?
   - Workflow context provided?

3. **Solution Seeking**
   - What has user tried?
   - What plugins mentioned?
   - What workarounds described?
   - What gaps remain?

4. **Community Engagement**
   - Upvote count (agreement indicator)
   - Comment quality and depth
   - Similar experiences shared?
   - Solutions offered by community?
   - Debate or consensus?

5. **Signal-01 Alignment**
   - Matches pain points?
   - Matches feature needs?
   - Matches user profile?
   - Matches privacy concerns?
   - Matches workflow challenges?

### Comment Analysis

**For High-Value Posts:**
- Review top 5-10 comments
- Note additional use cases mentioned
- Identify counter-arguments or concerns
- Document community-suggested solutions
- Track evolution of discussion

### Classification Schema

**Alignment with Signal-01:**
- **DIRECT:** Explicitly requests RAG/AI search features
- **HIGH:** Describes same problems and needs
- **MEDIUM:** Related problem, different angle
- **LOW:** Tangentially related
- **CONTRADICTORY:** Argues against need

**Evidence Quality:**
- **STRONG:** Detailed post, high upvotes, active discussion
- **MODERATE:** Clear need, some engagement
- **WEAK:** Brief mention, low engagement

**Community Support:**
- **STRONG:** 100+ upvotes, 50+ comments
- **MODERATE:** 20-99 upvotes, 10-49 comments
- **LOW:** <20 upvotes, <10 comments

## Expected Outputs

### 1. Post Evidence Table

| Title | Date | Upvotes | Comments | Alignment | Quality | Support | Summary |
|-------|------|---------|----------|-----------|---------|---------|---------|
| [Title] | YYYY-MM-DD | ### | ## | DIRECT/HIGH/MED/LOW | STRONG/MOD/WEAK | STRONG/MOD/LOW | Brief summary |

### 2. Thematic Grouping

**Pain Point Themes:**
```markdown
### Theme: Current Search Inadequacy
- **Total Posts:** ##
- **Total Upvotes:** ###
- **Date Range:** YYYY-MM-DD to YYYY-MM-DD
- **Top Posts:**
  - "[Post Title]" - ### upvotes, ## comments
  - "[Post Title]" - ### upvotes, ## comments
- **Common Complaints:**
  - "Find in files" not sufficient
  - Too many irrelevant results
  - Cannot synthesize across notes
- **Signal-01 Alignment:** HIGH
```

**Feature Request Themes:**
```markdown
### Theme: AI-Powered Search Request
- **Total Posts:** ##
- **Total Upvotes:** ###
- **Specific Features Requested:**
  - Natural language search
  - Semantic understanding
  - Related note discovery
  - Context-aware retrieval
- **Use Cases Described:**
  - [Use case 1]
  - [Use case 2]
- **Signal-01 Alignment:** DIRECT
```

### 3. Community Consensus Analysis

**Highly Upvoted Needs (100+ upvotes):**
- [Post title and summary] - ### upvotes
- Alignment with signal-01: [HIGH/MEDIUM/LOW]

**Controversial or Debated Topics:**
- [Topic]
- Upvote ratio: ##%
- Main arguments for/against
- Relevance to signal-01

### 4. Plugin Discussion Insights

**Existing AI Plugins Mentioned:**

**Smart Connections:**
- Posts mentioning: ##
- Positive feedback: ##
- Limitations noted: ##
- Unmet needs: [List]

**Other Plugins:**
- [Same structure for Copilot, Text Generator, etc.]

**Gap Analysis:**
- Features requested but not available
- Common limitations across plugins
- Privacy/security concerns not addressed

### 5. User Profile Patterns

**Observable User Types:**
- Students/academics: ## posts
- Professionals/knowledge workers: ## posts
- Developers/technical users: ## posts
- Personal knowledge management: ## posts

**Workflow Complexity:**
- Large vault users (>1000 notes): ## mentions
- Complex workflows: ## mentions
- Cross-device users: ## mentions
- Privacy-focused users: ## mentions

**Alignment with Signal-01 Profile:**
- Advanced knowledge workers: ##
- High-volume workflows: ##
- Privacy concerns: ##
- Technical sophistication: ##

### 6. Temporal Trend Analysis

**Posts Per Quarter:**
- Q1 2024: ##
- Q2 2024: ##
- Q3 2024: ##
- Q4 2024: ##
- Q1 2025: ## (partial)

**Trend:** Increasing / Stable / Decreasing

**Notable Spikes:**
- [Date]: ## posts (trigger: [event/plugin release/etc.])

### 7. Privacy and Security Sentiment

**Privacy Concerns:**
- Posts mentioning privacy: ##
- Types of concerns: [List]
- Local-first preferences: ##
- Cloud skepticism: ##

**Acceptable Solutions:**
- Local AI processing: ##
- Open source preferred: ##
- Transparent data handling: ##

## Validation Success Criteria

### Minimum Corroboration Threshold
To support signal-01:
- **Minimum 5 posts** with HIGH or DIRECT alignment
- **At least 200 total upvotes** across related posts
- **Evidence across multiple months** (not one-time spike)
- **At least 1 high-support post** (100+ upvotes)

### Confidence Scoring Impact

**If Found:**
- **10+ aligned posts:** +0.10 confidence
- **500+ total upvotes on related posts:** +0.10 confidence
- **Increasing trend over time:** +0.05 confidence
- **Privacy concerns in 5+ posts:** +0.05 confidence
- **Active recent discussions (<3 months):** +0.05 confidence

**If NOT Found:**
- **<5 related posts:** -0.10 confidence
- **Low engagement (<100 total upvotes):** -0.05 confidence
- **Decreasing trend:** -0.05 confidence
- **Community skepticism/opposition:** -0.10 confidence

## Deliverable Format

```markdown
# Reddit r/ObsidianMD Market Validation Report

## Executive Summary
- Total posts analyzed: ##
- Relevant posts: ##
- Total upvotes on related posts: ###
- Total comments: ##
- Community demand: HIGH / MEDIUM / LOW
- Validation outcome: SUPPORTS / PARTIAL / CONTRADICTS signal-01
- Confidence impact: +/- ##

## Post Evidence Summary
[Evidence table]

## Thematic Analysis
[Pain points and feature requests]

## Community Consensus
[Highly upvoted posts and debates]

## Plugin Discussion Insights
[Existing solutions and gaps]

## User Profile Patterns
[Demographics and workflows]

## Temporal Trends
[Activity over time]

## Privacy and Security
[Privacy concern patterns]

## Validation Decision
[Clear support/contradiction statement]
[Confidence adjustment]
[Rationale]

## Appendix: Notable Posts
[Detailed summaries]
```

### File Naming
Save as: `docs/01-research/signals/validation-evidence/reddit-validation-report-YYYY-MM-DD.md`

## Execution Instructions

### Phase 1: Search and Collect (Estimated: 3-4 hours)
1. Execute all search queries on r/ObsidianMD
2. Sort by Top, New, and Comments for each
3. Review results (scan titles, check post scores)
4. Read relevant posts completely + top comments
5. Capture metadata and key quotes
6. Tag with alignment, quality, support levels
7. Check related subreddits for crossover posts

### Phase 2: Analyze Patterns (Estimated: 2 hours)
1. Group posts by theme
2. Calculate quantitative metrics
3. Assess temporal trends
4. Analyze user profiles
5. Document plugin discussion insights
6. Synthesize privacy sentiment

### Phase 3: Report and Validate (Estimated: 1 hour)
1. Compare to signal-01 claims
2. Assess validation criteria
3. Calculate confidence impact
4. Write report
5. Make recommendation

**Total Estimated Effort:** 6-7 hours

## Quality Assurance

### Verification Checklist
- [ ] All search queries executed
- [ ] Multiple sort orders checked
- [ ] At least 25 posts reviewed
- [ ] Evidence table includes URLs
- [ ] Upvote counts and dates accurate
- [ ] User anonymization applied
- [ ] Comments reviewed for top posts
- [ ] Trend analysis spans multiple quarters
- [ ] Clear validation decision provided

### Bias Mitigation
- Include both high and low upvoted posts
- Note if evidence comes from vocal minority
- Consider Reddit demographic skew (may be more technical users)
- Distinguish between latest trend and sustained need
- Account for plugin release timing affecting discussions

## Reddit API Usage (Optional)

For automated collection, use Reddit API or PRAW (Python Reddit API Wrapper):

```python
import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_SECRET",
    user_agent="signal-validation-bot"
)

subreddit = reddit.subreddit("ObsidianMD")

# Search posts
for post in subreddit.search("AI search", time_filter="year", limit=100):
    # Process post
    print(post.title, post.score, post.num_comments)
```

## Related Documents

- [Signal-01](../../01-research/signals/signal-01-knowledge-worker-rag-demand.md)
- [Forum Validation Prompt](./prompt-obsidian-forum-validation.md)
- [GitHub Validation Prompt](./prompt-github-issues-validation.md)
- [Discord Validation Prompt](./prompt-discord-validation.md)
