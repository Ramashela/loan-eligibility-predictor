from flask import Flask, request
import os

app = Flask(__name__)

def predict_loan(income, loan_amount, credit_score, employed):

    score = 0

    if income > 3000:
        score += 1

    if loan_amount < 5000:
        score += 1

    if credit_score > 650:
        score += 1

    if employed == "Yes":
        score += 1

    if score >= 3:
        return "✅ Loan Approved"
    else:
        return "❌ Loan Rejected"


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        income = float(request.form["income"])
        loan_amount = float(request.form["loan_amount"])
        credit_score = float(request.form["credit_score"])
        employed = request.form["employed"]

        result = predict_loan(
            income,
            loan_amount,
            credit_score,
            employed
        )

    return f"""
    <html>
    <head>
        <title>Loan Eligibility Predictor</title>
        <style>
            body {{
                font-family: Arial;
                max-width: 600px;
                margin: 40px auto;
                padding: 20px;
            }}

            input, select {{
                width: 100%;
                padding: 10px;
                margin: 8px 0;
            }}

            button {{
                width: 100%;
                padding: 12px;
                cursor: pointer;
            }}

            h1 {{
                text-align: center;
            }}

            .result {{
                margin-top: 20px;
                font-size: 24px;
                text-align: center;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

        <h1>🏦 Loan Eligibility Predictor</h1>

        <form method
