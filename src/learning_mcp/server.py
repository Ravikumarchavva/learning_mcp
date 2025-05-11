# server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo", stateless_http=True)

@mcp.resource("hello://{name}")
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
