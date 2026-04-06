from tools.prediction_tool.predictor import make_prediction

def prediction_tool_func(input_data: str):
    
    try:
        # Step 1: Convert string to dictionary
        input_dict = eval(input_data)
        
        # Step 2: Call prediction logic
        result = make_prediction(input_dict)
        
        # Step 3: Return as string (important for agent)
        return str(result)
    
    except Exception as error:
        return f"Invalid input: {str(error)}"