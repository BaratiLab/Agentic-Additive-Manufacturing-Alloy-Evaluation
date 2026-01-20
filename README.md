# Agentic-Additive-Manufacturing-Alloy-Evaluation
Multi-agent workflow configuration for additive manufacturing alloy evaluation via Model Context Protocol (MCP)

<p align="center">
  <img src="./images/figures/main.png" alt="Main Figure" width="80%">
</p>

## Getting Started
1. Clone Repository
2. Install Thermo-Calc 2025B with TC-Python
    - Make sure environment variables `TC25B_HOME`, `LSHOST`, and `JAVA_HOME` are set.
3. Install [`uv`](https://docs.astral.sh/uv/)
4. Sync `additive-manufacturing`, `thermo-calc`, and `workspace-agent` packages.
    ```bash
    uv sync
    ```
1. Install LLM client such as [Claude Desktop](https://claude.ai/download), [Claude Code](https://docs.anthropic.com/en/docs/claude-code/setup), [Codex](https://developers.openai.com/codex/cli/), or [Gemini CLI](https://github.com/google-gemini/gemini-cli)
5. Install MCP tools and Agents to Client (i.e. [`claude-desktop`](https://claude.ai/download), [`vscode`](), [`claude-code`](https://docs.anthropic.com/en/docs/claude-code/setup), [`codex`](https://developers.openai.com/codex/cli/), or [`gemini-cli`](https://github.com/google-gemini/gemini-cli))
    ```
    uv run main.py <client>
    ```

### VSCode
1. Open Copilot and click on the tools icon
<p align="center">
  <img src="./images/screenshots/vscode_copilot_tools_open_menu.png" alt="Copilot tools open menu" width="80%">
</p>

2. Update the tools for `additive-manufacturing`, `thermo-calc`, and `workspace`
<p align="center">
  <img src="./images/screenshots/vscode_copilot_tools_update.png" alt="Copilot tools open menu" width="80%">
</p>

3. (Optional) Toggle off all other tools for better performance (i.e. "Built-In", "Python", "Jupyter", etc.)

## MCP Servers
<table>
  <tr>
    <td align="center" width="100">
      <img src="./images/icons/additive-manufacturing.svg" alt="Additive Manufacturing" width="100%">
    </td>
    <td>
      <a href="https://github.com/ppak10/additive-manufacturing"><b>Additive Manufacturing</b></a><br>
      <code>uv add additive-manufacturing</code><br>
      <code>pip install additive-manufacturing</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="100">
      <img src="./images/icons/thermo-calc.svg" alt="Thermo-Calc" width="100%">
    </td>
    <td>
      <a href="https://github.com/ppak10/thermo-calc"><b>Thermo-Calc</b></a><br>
      <code>uv add thermo-calc</code><br>
      <code>pip install thermo-calc</code>
    </td>
  </tr>
  <tr>
    <td align="center" width="100">
      <img src="./images/icons/workspace-agent.svg" alt="Workspace Agent" width="100%">
    </td>
    <td>
      <a href="https://github.com/ppak10/workspace-agent"><b>Workspace Agent</b></a><br>
      <code>uv add workspace-agent</code><br>
      <code>pip install workspace-agent</code>
    </td>
  </tr>
</table>
