#!/usr/bin/env python3
"""
Generate README.md and INDEX.md files for all directories in the project.
Follows DIRECTORY_STANDARD.md and DOCUMENTATION_STANDARD.md requirements.
"""

import os
from pathlib import Path
from datetime import date

# Directory metadata: (path, title, description, category)
DIRECTORIES = {
    "docs/02-personas": ("Personas", "User personas and empathy mapping artifacts", "personas"),
    "docs/03-vision": ("Vision", "Product vision and strategic direction", "vision"),
    "docs/04-user-experience-journeys": ("User Experience Journeys", "UX journey mapping and user flows", "ux"),
    "docs/05-requirements": ("Requirements", "Functional and non-functional requirements specifications", "requirements"),
    "docs/06-epics": ("Epics", "Epic-level planning and specifications", "epics"),
    "docs/07-features": ("Features", "Feature specifications and technical requirements", "features"),
    "docs/08-user-stories": ("User Stories", "User story definitions and acceptance criteria", "user-stories"),
    "docs/09-tasks": ("Tasks", "Task definitions and work item tracking", "tasks"),
    "docs/10-micro-tasks": ("Micro Tasks", "Micro-task breakdowns and implementation details", "micro-tasks"),
    "docs/11-nano-tasks": ("Nano Tasks", "Nano-task specifications for granular work tracking", "nano-tasks"),
    "docs/12-story-map": ("Story Map", "User story mapping and prioritization", "story-map"),
    "docs/13-release-roadmap": ("Release Roadmap", "Release roadmap planning and scheduling", "roadmap"),
    "docs/14-release-plan": ("Release Plan", "Detailed release plans and execution tracking", "release-plan"),
    "docs/15-work-queue": ("Work Queue", "Work queue management and prioritization", "work-queue"),
    "docs/a-architecture": ("Architecture", "Architectural documentation and design decisions", "architecture"),
    "docs/a-architecture/solutions": ("Solution Architecture", "Solution-specific architectural artifacts", "solutions"),
    "docs/b-solution-design": ("Solution Design", "Detailed solution design specifications", "design"),
    "docs/c-end-user-documentation": ("End User Documentation", "User-facing documentation and guides", "end-user-docs"),
    "docs/d-organizational-process-assets": ("Organizational Process Assets", "Organizational processes and procedures", "process-assets"),
    "docs/d-organizational-process-assets/processes-and-procedures": ("Processes and Procedures", "Process definitions and procedural documentation", "processes"),
    "docs/d-organizational-process-assets/project-management-scripts": ("Project Management Scripts", "Automation scripts for project management", "pm-scripts"),
    "docs/d-organizational-process-assets/templates": ("Project Templates", "Project-specific document templates", "templates"),
    "docs/e-assets": ("Assets", "Project assets including images, prompts, and scripts", "assets"),
    "docs/e-assets/pics": ("Pictures and Diagrams", "Visual assets, diagrams, and screenshots", "images"),
    "docs/e-assets/prompts": ("AI Prompts", "AI agent prompts and prompt templates", "prompts"),
    "docs/e-assets/scripts": ("Utility Scripts", "Documentation and utility scripts", "scripts"),
    "docs/standards": ("Standards", "Project-specific standards and guidelines", "standards"),
    "work/user-stories": ("Active User Stories", "In-progress user story execution", "work"),
    "work/tasks": ("Active Tasks", "Current task execution and tracking", "work"),
    "work/micro-tasks": ("Active Micro Tasks", "In-progress micro-task execution", "work"),
    "work/nano-tasks": ("Active Nano Tasks", "Current nano-task execution", "work"),
    "work/release-plans": ("Active Release Plans", "In-progress release planning", "work"),
    "src": ("Source Code", "Application source code", "source"),
    "tests": ("Test Suites", "Automated test suites and quality validation", "testing"),
    "iac": ("Infrastructure as Code", "Infrastructure provisioning and configuration", "infrastructure"),
    "iac/terraform": ("Terraform", "Terraform configurations and modules", "terraform"),
    "iac/terraform/modules": ("Terraform Modules", "Reusable Terraform modules", "terraform"),
    "iac/ansible": ("Ansible", "Ansible playbooks and roles", "ansible"),
    "iac/ansible/playbooks": ("Ansible Playbooks", "Ansible automation playbooks", "ansible"),
    "iac/ansible/roles": ("Ansible Roles", "Ansible role definitions", "ansible"),
    "iac/scripts": ("IaC Scripts", "Infrastructure automation scripts", "scripts"),
    "compliance": ("Compliance", "Compliance documentation and evidence", "compliance"),
    "compliance/policies": ("Policies", "Compliance policies and governance", "policies"),
    "compliance/controls": ("Controls", "Control specifications and requirements", "controls"),
    "compliance/procedures": ("Procedures", "Compliance procedures and workflows", "procedures"),
    "compliance/evidence": ("Evidence", "Compliance evidence and artifacts", "evidence"),
    "compliance/evidence/logs": ("Evidence Logs", "Compliance evidence log files", "logs"),
    "compliance/evidence/screenshots": ("Evidence Screenshots", "Visual evidence and screenshots", "screenshots"),
    "compliance/audit": ("Audit", "Audit reports and findings", "audit"),
    "compliance/bundles": ("Compliance Bundles", "Integrated compliance evidence packages", "bundles"),
    "releases": ("Releases", "Immutable release packages and artifacts", "releases"),
    "ops": ("Operations", "Operational state and runtime management", "operations"),
    "ops/locks": ("Concurrency Locks", "Operational concurrency control", "locks"),
    "ops/queues": ("Processing Queues", "Work queues and processing state", "queues"),
    "ops/runbooks": ("Runbooks", "Operational runbooks and procedures", "runbooks"),
    "ops/state": ("Operational State", "Runtime state management", "state"),
    "ops/state/terraform": ("Terraform State", "Terraform state files", "terraform-state"),
    "ops/state/pipelines": ("Pipeline State", "CI/CD pipeline state", "pipeline-state"),
    "examples": ("Examples", "Reference examples and sample projects", "examples"),
}

