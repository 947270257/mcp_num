from mcp.server.fastmcp import FastMCP

#初始化MCP对象
mcp = FastMCP("Demo 🚀")

#装饰器，用来给函数增加功能，申明函数是MCP工具
@mcp.tool()
def add(a: int, b: int) -> int:
  #使用自然语言告诉模型这个函数的功能是什么
    """Add two numbers"""
    return a + b
# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="stdio")