from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    phnumber = request.form["phnumber"]
    village = request.form["village"]

    return f"Name: {name}, Phone: {phnumber}, Village: {village}"

if __name__ == "__main__":
    app.run(debug=True)	
