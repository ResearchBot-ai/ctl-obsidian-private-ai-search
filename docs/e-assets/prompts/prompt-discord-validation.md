---
title: "Prompt: Obsidian Discord Market Validation Analysis"
description: "AI agent prompt for analyzing Obsidian Discord community to validate demand for RAG and AI search features"
doc_type: "agent-prompt"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "validation"
tags: ["prompt", "market-validation", "discord", "signal-validation", "community-analysis"]
agent_target: ["validation", "research"]
content_scope: "project-specific"
automation_type: "prompt"
workflow_stage: "validation"
related_docs: ["../../01-research/signals/signal-01-knowledge-worker-rag-demand.md", "../../01-research/signals/README.md"]
signal_reference: "signal-01-knowledge-worker-rag-demand"
validation_dimension: "market-demand"
---

# Prompt: Obsidian Discord Market Validation Analysis

## Objective

Analyze the Obsidian Discord community channels to gather real-time, conversational evidence validating signal-01-knowledge-worker-rag-demand. Capture organic discussions, feature requests, pain points, and community sentiment regarding AI-powered search, RAG capabilities, and intelligent knowledge retrieval.

## Target Platform

**Obsidian Discord Server**: https://discord.gg/obsidianmd

**Key Channels to Monitor:**
- #plugin-ideas
- #feature-requests
- #plugins-general
- #help (for pain points)
- #general
- #development (for technical feasibility discussions)
- #mobile (for cross-device concerns)

## Agent Target

- **Primary:** `agent.signal.validation`
- **Supporting:** `agent.research.market`, `agent.evidence.signal`, `agent.community.sentiment`

## Context Requirements

### Background
Signal-01 claims strong demand for RAG-enabled AI search in Obsidian. Discord provides real-time community sentiment and informal feature discussions that may not appear in formal forum posts or GitHub issues.

### Validation Hypothesis
Discord conversations should reveal:
1. Organic pain point discussions about search limitations
2. User suggestions for AI/semantic search features
3. Community reactions to existing AI plugins
4. Privacy concerns in AI feature discussions
5. Real-time feedback on workarounds and limitations

## Search and Monitoring Strategy

### Search Keywords

**Primary Terms:**
- AI
- search
- RAG
- semantic
- GPT
- ChatGPT
- LLM
- intelligent
- smart search
- find notes
- contextual

**Pain Point Terms:**
- search limitation
- can't find
- too many results
- search broken
- search not working
- search improvement

**Feature Ideas:**
- AI plugin
- AI integration
- chat with vault
- ask my notes
- AI assistant

### Time Frame
**Primary Focus:** Last 6 months (recent/current sentiment)
**Secondary:** Last 12 months (trend analysis)

### Message Collection Strategy

1. **Discord Search** (if available)
   - Use Discord's search function with keywords
   - Search within specific channels
   - Filter by date ranges

2. **Manual Channel Review** (if search limited)
   - Scan recent messages in key channels (last 30 days)
   - Look for keyword mentions
   - Follow conversation threads

3. **Pin and Important Message Review**
   - Check pinned messages in each channel
   - Review channel announcements
   - Note community guidelines or common requests

## Analysis Framework

### For Each Relevant Conversation/Message

**Metadata to Capture:**
- Channel name
- Date and time
- User (anonymize)
- Message ID (for reference)
- Emoji reactions (👍 ❤️ 🚀 etc.)
- Thread replies count

**Content Analysis:**

1. **Pain Point Expression**
   - What problem is user describing?
   - How acute is the need (urgency indicators)?
   - What have they tried?
   - Frustration level?

2. **Feature Suggestion**
   - What specific feature is requested?
   - How detailed is the suggestion?
   - Alignment with signal-01 features?
   - User's use case?

3. **Community Response**
   - How many others agree/react?
   - Additional use cases mentioned?
   - Counter-arguments or concerns?
   - Solutions suggested by community?

4. **Existing Plugin Discussion**
   - Which AI plugins are mentioned?
   - What limitations are discussed?
   - What's missing from current solutions?
   - Privacy/security concerns raised?

5. **Technical Sophistication**
   - User's technical level?
   - Specific technologies mentioned?
   - Implementation questions?
   - API or development interest?

### Classification Schema

