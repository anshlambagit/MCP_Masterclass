from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os 
from dotenv import load_dotenv
load_dotenv()


async def main():

    # Create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

    # MCP Server Config (JSON)
    {
        "tavily_mcp_http":{
            "transport": "streamable-http",
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={os.getenv('TAVILY_API_KEY')}"
        }

    }
    )

    # List the tools
    tools = await client.get_tools()
    for tool in tools:
        print("Available tool:", tool.name)

    tool_search = [tool for tool in tools if tool.name == "tavily_search"][0]
    result = await tool_search.ainvoke({"query": "What is the capital of France?"})
    print("Tool result:", result)

if __name__ == "__main__":
    asyncio.run(main())
