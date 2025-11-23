---
title: "Obsidian Tools Project Index"
description: "Navigation guide for the Obsidian Tools monorepo structure"
doc_type: "index"
author: "Devin Hedge"
version: "1.0"
last_updated: "2025-11-23"
status: "active"
category: "navigation"
tags: ["index", "navigation", "structure", "obsidian-tools"]
related_docs: ["README.md", "CLAUDE.md", "docs/standards/INDEX.md"]
---

# Obsidian Tools Project Index

## Quick Navigation

### Core Documentation
- [Project Overview](README.md) - What is this project and why does it exist
- [CLAUDE.md](CLAUDE.md) - AI assistant guidance for working with this codebase
- [CHANGELOG.md](CHANGELOG.md) - Version history and release notes

### Package Documentation
- [auto-plugin-obsidian](packages/auto-plugin-obsidian/README.md) - Auto plugin for release automation
- [create-obsidian-plugin](packages/create-obsidian-plugin/README.md) - Plugin scaffolding tool
- [obsidian-cli](packages/obsidian-cli/README.md) - Alternative CLI implementation
- [obsidian-plugin-cli](packages/obsidian-plugin-cli/README.md) - Primary development CLI
- [obsidian-utils](packages/obsidian-utils/README.md) - Core utilities library

## Directory Structure

### `/docs/` - Documentation and Research
Sequential documentation following the work decomposition chain:

#### Work Decomposition Chain (01-15)
- [01-research/](docs/01-research/) - Research and prototype material
- [02-personas/](docs/02-personas/) - User personas
- [03-vision/](docs/03-vision/) - Product vision
- [04-user-experience-journeys/](docs/04-user-experience-journeys/) - UX journeys
- [05-requirements/](docs/05-requirements/) - Requirements specifications
- [06-epics/](docs/06-epics/) - Epic planning
- [07-features/](docs/07-features/) - Feature specifications
- [08-user-stories/](docs/08-user-stories/) - User stories
- [09-tasks/](docs/09-tasks/) - Task definitions
- [10-micro-tasks/](docs/10-micro-tasks/) - Micro-task breakdowns
- [11-nano-tasks/](docs/11-nano-tasks/) - Nano-task specifications
- [12-story-map/](docs/12-story-map/) - Story mapping
- [13-release-roadmap/](docs/13-release-roadmap/) - Release roadmap planning
- [14-release-plan/](docs/14-release-plan/) - Release plans
- [15-work-queue/](docs/15-work-queue/) - Work queue management

#### Architecture and Design (a-e)
- [a-architecture/](docs/a-architecture/) - Architectural documentation
  - [solutions/](docs/a-architecture/solutions/) - Solution-specific architecture
- [b-solution-design/](docs/b-solution-design/) - Solution design artifacts
- [c-end-user-documentation/](docs/c-end-user-documentation/) - End-user documentation
- [d-organizational-process-assets/](docs/d-organizational-process-assets/) - Organizational processes
  - [processes-and-procedures/](docs/d-organizational-process-assets/processes-and-procedures/)
  - [project-management-scripts/](docs/d-organizational-process-assets/project-management-scripts/)
  - [templates/](docs/d-organizational-process-assets/templates/)
- [e-assets/](docs/e-assets/) - Project assets
  - [pics/](docs/e-assets/pics/) - Images and diagrams
  - [prompts/](docs/e-assets/prompts/) - AI prompts
  - [scripts/](docs/e-assets/scripts/) - Utility scripts

#### Standards
- [standards/](docs/standards/) - Project-specific standards

### `/work/` - Active Work Execution
Dynamic workspace for in-flight work items:
- [user-stories/](work/user-stories/) - Active user stories
- [tasks/](work/tasks/) - Current tasks
- [micro-tasks/](work/micro-tasks/) - Active micro-tasks
- [nano-tasks/](work/nano-tasks/) - Current nano-tasks
- [release-plans/](work/release-plans/) - Active release planning

### `/src/` - Source Code
All source code is organized in the [packages/](packages/) directory as a Lerna monorepo.

### `/tests/` - Test Suites
Test suites mirroring the source structure:
- Unit tests
- Integration tests
- End-to-end tests

### `/iac/` - Infrastructure as Code
Infrastructure provisioning and configuration:
- [terraform/](iac/terraform/) - Terraform configurations
  - [modules/](iac/terraform/modules/) - Reusable Terraform modules
- [ansible/](iac/ansible/) - Ansible playbooks and roles
  - [playbooks/](iac/ansible/playbooks/)
  - [roles/](iac/ansible/roles/)
- [scripts/](iac/scripts/) - Infrastructure scripts

### `/compliance/` - Compliance and Audit
Compliance documentation and evidence:
- [policies/](compliance/policies/) - Compliance policies
- [controls/](compliance/controls/) - Control specifications
- [procedures/](compliance/procedures/) - Compliance procedures
- [evidence/](compliance/evidence/) - Compliance evidence
  - [logs/](compliance/evidence/logs/)
  - [screenshots/](compliance/evidence/screenshots/)
- [audit/](compliance/audit/) - Audit reports
- [bundles/](compliance/bundles/) - Compliance bundles

### `/releases/` - Release Packages
Immutable release artifacts with SBOMs and attestations.

### `/ops/` - Operational State
Runtime state and operational documentation:
- [locks/](ops/locks/) - Concurrency locks
- [queues/](ops/queues/) - Processing queues
- [runbooks/](ops/runbooks/) - Operational runbooks
- [state/](ops/state/) - State management
  - [terraform/](ops/state/terraform/)
  - [pipelines/](ops/state/pipelines/)

### `/examples/` - Examples and Samples
Reference implementations and sample projects.

## Configuration Files

### Root Configuration
- [package.json](package.json) - Root workspace configuration
- [lerna.json](lerna.json) - Lerna monorepo configuration
- [jest.config.js](jest.config.js) - Jest test configuration
- [.gitignore](.gitignore) - Git ignore patterns
- [.prettierrc](.prettierrc) - Code formatting configuration

### Package Configuration
Each package contains its own:
- `package.json` - Package dependencies and scripts
- `tsconfig.json` - TypeScript configuration
- Additional package-specific configuration

## Development Workflows

### Getting Started
1. Review [README.md](README.md) for project overview
2. Review [CLAUDE.md](CLAUDE.md) for development guidance
3. Install dependencies: `yarn install`
4. Build all packages: `yarn build`

### Common Tasks
- Run tests: `yarn test`
- Build packages: `yarn build`
- Release: `yarn release`

### Package Development
- Navigate to package: `cd packages/[package-name]`
- Follow package-specific README for development instructions

## Enterprise Standards Integration

This project follows the Calature Holdings enterprise standards framework:
- **Directory Structure**: Follows `../../../../../../enterprise/chl-standards/standards/DIRECTORY_STANDARD.md`
- **Documentation Standards**: Follows `../../../../../../enterprise/chl-standards/DOCUMENTATION_STANDARD.md`
- **Work Standards**: Follows `../../../../../../enterprise/chl-standards/standards/WORK_STANDARD.md`

## Related Documents

- [README.md](README.md) - Project overview and purpose
- [CLAUDE.md](CLAUDE.md) - AI assistant development guidance
- [CHANGELOG.md](CHANGELOG.md) - Version history
- Enterprise Standards: `../../../../../../enterprise/chl-standards/`
