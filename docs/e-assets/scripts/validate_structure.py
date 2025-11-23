#!/usr/bin/env python3
"""
Validate project structure against DIRECTORY_STANDARD.md requirements.
"""

import os
import sys
from pathlib import Path

# Required root-level directories per DIRECTORY_STANDARD.md
REQUIRED_DIRS = [
    "docs",
    "work",
    "src",
    "tests",
    "iac",
    "compliance",
    "releases",
    "ops",
]

# Required root-level files
REQUIRED_FILES = [
    "README.md",
    "INDEX.md",
    "Makefile",
    ".gitignore",
]

# Required docs subdirectories
REQUIRED_DOCS_DIRS = [
    "docs/01-research",
    "docs/02-personas",
    "docs/03-vision",
    "docs/04-user-experience-journeys",
    "docs/05-requirements",
    "docs/06-epics",
    "docs/07-features",
    "docs/08-user-stories",
    "docs/09-tasks",
    "docs/10-micro-tasks",
    "docs/11-nano-tasks",
    "docs/12-story-map",
    "docs/13-release-roadmap",
    "docs/14-release-plan",
    "docs/15-work-queue",
    "docs/a-architecture",
    "docs/b-solution-design",
    "docs/c-end-user-documentation",
    "docs/d-organizational-process-assets",
    "docs/e-assets",
    "docs/standards",
]

# Required work subdirectories
REQUIRED_WORK_DIRS = [
    "work/user-stories",
    "work/tasks",
    "work/micro-tasks",
    "work/nano-tasks",
    "work/release-plans",
]

def check_directory_exists(dir_path):
    """Check if a directory exists."""
    if os.path.isdir(dir_path):
        return True, f"✓ {dir_path}"
    return False, f"✗ {dir_path} (missing)"

def check_file_exists(file_path):
    """Check if a file exists."""
    if os.path.isfile(file_path):
        return True, f"✓ {file_path}"
    return False, f"✗ {file_path} (missing)"

def check_directory_has_docs(dir_path):
    """Check if a directory has README.md and INDEX.md."""
    readme = os.path.join(dir_path, "README.md")
    index = os.path.join(dir_path, "INDEX.md")

    readme_exists = os.path.isfile(readme)
    index_exists = os.path.isfile(index)

    if readme_exists and index_exists:
        return True, f"✓ {dir_path} (has README.md and INDEX.md)"
    elif not readme_exists and not index_exists:
        return False, f"✗ {dir_path} (missing README.md and INDEX.md)"
    elif not readme_exists:
        return False, f"✗ {dir_path} (missing README.md)"
    else:
        return False, f"✗ {dir_path} (missing INDEX.md)"

def main():
    """Run structure validation."""
    print("=" * 80)
    print("Directory Structure Validation")
    print("=" * 80)
    print()

    errors = []
    warnings = []

    # Check root directories
    print("Checking required root directories...")
    for dir_path in REQUIRED_DIRS:
        success, message = check_directory_exists(dir_path)
        print(f"  {message}")
        if not success:
            errors.append(message)
    print()

    # Check root files
    print("Checking required root files...")
    for file_path in REQUIRED_FILES:
        success, message = check_file_exists(file_path)
        print(f"  {message}")
        if not success:
            errors.append(message)
    print()

    # Check docs subdirectories
    print("Checking required docs subdirectories...")
    for dir_path in REQUIRED_DOCS_DIRS:
        success, message = check_directory_exists(dir_path)
        print(f"  {message}")
        if not success:
            errors.append(message)
    print()

    # Check work subdirectories
    print("Checking required work subdirectories...")
    for dir_path in REQUIRED_WORK_DIRS:
        success, message = check_directory_exists(dir_path)
        print(f"  {message}")
        if not success:
            errors.append(message)
    print()

    # Check README.md and INDEX.md in all directories
    print("Checking README.md and INDEX.md in all directories...")
    all_dirs = REQUIRED_DIRS + REQUIRED_DOCS_DIRS + REQUIRED_WORK_DIRS + ["iac", "compliance", "ops"]

    for dir_path in all_dirs:
        if os.path.isdir(dir_path):
            success, message = check_directory_has_docs(dir_path)
            print(f"  {message}")
            if not success:
                warnings.append(message)
    print()

    # Summary
    print("=" * 80)
    print("Validation Summary")
    print("=" * 80)
    print()

    if not errors and not warnings:
        print("✓ All checks passed!")
        print()
        return 0

    if errors:
        print(f"✗ Found {len(errors)} error(s):")
        for error in errors:
            print(f"  {error}")
        print()

    if warnings:
        print(f"⚠ Found {len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  {warning}")
        print()

    if errors:
        print("Structure validation FAILED")
        return 1
    else:
        print("Structure validation PASSED (with warnings)")
        return 0

if __name__ == "__main__":
    sys.exit(main())
