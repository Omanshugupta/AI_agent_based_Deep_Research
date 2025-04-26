from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def answer_drafter_agent(run: dict) -> dict:
    message = run.get("articles", "")
    llm = ChatOpenAI(model="gpt-3.5-turbo")  # or "gpt-4-turbo" if available
    return {"answer": llm.invoke([HumanMessage(content=message)]).content}
