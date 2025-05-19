import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient


async def run_memory_chat():
    # Load .env file
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))
    print("Resolved .env path:", env_path)
    print("Does .env exist?", os.path.exists(env_path))

    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("GROQ_API_KEY")
    print("Loaded GROQ_API_KEY:", api_key if api_key else "❌ Not found!")

    os.environ["GROQ_API_KEY"] = api_key or ""

    # Load MCP client from config
    config_file = "browser_mcp.json"
    print("Initializing chat...")

    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="qwen-qwq-32b", api_key=api_key)

    # 🧠 System prompt to guide tool usage
    system_prompt = (
        "You are a smart assistant that selects the correct MCP tool based on user queries. "
        "Use the 'airbnb' tool for travel or housing-related questions. "
        "Use 'groq' for general LLM-based reasoning and text generation. "
        "Use 'duckduckgo-search' for searching the web. "
        "Use 'playwright' to open and interact with websites. "
        "Use 'desktop-commander' to perform OS-level desktop tasks. "
    )

    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=100,
        memory_enabled=True,
        system_prompt=system_prompt
    )

    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("Type 'clear' to clear conversation history.")
    print("================================\n")

    try:
        while True:
            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            try:
                print("Running agent...")
                response = await asyncio.wait_for(agent.run(user_input), timeout=20)
                print("Agent run complete.")
                print(f"\nAgent: {response}")
            except asyncio.TimeoutError:
                print("Agent call timed out!")

    except KeyboardInterrupt:
        print("\nConversation interrupted. Exiting...")


if __name__ == "__main__":
    asyncio.run(run_memory_chat())
