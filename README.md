# Linux Admin

A workspace for Linux system administration tasks, designed for use with Claude Code and the linux-mcp-server.

## Overview

This project provides a structured environment for:
- Diagnosing system issues (CPU, memory, disk, network)
- Managing and troubleshooting systemd services
- Reviewing system and service logs
- Creating reusable Python scripts for common admin tasks

## Requirements

- Python 3.10+
- [linux-mcp-server](https://github.com/anthropics/linux-mcp-server) (provides read-only diagnostic tools)

## Structure

```
linux-admin/
├── config/       # Symlink to ~/.config for managing user configs
├── scripts/      # Reusable Python admin scripts
├── pyproject.toml
└── CLAUDE.md     # Instructions for Claude Code
```

## Usage

This workspace is intended for use with Claude Code. The MCP server provides diagnostic tools for:

- **System info**: OS version, CPU, memory, disk usage
- **Services**: List services, check status, view logs
- **Processes**: List and inspect running processes
- **Network**: Interfaces, connections, listening ports
- **Logs**: Query systemd journal and read log files

## Adding Scripts

Place reusable Python scripts in `scripts/`. Scripts should:
- Use Python 3.10+ with standard library modules when possible
- Include a shebang (`#!/usr/bin/env python3`) and be executable
- Use `argparse` for command-line arguments
- Include docstrings explaining usage

## License

MIT
