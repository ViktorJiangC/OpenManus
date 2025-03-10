import asyncio
from typing import List
from baidusearch.baidusearch import search  # 确保已安装 baidusearch 库

from app.tool.base import BaseTool


class BaiduSearch(BaseTool):
    name: str = "baidu_search"
    description: str = """Perform a Baidu search and return a list of relevant links.
Use this tool when you need to find information on Chinese websites, 
get China-specific data, or research topics better covered by Baidu.
The tool returns a list of URLs that match the search query.
"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "(required) The search query to submit to Baidu.",
            },
            "num_results": {
                "type": "integer",
                "description": "(optional) The number of search results to return. Default is 10.",
                "default": 10,
            },
        },
        "required": ["query"],
    }

    async def execute(self, query: str, num_results: int = 10) -> List[str]:
        """
        Execute a Baidu search and return a list of URLs.

        Args:
            query (str): The search query to submit to Baidu.
            num_results (int, optional): The number of search results to return. Default is 10.

        Returns:
            List[str]: A list of URLs matching the search query.
        """
        # 在异步上下文中执行同步搜索
        loop = asyncio.get_event_loop()
        results = await loop.run_in_executor(
            None, 
            lambda: list(search(query, num=num_results))
        )
        
        # 提取真实URL（假设返回结果已是最终链接）
        return [result['url'] for result in results[:num_results]]