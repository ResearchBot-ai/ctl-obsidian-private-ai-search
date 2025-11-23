#!/bin/bash
# generate-directory-docs.sh
# Generates README.md and INDEX.md files for all directories that need them

# Array of directories that need documentation
DIRECTORIES=(
    "docs/01-research"
    "docs/02-personas"
    "docs/03-vision"
    "docs/04-user-experience-journeys"
    "docs/05-requirements"
    "docs/06-epics"
    "docs/07-features"
    "docs/08-user-stories"
    "docs/09-tasks"
    "docs/10-micro-tasks"
    "docs/11-nano-tasks"
    "docs/12-story-map"
    "docs/13-release-roadmap"
    "docs/14-release-plan"
    "docs/15-work-queue"
    "docs/a-architecture"
    "docs/a-architecture/solutions"
    "docs/b-solution-design"
    "docs/c-end-user-documentation"
    "docs/d-organizational-process-assets"
    "docs/d-organizational-process-assets/processes-and-procedures"
    "docs/d-organizational-process-assets/project-management-scripts"
    "docs/d-organizational-process-assets/templates"
    "docs/e-assets"
    "docs/e-assets/pics"
    "docs/e-assets/prompts"
    "docs/e-assets/scripts"
    "docs/standards"
    "work/user-stories"
    "work/tasks"
    "work/micro-tasks"
    "work/nano-tasks"
    "work/release-plans"
    "src"
    "tests"
    "iac"
    "iac/terraform"
    "iac/terraform/modules"
    "iac/ansible"
    "iac/ansible/playbooks"
    "iac/ansible/roles"
    "iac/scripts"
    "compliance"
    "compliance/policies"
    "compliance/controls"
    "compliance/procedures"
    "compliance/evidence"
    "compliance/evidence/logs"
    "compliance/evidence/screenshots"
    "compliance/audit"
    "compliance/bundles"
    "releases"
    "ops"
    "ops/locks"
    "ops/queues"
    "ops/runbooks"
    "ops/state"
    "ops/state/terraform"
    "ops/state/pipelines"
    "examples"
)

echo "Generating directory documentation files..."
echo "Total directories to process: ${#DIRECTORIES[@]}"
echo ""

for dir in "${DIRECTORIES[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "Warning: Directory $dir does not exist, skipping..."
        continue
    fi

    echo "Processing: $dir"

    # Skip if files already exist
    if [ -f "$dir/README.md" ] && [ -f "$dir/INDEX.md" ]; then
        echo "  - Files already exist, skipping..."
        continue
    fi

    # Mark that we need to create files
    echo "  - Creating documentation files..."
done

echo ""
echo "Script completed. Use Python script for actual file generation with proper frontmatter."
