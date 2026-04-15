import pandas as pd
from tools.prediction_tool.model_loader import load_model

def make_prediction(input_data: dict):
    
    model = load_model()
    
    if model is None:
        return "Model not available"
    
    try:
        input_dataframe = pd.DataFrame([input_data])
        
        
        expected_columns = [
            "amount",
            "channel",
            "currency",
            "customer_segment",
            "customer_country"
        ]
        
        input_dataframe = input_dataframe[expected_columns]
        
        
        prediction = model.predict(input_dataframe)
        
        
        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(input_dataframe)[0][1]
        else:
            probability = None
        
        
        if prediction[0] == 1:
            label = "High Risk / Fraud"
        else:
            label = "Low Risk / Safe"
        
        
        
        result = {
            "prediction": label,
            "probability": probability
        }
        
        return result
    
    except Exception as error:
        return f"Prediction failed: {str(error)}"