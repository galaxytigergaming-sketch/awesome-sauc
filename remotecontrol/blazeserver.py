from flask import Flask, request, jsonify

app = Flask(__name__)

latest_command = "none"


@app.route("/send", methods=["POST"])
def send():
    global latest_command

    data = request.json
    latest_command = data["command"]

    print("Command:", latest_command)

    return jsonify({
        "status": "ok"
    })


@app.route("/get", methods=["GET"])
def get():
    return jsonify({
        "command": latest_command
    })


@app.route("/")
def home():
    return "Quantum Remote Server Online"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )