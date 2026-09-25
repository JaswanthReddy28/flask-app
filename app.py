from flask import Flask, jsonify, request, abort
 
app = Flask(__name__)
 
# --- Arithmetic Services (Using Query Parameters) ---
 
@app.route("/")
def hello():
    # How to call: http://127.0.0.1:5000/
    return "Hello, CI/CD! This is a simple REST API."
 
 
@app.route("/add", methods=["GET"])
def add_numbers():
    """Calculates a + b using query parameters."""
    # How to call: http://127.0.0.1:5000/add?a=7&b=6
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Invalid input: 'a' and 'b' must be integers"}), 400
 
if __name__ == "__main__":
    app.run(debug=True)
 