**Conversation Type:**
- **Pain Point:** User describing current problem
- **Feature Request:** User suggesting new capability
- **Plugin Discussion:** Evaluation of existing solutions
- **Help Seeking:** User asking how to accomplish something
- **Technical:** Development/implementation discussion

**Alignment with Signal-01:**
- **DIRECT:** Explicitly mentions RAG, AI search, semantic capabilities
- **HIGH:** Describes same problems/needs as signal-01
- **MEDIUM:** Related need, different emphasis
- **LOW:** Tangentially related

**Sentiment:**
- **URGENT:** Strong need, high frustration
- **INTERESTED:** Curious, would like to have
- **NEUTRAL:** Mentioned without strong opinion
- **SKEPTICAL:** Concerns or doubts expressed

## Expected Outputs

### 1. Message Evidence Table

| Date | Channel | Type | Alignment | Sentiment | Reactions | Summary | Key Quote |
|------|---------|------|-----------|-----------|-----------|---------|-----------|
| YYYY-MM-DD | #plugin-ideas | Feature Request | HIGH | URGENT | 👍×5 ❤️×2 | Brief summary | "Direct quote" |

### 2. Thematic Analysis

**Pain Point Themes:**
```markdown
### Theme: Search Result Overload
- **Frequency:** ## mentions
- **Channels:** #help, #general
- **Severity:** URGENT / INTERESTED / NEUTRAL
- **Common Expressions:**
  - "Too many search results"
  - "Can't find what I need"
  - "Search is overwhelming"
- **Workarounds Mentioned:**
  - Manual tagging
  - Folder organization
  - Multiple searches
- **Signal-01 Alignment:** HIGH
```

**Feature Request Themes:**
```markdown
### Theme: AI-Powered Contextual Search
- **Frequency:** ## mentions
- **Channels:** #plugin-ideas, #feature-requests
- **Detail Level:** HIGH / MEDIUM / LOW
- **Specific Features Requested:**
  - Natural language search
  - Semantic understanding
  - Related note discovery
- **Use Cases Described:**
  - [Use case 1]
  - [Use case 2]
- **Signal-01 Alignment:** DIRECT
```

### 3. Community Sentiment Summary

**Overall Demand Level:** HIGH / MEDIUM / LOW

**Evidence:**
- Total relevant conversations: ##
- Unique users expressing need: ##
- Total reactions on related messages: ##
- Date range: YYYY-MM-DD to YYYY-MM-DD
- Trend: Increasing / Stable / Decreasing

**Sentiment Breakdown:**
- Urgent/Strong Need: ##%
- Interested: ##%
- Neutral Mention: ##%
- Skeptical/Concerned: ##%

### 4. Existing Plugin Feedback

**Plugins Discussed:**

**Smart Connections:**
- Mentions: ##
- Positive feedback: ##
- Limitations noted: ##
- Gaps vs. signal-01: [List]

**Text Generator / Copilot / Other AI Plugins:**
- [Same structure for each]

**Unmet Needs:**
- Features requested but not available in any plugin
- Privacy concerns not addressed by current solutions
- Performance issues mentioned
- Cross-device limitations

### 5. Privacy and Security Discussion

**Privacy Concerns Mentioned:**
- Frequency: ##
- Specific concerns: [List]
- Acceptable solutions: [List]
- Deal-breakers: [List]

**Local vs. Cloud Preferences:**
- Local-first advocates: ##
- Open to cloud with privacy: ##
- No strong preference: ##

### 6. User Profile Patterns

**Observable Characteristics:**
- Technical sophistication levels
- Common use cases (academic, professional, personal)
- Vault complexity mentions
- Knowledge management frameworks referenced
- Workflow challenges described

**Alignment with Signal-01 User Profile:**
- Advanced knowledge workers: ## users
- Privacy-focused users: ## users
- High-volume workflow users: ## users

### 7. Real-Time Trend Indicators

**Recent Discussions (Last 30 Days):**
- AI/search related conversations: ##
- Notable spikes in discussion
- New pain points emerging
- Community excitement indicators

**Momentum:**
- Growing interest: [Evidence]
- Stable interest: [Evidence]
- Declining interest: [Evidence]

## Validation Success Criteria

