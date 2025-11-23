# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Obsidian Tools**: A monorepo collection of tools that helps developers build plugins for [Obsidian](https://obsidian.md/). This is a TypeScript-based project using Lerna for monorepo management and yarn workspaces.

## Monorepo Architecture

This is a Lerna monorepo with independent versioning. All packages are located in `packages/` and managed as yarn workspaces.

### Package Structure

- **create-obsidian-plugin**: Plugin scaffolding tool (npm init obsidian-plugin / yarn create obsidian-plugin)
- **obsidian-plugin-cli**: Complete plugin development CLI with build, dev, and install commands
- **obsidian-cli**: Alternative CLI implementation for plugin development workflows
- **obsidian-utils**: Core utilities library for programmatic Obsidian interactions (vault management, plugin registry, installation)
- **auto-plugin-obsidian**: Auto plugin for automating Obsidian plugin releases

### Key Architecture Concepts

**Vault Management**: The obsidian-utils package provides cross-platform vault detection by reading Obsidian's configuration files. It supports:
- macOS: `~/Library/Application Support/Obsidian`
- Windows: AppData locations
- Linux: `~/.config/obsidian`, `~/.obsidian`, or XDG paths
- WSL: Detects Windows paths via wslvar and wslpath

**Plugin Installation**: Plugins can be installed from:
- Obsidian community plugin registry (by name)
- GitHub repositories (by owner/repo or full URL)
- Local disk (for development)

**Build System**: Uses esbuild for fast TypeScript compilation and bundling. Each package may have custom esbuild configurations.

## Common Development Commands

### Root Level (Monorepo)

```bash
# Install all dependencies
yarn install

# Build all packages
yarn build
# or
npm run build

# Run tests across all packages
yarn test
# or
npm test

# Release (uses auto for automated releases)
yarn release
```

### Individual Package Development

```bash
# Navigate to a specific package
cd packages/obsidian-utils

# Build a specific package
yarn build

# Run tests for a specific package
yarn test

# Watch mode for tests
yarn test:watch

# Test coverage
yarn test:coverage
```

### obsidian-plugin-cli Commands

```bash
# Build a plugin for release
obsidian-plugin build [ENTRYPOINT]

# Development mode (watch + copy to vault)
obsidian-plugin dev [ENTRYPOINT]

# Install a plugin from registry or GitHub
obsidian-plugin install [PLUGIN]

# Options for dev command:
# -v, --vault-path=vault-path    Explicit vault path
# -n, --no-prompts              Disable interactive prompts
# -e, --esbuild-config          Path to custom esbuild config
# -S, --with-stylesheet         Include stylesheet

# Options for build command:
# -o, --output-dir=output-dir   Output directory (default: dist)
# -e, --esbuild-config          Custom esbuild config path
# -S, --with-stylesheet         Include stylesheet
```

### Testing

```bash
# Root level tests (runs all packages)
jest

# Test specific package
cd packages/obsidian-utils
yarn test

# Watch mode
yarn test:watch
```

### Documentation Generation

```bash
# Generate API docs for obsidian-utils
cd packages/obsidian-utils
yarn generate-docs
```

## Development Workflow

### Working on a Package

1. Make changes to source code in `packages/[package-name]/src/`
2. Build the package: `yarn build` (from package directory or root)
3. Test changes: `yarn test`
4. For plugin CLI development, use `obsidian-plugin dev` to test in a real vault

### Creating a New Plugin (End User)

```bash
# Initialize new plugin
npm init obsidian-plugin
# or
yarn create obsidian-plugin

# With plugin ID
yarn create obsidian-plugin my-plugin-id
```

### Testing Plugin Development Workflow

```bash
# From a plugin project directory
obsidian-plugin dev

# This will:
# - Build the plugin with esbuild
# - Watch for changes
# - Auto-detect or prompt for vault selection
# - Copy compiled files to vault's .obsidian/plugins/ directory
```

## Build and Release

### Lerna Configuration

- Uses independent versioning (each package has its own version)
- Uses yarn as npm client
- Configured with yarn workspaces

### Auto Configuration

The project uses [auto](https://github.com/intuit/auto) for automated releases with plugins:
- npm (publish to npm registry)
- all-contributors (contributor management)
- first-time-contributor (welcome first-time contributors)
- released (label management)

### Publishing

```bash
# Automated release (from root)
yarn release

# This will:
# - Determine version bumps
# - Update changelogs
# - Create git tags
# - Publish to npm
# - Update contributors
```

## TypeScript Configuration

Each package has its own `tsconfig.json` that extends a base configuration. All packages target Node.js environments with ES module output.

## Testing Setup

Uses Jest with ts-jest for TypeScript support:
- Root jest.config.js configures projects for all packages
- Each package may have additional Jest configuration in package.json
- Test files use pattern: `**/__tests__/**` or `**/*.test.ts` or `**/*.spec.ts`

## Key Dependencies

### Production
- **esbuild**: Fast bundler for plugin compilation
- **oclif**: CLI framework (for obsidian-plugin-cli)
- **node-fetch**: HTTP requests for plugin registry API
- **which/execa**: Process execution and binary detection
- **prompts**: Interactive CLI prompts

### Development
- **lerna**: Monorepo management
- **jest/ts-jest**: Testing framework
- **typescript**: Type checking and compilation
- **auto**: Release automation
- **typedoc**: API documentation generation (obsidian-utils)

## File Organization

```text
.
├── packages/
│   ├── auto-plugin-obsidian/     # Auto plugin for release automation
│   ├── create-obsidian-plugin/   # Plugin scaffolding
│   ├── obsidian-cli/             # Alternative CLI
│   ├── obsidian-plugin-cli/      # Primary development CLI
│   └── obsidian-utils/           # Core utilities library
├── resources/                     # Shared resources (logos, etc)
├── .github/                       # GitHub workflows and configs
├── lerna.json                     # Lerna configuration
├── jest.config.js                 # Root Jest configuration
└── package.json                   # Root workspace configuration
```

## Important Notes

- **No tests in obsidian-plugin-cli**: The package.json shows `test: echo NO TESTS`
- **esbuild workspace nohoist**: The root package.json specifies esbuild should not be hoisted to avoid version conflicts
- **Platform-specific vault detection**: Vault finding logic varies by OS and includes WSL support
- **Independent versioning**: Each package maintains its own version number
- **TypeScript compilation**: Each package compiles independently but may share type definitions through package dependencies

## Troubleshooting

### Vault Not Found
If vault auto-detection fails, explicitly pass `--vault-path` to obsidian-plugin commands or check:
- Obsidian is installed
- At least one vault has been opened
- Configuration files exist in platform-specific locations

### Build Failures
- Ensure all dependencies are installed: `yarn install` from root
- Rebuild all packages: `yarn build` from root
- Check for TypeScript errors in specific package

### Lerna Issues
- Clear bootstrap: `lerna clean` (if available)
- Reinstall: `rm -rf node_modules packages/*/node_modules && yarn install`
