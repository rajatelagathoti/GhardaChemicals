from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form")
def farm_form():
    return render_template("form.html")


@app.route("/recommendations", methods=["POST"])
def recommendations():
    farmer_name = request.form["farmer_name"]
    location = request.form["location"]
    soil_type = request.form["soil_type"]
    crop = request.form["crop"]
    water_source = request.form["water_source"]

    tips = [
        "Use mulch or cover crops to reduce soil erosion.",
        "Plant trees and maintain windbreaks around fields.",
        "Adopt drip irrigation to conserve water.",
        "Practice crop rotation to improve soil fertility."
    ]

    if soil_type == "sandy":
        tips.append("Add compost or organic matter to improve water retention.")

    return render_template(
        "result.html",
        farmer_name=farmer_name,
        location=location,
        soil_type=soil_type,
        crop=crop,
        water_source=water_source,
        recommendations=tips
    )


if __name__ == "__main__":
    app.run(debug=True)
