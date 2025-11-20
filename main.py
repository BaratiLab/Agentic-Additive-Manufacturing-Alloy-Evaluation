import argparse
import json
import os

from pathlib import Path
from typing import cast

from am.mcp.install import install as install_am
from wa.mcp.install import install as install_wa
from tc.mcp.install import install as install_tc
from tc.cli.install import install_command


def main():
    parser = argparse.ArgumentParser(
        description="Install MCP Servers for AM Alloy Discovery"
    )
    _ = parser.add_argument(
        "client",
        choices=["claude-code", "codex", "gemini-cli", "vscode"],
        default="vscode",
        help="Target client for MCP server installation (default: claude-code)",
    )
    args = parser.parse_args()
    client = cast(str, args.client)

    print(f"Installing MCP Servers for {client}")
    if client == "vscode":
        # Build environment variables from system environment
        tc_env = {}
        if java_home := os.environ.get("JAVA_HOME"):
            tc_env["JAVA_HOME"] = java_home
        if tc25b_home := os.environ.get("TC25B_HOME"):
            tc_env["TC25B_HOME"] = tc25b_home
        if lshost := os.environ.get("LSHOST"):
            tc_env["LSHOST"] = lshost

        mcp_config = {
            "servers": {
                "additive-manufacturing": {
                    "type": "stdio",
                    "command": "uv",
                    "args": ["run", "-m", "am.mcp"],
                },
                "thermo-calc": {
                    "type": "stdio",
                    "command": "uv",
                    "args": ["run", "-m", "tc.mcp"],
                    "env": tc_env,
                },
                "workspace": {
                    "type": "stdio",
                    "command": "uv",
                    "args": ["run", "-m", "wa.mcp"],
                },
            },
            "inputs": [],
        }

        # Create .vscode folder if it doesn't exist
        vscode_dir = Path(".vscode")
        vscode_dir.mkdir(exist_ok=True)

        # Write mcp.json file
        mcp_json_path = vscode_dir / "mcp.json"
        with open(mcp_json_path, "w") as f:
            json.dump(mcp_config, f, indent=4)

        print(f"Written MCP config to {mcp_json_path}")

    else:
        path = Path(__file__).parent

        install_am(path, client=client)
        install_wa(path, client=client)
        install_tc(path, client=client)

    print("Installing TC-Python")
    install_command(None)


if __name__ == "__main__":
    main()
