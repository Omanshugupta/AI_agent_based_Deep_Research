from langchain_community.tools.tavily_search.tool import TavilySearchResults

def research_agent(run: dict) -> dict:
    topic = run.get("topic") or run.get("query") or run
    tavily = TavilySearchResults()
    result = tavily.invoke(topic)
    return {"articles": result}  # ✅ wrap result in a dict
