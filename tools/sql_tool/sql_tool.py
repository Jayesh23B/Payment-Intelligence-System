from tools.sql_tool.query_builder import execute_query

import pandas as pd

def sql_tool_func(query: str):
    result = execute_query(query)

    if isinstance(result, str):
        return result

    if result.empty:
        return "No data found."

    return result.to_string(index=False)