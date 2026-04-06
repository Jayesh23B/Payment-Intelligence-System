from langchain_community.chat_models import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate

from agent.tools import get_tools


def create_agent():
    
    llm = ChatOllama(
        model="llama3:8b",
        temperature=0
    )

    tools = get_tools()

    prompt = PromptTemplate.from_template("""
You are an AI agent.

Use tools to answer questions.

Available tools:
{tools}

Format:

Question: {input}
Thought: decide tool
Action: one of [{tool_names}]
Action Input: input
Observation: result
Final Answer: return the result

Rules:
- Be fast
- Do not overthink
- Do not repeat steps

Question: {input}
{agent_scratchpad}
""")

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        handle_parsing_errors=True,   
        max_iterations=3
    )

    return agent_executor