---
title: "Research Directory"
description: "Repository for research artifacts, prototypes, and experimental findings"
doc_type: "readme"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "research"
tags: ["research", "prototypes", "experiments", "findings"]
related_docs: ["INDEX.md", "../INDEX.md"]
---

# Research Directory

## Purpose

This directory serves as the repository for research artifacts, prototypes, and experimental findings. Research materials are versioned by release lineage to ensure traceability between research outputs and corresponding product releases.

## Structure

Research is organized into release-specific subdirectories:

```
01-research/
├── Release-1-GenAI-Assets/
│   ├── models/
│   ├── benchmarks/
│   └── findings.md
└── Release-2-GenAI-Assets/
    ├── models/
    ├── benchmarks/
    └── findings.md
```

## Usage

### Adding Research Artifacts

1. Create a release-specific subdirectory if it does not exist
2. Organize materials into appropriate subdirectories (models, benchmarks, etc.)
3. Document findings in a `findings.md` file
4. Link research artifacts to corresponding work items in `/work/`

### Research Types

- **Models**: AI/ML models, training data, model specifications
- **Benchmarks**: Performance benchmarks, comparison studies
- **Findings**: Research conclusions, insights, recommendations
- **Prototypes**: Proof-of-concept implementations
- **Experiments**: Experimental code and results

## Traceability

All research artifacts should maintain clear traceability to:
- Product releases in `/releases/`
- Feature specifications in `/docs/07-features/`
- Epic definitions in `/docs/06-epics/`

## Related Documents

- [Research Index](INDEX.md) - Navigation guide for research artifacts
- [Documentation Standards](../standards/DOCUMENTATION_STANDARD.md) - General documentation standards
- [Work Standard](../standards/WORK_STANDARD.md) - Work decomposition and traceability