### Minimum Corroboration Threshold
To support signal-01:
- **Minimum 5 relevant conversations** with HIGH alignment
- **At least 10 unique users** expressing similar needs
- **Evidence of organic discussion** (not just one-off mentions)
- **Recent activity** (discussions within last 3 months)

### Confidence Scoring Impact

**If Found:**
- **10+ high-alignment conversations:** +0.10 confidence
- **20+ unique users expressing need:** +0.10 confidence
- **50+ total reactions on related messages:** +0.05 confidence
- **Privacy concerns from 5+ users:** +0.05 confidence
- **Discussion trend increasing:** +0.05 confidence

**If NOT Found:**
- **<5 relevant conversations:** -0.05 confidence
- **Only old discussions (>6 months):** -0.05 confidence
- **Community resistance/skepticism:** -0.10 confidence

## Deliverable Format

```markdown
# Discord Community Market Validation Report

## Executive Summary
- Total conversations analyzed: ##
- Relevant conversations: ##
- Unique users expressing need: ##
- Community sentiment: HIGH / MEDIUM / LOW demand
- Validation outcome: SUPPORTS / PARTIAL / CONTRADICTS signal-01
- Confidence impact: +/- ##

## Message Evidence Summary
[Evidence table]

## Thematic Analysis
[Pain points and feature requests by theme]

## Community Sentiment
[Overall demand assessment]

## Existing Plugin Feedback
[Current solutions and gaps]

## Privacy and Security Findings
[Privacy concern patterns]

## User Profile Patterns
[Demographics and alignment]

## Trend Indicators
[Recent activity and momentum]

## Validation Decision
[Clear statement of support/contradiction]
[Confidence adjustment]
[Rationale]

## Appendix: Notable Conversations
[Detailed summaries of key discussions]
```

### File Naming
Save as: `docs/01-research/signals/validation-evidence/discord-validation-report-YYYY-MM-DD.md`

## Execution Instructions

### Phase 1: Search and Collect (Estimated: 4-5 hours)
1. Join Obsidian Discord server
2. Review channel purposes and activity levels
3. Execute searches for each keyword in relevant channels
4. Manually scan recent activity in key channels
5. Capture relevant conversations with metadata
6. Follow threads and note community responses
7. Document reactions and engagement metrics

### Phase 2: Analyze Patterns (Estimated: 2 hours)
1. Group conversations by theme
2. Calculate sentiment distribution
3. Identify user profile patterns
4. Assess existing plugin gaps
5. Document privacy concerns
6. Analyze trends over time

### Phase 3: Report and Validate (Estimated: 1 hour)
1. Compare findings to signal-01
2. Assess validation criteria
3. Calculate confidence impact
4. Write validation report
5. Provide clear recommendation

**Total Estimated Effort:** 7-8 hours

## Quality Assurance

### Verification Checklist
- [ ] All key channels reviewed
- [ ] Search conducted with primary keywords
- [ ] At least 20 conversations reviewed
- [ ] Evidence table includes dates and channels
- [ ] Quotes are verbatim with context
- [ ] User anonymization applied
- [ ] Sentiment assessment is balanced
- [ ] Trend analysis considers timeframe
- [ ] Clear validation decision provided

### Ethical Considerations
- Anonymize all usernames
- Don't quote private/DM conversations
- Respect community norms
- Consider that Discord users may be more engaged/vocal than average users
- Note if evidence comes from small subset of very active users

## Special Considerations for Discord

**Platform Limitations:**
- Search may be limited without Discord Nitro
- Older messages may not be searchable
- Conversations are less formal than forum/GitHub
- May include more casual complaints vs. structured requests

**Community Dynamics:**
- Active users may dominate discussions
- Real-time nature creates momentum/bandwagon effects
- May capture "hot topic" spikes vs. sustained demand
- Helper community may provide workarounds, reducing visible pain

**Strengths:**
- Real-time, organic sentiment
- Less filtered than formal feature requests
- Captures user frustration in natural language
- Shows what users actually struggle with daily

## Related Documents

- [Signal-01](../../01-research/signals/signal-01-knowledge-worker-rag-demand.md)
- [Forum Validation Prompt](./prompt-obsidian-forum-validation.md)
- [GitHub Validation Prompt](./prompt-github-issues-validation.md)
