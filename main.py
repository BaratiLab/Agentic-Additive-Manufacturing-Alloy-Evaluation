import argparse

from pathlib import Path
from typing import cast

from am.mcp.install import install as install_am
from wa.mcp.install import install as install_wa
from tc.mcp.install import install as install_tc
from tc.cli.install import install_command


def main():
    parser = argparse.ArgumentParser(description="Install MCP Servers for AM Alloy Discovery")
    _ = parser.add_argument(
        "client",
        choices=["claude-code", "codex", "gemini-cli"],
        default="claude-code",
        help="Target client for MCP server installation (default: claude-code)"
    )
    args = parser.parse_args()
    client = cast(str, args.client)

    print(f"Installing MCP Servers for {client}")
    path = Path(__file__).parent

    install_am(path, client=client)
    install_wa(path, client=client)
    install_tc(path, client=client)

    print("Installing TC-Python")
    install_command(None)

if __name__ == "__main__":
    main()

