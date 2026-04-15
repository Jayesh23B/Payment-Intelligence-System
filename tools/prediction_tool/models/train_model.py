import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

from tools.sql_tool.db_connection import create_connection


def train_model():
    connection = create_connection()

   
    query = """
    SELECT 
        merchant_id,
        amount
    FROM transactions
    """

    df = pd.read_sql(query, connection)
    connection.close()

    if df.empty:
        print(" No data found!")
        return

    print(" Data fetched:", df.shape)


   
    df['transaction_hour'] = df.index % 24

    df['merchant_avg_amount'] = df.groupby('merchant_id')['amount'].transform('mean')

    df['amount_deviation'] = df['amount'] - df['merchant_avg_amount']

    df['transaction_count'] = df.groupby('merchant_id')['amount'].transform('count')



    df['is_fraud'] = df.apply(
        lambda row: 1 if (
            row['amount'] > 2000 and
            abs(row['amount_deviation']) > 500
        ) else 0,
        axis=1
    )



    features = [
        'amount',
        'transaction_hour',
        'merchant_avg_amount',
        'amount_deviation',
        'transaction_count'
    ]

    X = df[features]
    y = df['is_fraud']


    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    model_path = os.path.join(
        os.path.dirname(__file__),
        "fraud_model.pkl"
    )

    joblib.dump(model, model_path)

    print(" Model trained and saved at:", model_path)


if __name__ == "__main__":
    train_model()