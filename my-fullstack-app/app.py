from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins

@app.route("/")
def hello_world():
    return "Mijn leven is perfect! "

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to a free port
