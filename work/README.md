---
title: "Work Directory"
description: "Active work execution mirror for in-flight work items"
doc_type: "readme"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "work"
tags: ["work", "execution", "active"]
related_docs: ["INDEX.md", "../INDEX.md"]
---

# Work Directory

## Purpose

The `/work/` directory serves as the execution mirror for active, evolving, or automation-generated artifacts. It tracks work items that are currently in progress, while the `/docs/` directory maintains immutable historical records.

## Structure

The work directory mirrors the logical structure of the `/docs/` directory for work-related artifacts:

```
work/
├── user-stories/     → docs/08-user-stories/
├── tasks/            → docs/09-tasks/
├── micro-tasks/      → docs/10-micro-tasks/
├── nano-tasks/       → docs/11-nano-tasks/
└── release-plans/    → docs/14-release-plan/
```

## Usage

### Adding Work Items

1. Create work items in the appropriate subdirectory
2. Use descriptive names following the naming convention: `lowercase-with-hyphens.md`
3. Include proper YAML frontmatter with status tracking
4. Update the directory's INDEX.md with links to new work items

### Work Item Lifecycle

Work items flow through the following lifecycle:

1. **Created** - Work item is defined in `/work/`
2. **In Progress** - Work is actively being performed
3. **Completed** - Work is finished and validated
4. **Archived** - Completed work moves to corresponding `/docs/` directory

### Status Tracking

Work items should include status information in their frontmatter:
- `status: "pending"` - Not yet started
- `status: "in_progress"` - Currently being worked on
- `status: "blocked"` - Waiting on dependencies
- `status: "completed"` - Finished and ready for archival

## Separation from Documentation

This separation ensures:
- `/docs/` remains an immutable historical record
- `/work/` stays dynamic and reflects current state
- Clear distinction between planning and execution
- Traceability from active work to completed documentation

## Work Item Graduation

When work items are completed:

1. **Validate** - Ensure acceptance criteria are met
2. **Archive** - Move from `/work/` to corresponding `/docs/` directory
3. **Update** - Update INDEX.md files in both locations
4. **Link** - Maintain traceability links between work and documentation

## Enterprise Standards Compliance

This work structure follows the Calature Holdings enterprise standards:
- Directory structure: `../../../../../../enterprise/chl-standards/standards/DIRECTORY_STANDARD.md`
- Work standards: `../../../../../../enterprise/chl-standards/standards/WORK_STANDARD.md`

## Related Documents

- [Work Index](INDEX.md) - Navigation guide for active work items
- [Documentation Directory](../docs/README.md) - Immutable documentation repository
- [Project Index](../INDEX.md) - Root project navigation
