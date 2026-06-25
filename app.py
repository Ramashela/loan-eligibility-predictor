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
        return "Loan Approved"
    else:
        return "Loan Rejected"


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

    html = """
    <html>
    <head>
        <title>Loan Eligibility Predictor</title>
    </head>
    <body>
        <h1>Loan Eligibility Predictor</h1>

        <form method="post">

            <p>Monthly Income</p>
            <input type="number" name="income" required>

            <p>Loan Amount</p>
            <input type="number" name="loan_amount" required>

            <p>Credit Score</p>
            <input type="number" name="credit_score" required>

            <p>Employed?</p>
            <select name="employed">
                <option>Yes</option>
                <option>No</option>
            </select>

            <br><br>

            <button type="submit">Predict</button>

        </form>

        <h2>RESULT_PLACEHOLDER</h2>

    </body>
    </html>
    """

    return html.replace("RESULT_PLACEHOLDER", result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
