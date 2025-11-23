---
title: "Documentation Root"
description: "Canonical documentation and research repository for Obsidian Tools"
doc_type: "readme"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "documentation"
tags: ["documentation", "root", "structure"]
related_docs: ["INDEX.md", "../INDEX.md"]
---

# Documentation Root

## Purpose

This directory serves as the canonical documentation and research repository for the Obsidian Tools project. It follows a structured approach that mirrors the lifecycle of discovery, design, delivery, validation, and release.

## Structure

The documentation is organized into two main categories:

### Work Decomposition Chain (01-15)

Sequential directories following the work decomposition chain from signals through release:

- **01-research/** - Research and prototype material
- **02-personas/** - User personas and empathy mapping
- **03-vision/** - Product vision and strategic direction
- **04-user-experience-journeys/** - UX journey mapping
- **05-requirements/** - Requirements specifications
- **06-epics/** - Epic-level planning
- **07-features/** - Feature specifications
- **08-user-stories/** - User story definitions
- **09-tasks/** - Task definitions
- **10-micro-tasks/** - Micro-task breakdowns
- **11-nano-tasks/** - Nano-task specifications
- **12-story-map/** - Story mapping
- **13-release-roadmap/** - Release roadmap planning
- **14-release-plan/** - Release plans
- **15-work-queue/** - Work queue management

### Supporting Documentation (a-e)

Lettered directories for architecture, design, and supporting materials:

- **a-architecture/** - Architectural documentation
  - **solutions/** - Solution-specific architecture
- **b-solution-design/** - Solution design artifacts
- **c-end-user-documentation/** - End-user documentation
- **d-organizational-process-assets/** - Organizational processes
  - **processes-and-procedures/** - Process definitions
  - **project-management-scripts/** - PM automation scripts
  - **templates/** - Project-specific templates
- **e-assets/** - Project assets
  - **pics/** - Images and diagrams
  - **prompts/** - AI prompts
  - **scripts/** - Utility scripts
- **standards/** - Project-specific standards

## Usage

### Documentation Standards

All documentation in this directory must follow:

1. **DOCUMENTATION_STANDARD.md** - General formatting and frontmatter requirements
2. **DIRECTORY_STANDARD.md** - Directory organization and structure
3. Context-specific standards (e.g., EPIC_STANDARD.md, USER_PERSONA_STANDARD.md)

### Naming Conventions

- Use lowercase with hyphens: `feature-name.md`
- Include descriptive prefixes: `01-task-name.md` for ordered items
- Use `.md` extension for all documentation

### Required Files

Every directory must contain:
- **README.md** - Context and purpose
- **INDEX.md** - Navigation and structure

## Integration with Work Directory

The `/docs/` directory maintains immutable historical records, while the `/work/` directory contains active, evolving artifacts. Work items graduate from `/work/` to `/docs/` upon completion.

## Enterprise Standards Compliance

This documentation structure follows the Calature Holdings enterprise standards:
- Directory structure: `../../../../../../enterprise/chl-standards/standards/DIRECTORY_STANDARD.md`
- Documentation standards: `../../../../../../enterprise/chl-standards/DOCUMENTATION_STANDARD.md`
- Work standards: `../../../../../../enterprise/chl-standards/standards/WORK_STANDARD.md`

## Related Documents

- [Documentation Index](INDEX.md) - Navigation guide for all documentation
- [Project Index](../INDEX.md) - Root project navigation
- [Enterprise Standards](../../../../../../enterprise/chl-standards/)
