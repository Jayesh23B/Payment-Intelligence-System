import pyodbc

def create_connection():
    
    # Step 1: Define connection string
    connection_string = (
        "DRIVER={SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=PaymentIntelligenceC;"
        "Trusted_Connection=yes;"
    )
    
    try:
        # Step 2: Create connection
        connection = pyodbc.connect(connection_string)
        
        return connection
    
    except Exception as error:
        print("Database connection failed:", error)
        return None