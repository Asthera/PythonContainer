from flask import Flask, request, jsonify
import torch

app = Flask(__name__)


@app.route("/multiply", methods=["POST"])
def multiply_matrices():
    data = request.json
    try:
        # Extract matrices from the request
        matrix_a = torch.tensor(data['matrix_a'])
        matrix_b = torch.tensor(data['matrix_b'])

        # Perform matrix multiplication
        result = torch.matmul(matrix_a, matrix_b).tolist()

        # Return the result
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
