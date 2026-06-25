from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Simple ML-style logic model (for deployment testing)
def predict_loan(income, loan_amount, credit_score, employed):

    score = 0

    if income > 3000:
        score += 1
    if loan_amount < 5000:
        score += 1
    if credit_score > 650:
        score += 1
    if employed == 1:
        score += 1

    if score >= 3:
        return "Approved"
    else:
        return "Rejected"

@app.route("/")
def home():
    return "Loan Eligibility API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    result = predict_loan(
        data["income"],
        data["loan_amount"],
        data["credit_score"],
        data["employed"]
    )

    return jsonify({"decision": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
