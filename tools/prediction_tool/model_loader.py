import joblib

def load_model():
    
    # Step 1: Define model path
    model_path = "fraud_model.pkl"

    try:
        # Step 2: Load model
        model = joblib.load(model_path)
        
        return model
    
    except Exception as error:
        print("Model loading failed:", error)
        return None