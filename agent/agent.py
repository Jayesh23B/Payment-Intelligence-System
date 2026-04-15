from langchain_community.chat_models import ChatOllama
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate

from agent.tools import get_tools
from agent.prompt import get_system_prompt


def create_agent():
    
    llm = ChatOllama(
        model="llama3:8b",
        temperature=0
    )

    tools = get_tools()

    # ✅ System prompt
    system_prompt = get_system_prompt()

    # ✅ Combined prompt
    prompt = PromptTemplate.from_template(f"""
{system_prompt}

---------------------------------------

You have access to the following tools:
{{tools}}

Available tool names:
{{tool_names}}

---------------------------------------

You MUST follow this format EXACTLY:

Question: {{input}}

Thought: <your reasoning>

Action: <tool name EXACTLY from [{{tool_names}}]>

Action Input: <input to the tool>

Observation: <tool result>

Final Answer: <your final response>

---------------------------------------

STRICT RULES:

- NEVER write sentences in Action
- Action must be EXACT tool name only

- Action Input MUST be:
  • ONLY valid SQL query (for SQL Tool)
  • ONLY None (for Prediction Tool)
  • NO explanations, NO comments, NO extra text

  - If model is not available:
  • Return error
  • DO NOT retry
  • DO NOT switch tools

- Prediction Tool:
  • Requires NO input → always use: None
  • NEVER try to train model

- SQL Tool:
  • MUST receive ONLY executable SQL
  • NEVER include English text

- If model is not available:
  • Return the error
  • DO NOT retry
  • DO NOT switch tools

- ALWAYS use correct SQL Server syntax
- NEVER use LIMIT
- ALWAYS use TOP
- Use ONLY given schema

- Do NOT loop
- After one tool call → return Final Answer

---------------------------------------

Question: {{input}}
{{agent_scratchpad}}
""")

    # ✅ Create agent
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    # ✅ Executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5,
        max_execution_time=60,
    )

    return agent_executor