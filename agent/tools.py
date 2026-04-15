from langchain.tools import Tool

from tools.sql_tool.sql_tool import sql_tool_func
from tools.prediction_tool.predictor_tool import prediction_tool_func


def get_tools():
    
    sql_tool = Tool(
        name="SQL Tool",
        func=sql_tool_func,
        description="""
Use ONLY for database queries.

- Input MUST be valid SQL
- Use for transactions, merchants, stored data
- Do NOT use for prediction
- Examples:
  • top merchants
  • transaction counts
  • revenue analysis
  • merchant statistics
""",
        return_direct=True
    )
    
    prediction_tool = Tool(
        name="Prediction Tool",
        func=prediction_tool_func,
        description="""
Use for fraud and risk prediction.

- Automatically fetches data from database
- No input required from user
- Returns high-risk merchants
""",
    return_direct=True
    )
    
    return [sql_tool, prediction_tool]