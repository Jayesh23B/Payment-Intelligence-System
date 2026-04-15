import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from tools.sql_tool.db_connection import create_connection

def execute_query(query: str):
    
    connection = create_connection()
    
    if connection is None:
        return "No connection available"
    
    try:
        dataframe = pd.read_sql(query, connection)
        
        connection.close()
        
        result = dataframe.head(10)
        
        return result
    
    except Exception as error:
        return f"Query execution failed: {str(error)}"