import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from tools.sql_tool.db_connection import create_connection

def execute_query(query: str):
    
    # Step 1: Get database connection
    connection = create_connection()
    
    if connection is None:
        return "No connection available"
    
    try:
        # Step 2: Execute query
        dataframe = pd.read_sql(query, connection)
        
        # Step 3: Close connection
        connection.close()
        
        # Step 4: Limit rows for readability
        result = dataframe.head(10)
        
        return result
    
    except Exception as error:
        return f"Query execution failed: {str(error)}"