#!/usr/bin/env python3
"""Setup script for Linux administration workspace with Claude Code."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"  {description}...")
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"  ✓ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ {description} failed: {e.stderr.strip()}")
        return False
    except FileNotFoundError:
        print(f"  ✗ Command not found: {cmd[0]}")
        return False


def check_command_exists(cmd: str) -> bool:
    """Check if a command exists in PATH."""
    try:
        subprocess.run(
            ["which", cmd], check=True, capture_output=True, text=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


def main():
    print("Linux Admin Workspace Setup")
    print("=" * 40)

    project_dir = Path(__file__).parent.resolve()
    config_link = project_dir / "config"
    config_target = Path.home() / ".config"
    scripts_dir = project_dir / "scripts"

    # Check for uv
    print("\n[1/4] Checking prerequisites...")
    if not check_command_exists("uv"):
        print("  ✗ uv is not installed")
        print("    Install with: curl -LsSf https://astral.sh/uv/install.sh | sh")
        sys.exit(1)
    print("  ✓ uv is installed")

    # Install linux-mcp-server
    print("\n[2/4] Installing linux-mcp-server...")
    if check_command_exists("linux-mcp-server"):
        print("  ✓ linux-mcp-server is already installed")
    else:
        if not run_command(
            ["uv", "tool", "install", "linux-mcp-server"],
            "Installing linux-mcp-server"
        ):
            print("    Try manually: uv tool install linux-mcp-server")
            sys.exit(1)

    # Setup config symlink
    print("\n[3/4] Setting up config symlink...")
    if config_link.exists():
        if config_link.is_symlink():
            current_target = config_link.resolve()
            if current_target == config_target:
                print(f"  ✓ config/ already links to {config_target}")
            else:
                print(f"  ! config/ links to {current_target} (not {config_target})")
        else:
            print("  ! config/ exists but is not a symlink")
    else:
        if config_target.exists():
            config_link.symlink_to(config_target)
            print(f"  ✓ Created symlink: config/ -> {config_target}")
        else:
            print(f"  ✗ {config_target} does not exist")

    # Setup scripts directory
    print("\n[4/4] Setting up scripts directory...")
    if scripts_dir.exists():
        print(f"  ✓ scripts/ already exists")
    else:
        scripts_dir.mkdir()
        print(f"  ✓ Created scripts/")

    # Summary
    print("\n" + "=" * 40)
    print("Setup complete!")
    print("\nYou can now run Claude Code in this directory.")
    print("The linux-mcp-server tools will be available for system diagnostics.")


if __name__ == "__main__":
    main()
