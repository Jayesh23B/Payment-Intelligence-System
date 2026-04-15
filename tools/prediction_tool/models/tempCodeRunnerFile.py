import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from tools.sql_tool.db_connection import create_connection

def train_model():

    connection = create_connection()

    query = """
    SELECT merchant_id, amount
    FROM transactions
    """

    df = pd.read_sql(query, connection)
    connection.close()

    if df.empty:
        print("No data found!")
        return

    print(" Data fetched:", df.shape)

    # Temporary fraud logic
    df['is_fraud'] = df['amount'].apply(lambda x: 1 if x > 5000 else 0)

    X = df[['amount', 'merchant_id']]
    y = df['is_fraud']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # ✅ Save in SAME folder
    model_path = os.path.join(
        os.path.dirname(__file__),
        "fraud_model.pkl"
    )

    joblib.dump(model, model_path)

    print(" Model saved at:", model_path)


if __name__ == "__main__":
    train_model()