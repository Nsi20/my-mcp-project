# my-mcp-project
A starting point for an MCP-based project.

# MCPProject

An interactive, multi-tool AI assistant powered by [LangChain](https://python.langchain.com/), [Groq LLM](https://groq.com/), and [MCP (Multi-Command Platform)](https://github.com/wonderwye/mcp). This project enables advanced conversational AI with access to a variety of tools for web search, travel, browser automation, and desktop commands.

## Features

- **Conversational AI**: Chat with an agent powered by Groq LLM via LangChain.
- **Tool Selection**: The agent can select and use the correct tool for your query:
  - **Airbnb**: Travel and housing-related queries
  - **Groq**: General LLM-based reasoning and text generation
  - **DuckDuckGo**: Web search
  - **Playwright**: Website automation and interaction
  - **Desktop Commander**: OS-level desktop tasks
- **Memory**: Maintains conversation history (can be cleared during chat).
- **Configurable**: Easily add or modify tools via `browser_mcp.json`.

## Project Structure

- `app.py` — Main entry point for the interactive chat agent.
- `main.py` — Simple hello-world script.
- `groq_test.py` — Example/test for Groq LLM usage.
- `browser_mcp.json` — Configuration for available MCP tools.
- `.env` — Store your API keys and secrets (not included in repo).
- `pyproject.toml` — Python dependencies and project metadata.

## Requirements

- Python 3.11
- [pip](https://pip.pypa.io/en/stable/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd mcpproject
   ```
2. **Create a virtual environment:**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt  # or use poetry/pip-tools if preferred
   ```
   Or, if using `pyproject.toml`:
   ```bash
   pip install .
   ```
4. **Set up environment variables:**
   - Create a `.env` file in the project root with your Groq API key:
     ```env
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage

Run the interactive chat agent:

```bash
python app.py
```

- Type your queries and the agent will select the appropriate tool.
- Type `exit` or `quit` to end the conversation.
- Type `clear` to clear the conversation history.

### Example: Test Groq LLM

```bash
python groq_test.py
```

## Configuration

- **Tools**: Edit `browser_mcp.json` to add or modify available tools and their configurations.
- **API Keys**: Store sensitive keys in `.env` (never commit this file).

## Dependencies

- `langchain-groq`
- `langchain-openai`
- `mcp-use`
- (See `pyproject.toml` for full list)

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to your fork and submit a pull request

## Acknowledgments

- [LangChain](https://python.langchain.com/)
- [Groq](https://groq.com/)
- [MCP](https://github.com/wonderwye/mcp)

