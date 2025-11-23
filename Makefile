.PHONY: help install build test clean validate-structure validate-docs lint release

# Default target
help:
	@echo "Obsidian Tools - Available Makefile targets:"
	@echo ""
	@echo "  install              Install all dependencies"
	@echo "  build                Build all packages"
	@echo "  test                 Run all tests"
	@echo "  clean                Clean build artifacts"
	@echo "  validate-structure   Validate directory structure compliance"
	@echo "  validate-docs        Validate documentation standards"
	@echo "  lint                 Run linters"
	@echo "  release              Create a release"
	@echo ""

# Install dependencies
install:
	@echo "Installing dependencies..."
	yarn install

# Build all packages
build:
	@echo "Building all packages..."
	yarn build

# Run tests
test:
	@echo "Running tests..."
	yarn test

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	lerna clean --yes
	rm -rf packages/*/lib
	rm -rf packages/*/dist
	rm -rf node_modules
	rm -rf packages/*/node_modules

# Validate directory structure
validate-structure:
	@echo "Validating directory structure..."
	@python3 docs/e-assets/scripts/validate_structure.py

# Validate documentation standards
validate-docs:
	@echo "Validating documentation..."
	@echo "Checking for README.md and INDEX.md in all directories..."
	@find docs work src tests iac compliance releases ops examples -type d -exec test -f {}/README.md -a -f {}/INDEX.md \; -print || echo "Missing README.md or INDEX.md in some directories"
	@echo "Validation complete."

# Run linters
lint:
	@echo "Running linters..."
	@echo "Prettier check..."
	@npx prettier --check "**/*.{js,ts,json,md}"

# Create release
release:
	@echo "Creating release..."
	yarn release
