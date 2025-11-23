---
title: "Work Index"
description: "Navigation guide for active work items"
doc_type: "index"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "navigation"
tags: ["index", "navigation", "work"]
related_docs: ["README.md", "../INDEX.md"]
---

# Work Index

## Directory Purpose

This directory contains active, in-progress work items that are currently being executed. Upon completion, these items graduate to the corresponding directories in `/docs/`.

## Quick Navigation

### Active Work Directories

- [user-stories/](user-stories/) - Active user story execution
- [tasks/](tasks/) - Current task execution
- [micro-tasks/](micro-tasks/) - In-progress micro-tasks
- [nano-tasks/](nano-tasks/) - Current nano-task execution
- [release-plans/](release-plans/) - Active release planning

## Work Item Status

### Current Work Load

To see current active work items, check each subdirectory's INDEX.md:

- [User Stories Index](user-stories/INDEX.md)
- [Tasks Index](tasks/INDEX.md)
- [Micro Tasks Index](micro-tasks/INDEX.md)
- [Nano Tasks Index](nano-tasks/INDEX.md)
- [Release Plans Index](release-plans/INDEX.md)

## Work Flow

### Adding New Work

1. Identify the work item type (user story, task, etc.)
2. Create the work item in the appropriate subdirectory
3. Follow naming conventions and include proper frontmatter
4. Update the subdirectory's INDEX.md

### Completing Work

1. Update work item status to "completed"
2. Validate against acceptance criteria
3. Archive to corresponding `/docs/` directory
4. Update INDEX.md files in both locations

### Work Item Tracking

Use the following status values in frontmatter:
- `pending` - Not yet started
- `in_progress` - Currently active
- `blocked` - Waiting on dependencies
- `completed` - Finished and ready for archival

## Relationship to Documentation

Work items in `/work/` correspond to documentation in `/docs/`:

| Work Directory | Documentation Directory |
|----------------|------------------------|
| work/user-stories/ | docs/08-user-stories/ |
| work/tasks/ | docs/09-tasks/ |
| work/micro-tasks/ | docs/10-micro-tasks/ |
| work/nano-tasks/ | docs/11-nano-tasks/ |
| work/release-plans/ | docs/14-release-plan/ |

## Related Documents

- [Work Directory Purpose](README.md) - Detailed information about the work directory
- [Documentation Index](../docs/INDEX.md) - Documentation repository
- [Project Index](../INDEX.md) - Root project navigation
