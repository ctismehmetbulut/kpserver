from flask import Flask
from flask_sock import Sock  # Import Sock from flask_sock for WebSocket support

app = Flask(__name__)
sock = Sock(app)  # Initialize Sock with the Flask app

# Define a WebSocket route
@sock.route('/reverse')
def reverse(ws):
    while True:
        text = ws.receive()
        ws.send(text[::-1])

# Optional: A regular HTTP route if needed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
