Demo 🚀 服务文档
许可证
🌟 项目简介
本项目基于FastMCP框架实现模型控制协议服务，提供：

同步工具调用：实现加法计算功能
动态资源路由：支持个性化问候语生成
标准协议支持：符合Model Control Protocol规范
🧠 技术架构
mermaid
graph TD
    A[客户端] -->|HTTP/WebSocket| B(FastMCP服务)
    B --> C{功能模块}
    C --> D[工具调用]
    C --> E[资源路由]
    D --> F[add函数]
    E --> G[greeting资源]
    B --> H[Pydantic数据验证]
    B --> I[SSE流式响应]

🛠️ 环境要求
组件	版本要求
Python	3.10+
FastMCP	0.1.0+
Pydantic	2.0.0+
Uvicorn	0.22.0+

📦 安装指南
bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 安装依赖
pip install fastmcp pydantic uvicorn sse-starlette
🚀 快速启动
bash
# 启动服务（stdio模式）
python main.py

# 或使用Uvicorn启动（推荐生产环境）
uvicorn main:app --reload
🧩 核心功能
1. 工具调用 add
python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
调用示例：

json
{
  "method": "add",
  "params": {"a": 2, "b": 3},
  "response": 5
}
2. 动态资源 greeting://{name}
python
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
访问示例：

bash
GET /greeting://Alice
# 返回: "Hello, Alice!"
📡 接口规范
工具调用接口
方法: POST /tool_call
请求体:
json
{
  "method": "add",
  "params": {"a": 2, "b": 3}
}
响应:
json
{
  "result": 5
}
资源访问接口
方法: GET /greeting://{name}
路径参数:
name: 需问候的名称
🛡️ 服务部署
生产环境配置
bash
# 使用Uvicorn部署
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
Docker部署示例
dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
📐 开发规范
类型注解：所有函数必须使用Python类型注解
文档字符串：每个工具/资源需包含docstring说明
异常处理：使用PydanticCustomError进行错误处理
日志记录：使用标准logging模块输出日志
代码风格：遵循PEP8规范

🤝 贡献代码
Fork仓库
创建特性分支 git checkout -b feature/xxx
提交代码 git commit -am 'Add xxx'
推送分支 git push origin feature/xxx
创建PR并附上修改说明

📄 许可证
MIT License（需替换为实际许可证）

📌 注意事项
生产环境需补充：

 JWT身份验证
 请求限流策略
 Prometheus监控指标
 分布式追踪支持
 容错处理机制
服务默认使用stdio通信，生产环境建议切换为HTTP模式：

python
if __name__ == "__main__":
    mcp.run(transport="http", port=8000)