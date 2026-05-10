from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os 


async def main():

    # Create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

    # MCP Server Config (JSON)
    {
        "agentic_terminal":{
            "transport": "stdio",
            "command": "uvx",
            "args": ["agentic_terminal"]
        }

    }
    )

    # List the tools
    tools = await client.get_tools()
    for tool in tools:
        print("Available tool:", tool.name)



if __name__ == "__main__":
    asyncio.run(main())
