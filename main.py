from pathlib import Path

from am.mcp.install import install as install_am
from wa.mcp.install import install as install_wa
from tc.mcp.install import install as install_tc
from tc.cli.install import install_command


def main():
    print("Installing MCP Servers")
    path = Path(__file__).parent

    install_am(path, client="claude-code")
    install_wa(path, client="claude-code")
    install_tc(path, client="claude-code")

    print("Installing TC-Python")
    install_command(None)

if __name__ == "__main__":
    main()

