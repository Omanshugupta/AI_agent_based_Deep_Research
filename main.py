from dotenv import load_dotenv
load_dotenv()

from graph.research_graph import DeepResearchGraph

if __name__ == "__main__":
    
    graph = DeepResearchGraph().build()

    query = input("Enter your research topic: ")
    result = graph.invoke({"topic": query})  # 👈 this sends a dict

    print("\n===== Final Answer =====\n")
    print(result)