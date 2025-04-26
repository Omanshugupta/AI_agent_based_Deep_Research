
# 🧠 Deep Research AI Agentic System

A multi-agent system for deep online research and content drafting using real-time web search via **Tavily**, structured workflows with **LangGraph**, and intelligent agent orchestration through **LangChain**.

## 🚀 Overview

This project implements a **dual-agent AI system**:
- A **Research Agent** that performs real-time online information gathering.
- A **Drafting Agent** that synthesizes the collected data into coherent, human-readable content.

These agents communicate via a **LangGraph state machine**, enabling a seamless flow from query to finalized report.

## 🧩 Architecture

```
User Prompt
   │
   ▼
Research Agent (Tavily Search + Summarizer)
   │
   ▼
Drafting Agent (LLM-based Answer Composer)
   │
   ▼
Final Output (Markdown / Text Summary)
```

- **Framework**: LangGraph, LangChain
- **Search Engine**: Tavily API
- **LLM**: OpenAI GPT / Claude / Gemini (configurable)
- **Optional**: FAISS / SQLite for memory storage

## 📂 Directory Structure

```
deep-research-agent/
├── agents/
│   ├── research_agent.py     # Tavily search & summarization logic
│   └── answer_drafter.py        # Answer composition logic
├── graph/
│   └── research_graph.py       # LangGraph workflow
├── main.py                     # Entry point to run the system
├── requirements.txt            # Python dependencies
└── README.md                    # Project documentation
```

## 🛠️ Installation

### 1. Clone the Repo
```bash
git clone https://github.com/Omanshugupta/AI_agent_based_Deep_Research
cd AI_agent_based_Deep_Research
```

### 2. Create & Activate Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file:
```
OPENAI_API_KEY=your-key
TAVILY_API_KEY=your-key
```

## 💡 How It Works

1. **Input Prompt**: User provides a research query.
2. **Research Agent**: Uses Tavily to search top results and summarizes them.
3. **Drafting Agent**: Uses an LLM to compile structured responses from the summarized data.
4. **Output**: Final draft is returned as plain text or Markdown.

## 🧪 Example Use Case

```bash
> python main.py
Enter your query: "Latest advancements in generative AI for e-commerce"
```

Sample output (abridged):
```
### Summary of Findings:
- Generative AI is being adopted for personalized product generation, synthetic data creation, and virtual shopping assistants.
- Major players include Shopify, Amazon, and OpenAI...

### Sources:
1. [TechCrunch article](https://example.com)
2. [OpenAI Blog](https://example.com)
...
```

## ✅ Features

- 🌐 Real-time search with Tavily
- 🧠 LLM-based summarization and drafting
- 🔗 Agent collaboration via LangGraph
- 📄 Markdown output ready for blogs, reports, or documentation
- 📚 Extensible and modular design

## 📌 Future Enhancements

- Add citation formatting (APA/MLA)
- Multi-agent feedback loops
- PDF export and auto-email output
- LangChain memory integration (e.g., long-term research threads)

## 📜 License

MIT License. Feel free to fork, extend, and build on this.

## 🙋 About the Developer

Omanshu Gupta  
AI Developer | Full Stack Data Science & AI  