def generate_readme(dir_path, title, description, category):
    """Generate README.md content for a directory."""
    today = date.today().strftime("%Y-%m-%d")

    content = f"""---
title: "{title} Directory"
description: "{description}"
doc_type: "readme"
author: "Devin Hedge"
version: "1.0"
last_updated: "{today}"
status: "active"
category: "{category}"
tags: ["{category}", "directory"]
related_docs: ["INDEX.md"]
---

# {title} Directory

## Purpose

{description}

## Structure

This directory is part of the Obsidian Tools project's canonical directory structure, following the enterprise DIRECTORY_STANDARD.md requirements.

## Usage

### Adding Content

1. Follow the naming conventions: lowercase-with-hyphens.md
2. Include proper YAML frontmatter in all markdown files
3. Maintain README.md and INDEX.md in all subdirectories
4. Reference related documents for traceability

### Documentation Standards

All files in this directory must comply with:
- DOCUMENTATION_STANDARD.md - General formatting and frontmatter requirements
- DIRECTORY_STANDARD.md - Directory organization and structure
- Context-specific standards (if applicable)

## Related Documents

- [Directory Index](INDEX.md) - Navigation guide for this directory
- [Project Index](../../INDEX.md) - Root project navigation
- [Enterprise Standards](../../../../../../enterprise/chl-standards/)
"""
    return content

def generate_index(dir_path, title, description, category):
    """Generate INDEX.md content for a directory."""
    today = date.today().strftime("%Y-%m-%d")

    content = f"""---
title: "{title} Index"
description: "Navigation guide for {title.lower()}"
doc_type: "index"
author: "Devin Hedge"
version: "1.0"
last_updated: "{today}"
status: "active"
category: "navigation"
tags: ["index", "navigation", "{category}"]
related_docs: ["README.md"]
---

# {title} Index

## Directory Purpose

{description}

## Quick Navigation

### Current Contents

This directory is currently empty or contains files not yet indexed.

### Adding Content

When adding files to this directory:

1. Follow naming conventions (lowercase-with-hyphens.md)
2. Include proper YAML frontmatter
3. Update this INDEX.md with links to new content
4. Maintain traceability to related documents

## File Organization

Files in this directory should follow the patterns established in DIRECTORY_STANDARD.md and DOCUMENTATION_STANDARD.md.

## Related Documents

- [Directory Purpose and Usage](README.md) - Detailed information about this directory
- [Project Index](../../INDEX.md) - Root project navigation
"""
    return content

def main():
    """Generate README.md and INDEX.md for all directories."""
    script_dir = Path(__file__).parent.parent.parent.parent
    os.chdir(script_dir)

    created_count = 0
    skipped_count = 0

    print("Generating directory documentation...")
    print(f"Working directory: {os.getcwd()}")
    print()

    for dir_path, (title, description, category) in DIRECTORIES.items():
        if not os.path.exists(dir_path):
            print(f"Warning: Directory {dir_path} does not exist, skipping...")
            continue

        readme_path = os.path.join(dir_path, "README.md")
        index_path = os.path.join(dir_path, "INDEX.md")

        # Generate README.md if it doesn't exist
        if not os.path.exists(readme_path):
            readme_content = generate_readme(dir_path, title, description, category)
            with open(readme_path, 'w') as f:
                f.write(readme_content)
            print(f"Created: {readme_path}")
            created_count += 1
        else:
            print(f"Skipped: {readme_path} (already exists)")
            skipped_count += 1

        # Generate INDEX.md if it doesn't exist
        if not os.path.exists(index_path):
            index_content = generate_index(dir_path, title, description, category)
            with open(index_path, 'w') as f:
                f.write(index_content)
            print(f"Created: {index_path}")
            created_count += 1
        else:
            print(f"Skipped: {index_path} (already exists)")
            skipped_count += 1

    print()
    print(f"Generation complete!")
    print(f"Created: {created_count} files")
    print(f"Skipped: {skipped_count} files (already existed)")

if __name__ == "__main__":
    main()
