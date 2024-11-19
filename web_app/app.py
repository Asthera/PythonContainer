from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL of the PyTorch container API
PYTORCH_API_URL = "http://pytorch-container:5001/multiply"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get matrices from the form data
        matrix_a = [[int(request.form["a1"]), int(request.form["a2"])],
                    [int(request.form["b1"]), int(request.form["b2"])]]
        matrix_b = [[int(request.form["c1"]), int(request.form["c2"])],
                    [int(request.form["d1"]), int(request.form["d2"])]]

        # Send matrices to the PyTorch API for multiplication
        response = requests.post(PYTORCH_API_URL, json={
            "matrix_a": matrix_a,
            "matrix_b": matrix_b
        })

        if response.status_code == 200:
            result = response.json().get("result")
            return render_template("index.html", result=result)
        else:
            return render_template("index.html", error="Error multiplying matrices")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
