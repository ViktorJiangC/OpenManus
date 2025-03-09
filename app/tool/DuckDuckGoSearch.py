import asyncio

from duckduckgo_search import DDGS

from typing import List

from app.tool.base import BaseTool
class DuckDuckGoSearch(BaseTool):
    name: str = "duckduckgo_search"
    description: str = """Perform a DuckDuckGo search and return a list of relevant links."""
    parameters: dict = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "(required) The search query to submit to DuckDuckGo.",
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
        async with DDGS() as ddgs:
            results = await ddgs.text(query, max_results=num_results)
            links = [result["href"] for result in results]
            return links