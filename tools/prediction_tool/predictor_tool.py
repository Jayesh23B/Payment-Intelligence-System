import pandas as pd
from tools.sql_tool.db_connection import create_connection
from tools.prediction_tool.model_loader import load_model


def prediction_tool_func(query: str):
    try:

        model = load_model()

        if model is None:
            return "❌ Model not loaded. Please train the model first."


        connection = create_connection()

        sql_query = """
        SELECT merchant_id, amount
        FROM transactions
        """

        df = pd.read_sql(sql_query, connection)
        connection.close()

        if df.empty:
            return "No transaction data available."



        df['transaction_hour'] = df.index % 24

        df['merchant_avg_amount'] = df.groupby('merchant_id')['amount'].transform('mean')

        df['amount_deviation'] = df['amount'] - df['merchant_avg_amount']

        df['transaction_count'] = df.groupby('merchant_id')['amount'].transform('count')

        features = [
            'amount',
            'transaction_hour',
            'merchant_avg_amount',
            'amount_deviation',
            'transaction_count'
        ]


        df['risk'] = model.predict(df[features])


        if hasattr(model, "predict_proba"):
            df['risk_score'] = model.predict_proba(df[features])[:, 1]


        risky = (
            df[df['risk'] == 1]
            .groupby('merchant_id')
            .agg(
                risk_count=('risk', 'count'),
                avg_risk_score=('risk_score', 'mean') if 'risk_score' in df.columns else ('risk', 'count')
            )
            .reset_index()
            .sort_values(by='risk_count', ascending=False)
            .head(5)
        )

        if risky.empty:
            return "No high-risk merchants found."

        return risky.to_string(index=False)

    except Exception as e:
        return f"Prediction Error: {str(e)}"