import pyodbc

def create_connection():
    
    connection_string = (
        "DRIVER={SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=PaymentIntelligenceC;"
        "Trusted_Connection=yes;"
    )
    
    try:
        connection = pyodbc.connect(connection_string)
        
        return connection
    
    except Exception as error:
        print("Database connection failed:", error)
        return None