import pandas as pd
from tools.prediction_tool.model_loader import load_model

def make_prediction(input_data: dict):
    
    # Step 1: Load model
    model = load_model()
    
    if model is None:
        return "Model not available"
    
    try:
        # Step 2: Convert input into DataFrame
        input_dataframe = pd.DataFrame([input_data])
        
        
        # Step 3: Define expected columns (IMPORTANT)
        expected_columns = [
            "amount",
            "channel",
            "currency",
            "customer_segment",
            "customer_country"
        ]
        
        input_dataframe = input_dataframe[expected_columns]
        
        
        # Step 4: Make prediction
        prediction = model.predict(input_dataframe)
        
        
        # Step 5: Get probability (if available)
        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(input_dataframe)[0][1]
        else:
            probability = None
        
        
        # Step 6: Convert to readable output
        if prediction[0] == 1:
            label = "High Risk / Fraud"
        else:
            label = "Low Risk / Safe"
        
        
        # Step 7: Prepare result
        result = {
            "prediction": label,
            "probability": probability
        }
        
        return result
    
    except Exception as error:
        return f"Prediction failed: {str(error)}"