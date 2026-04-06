from tools.sql_tool.query_builder import execute_query

def sql_tool_func(query: str):
    
    result = execute_query(query)

    # ✅ If result is DataFrame → format it
    try:
        return result.to_string(index=False)
    except:
        # ✅ If already string → return directly
        return str(result)