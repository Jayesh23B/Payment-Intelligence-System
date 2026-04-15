import os
import joblib

def load_model():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))

        model_path = os.path.join(
            current_dir,
            "models",
            "fraud_model.pkl"
        )

        print("DEBUG: Loading model from:", model_path)

        if not os.path.exists(model_path):
            print(" Model file not found at:", model_path)
            return None

        model = joblib.load(model_path)
        print(" Model loaded successfully")

        return model

    except Exception as error:
        print(" Model loading failed:", error)
        return None