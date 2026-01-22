from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    username = "John"
    highlights = [
        "Latest Gym Equipment",
        "Certified Trainers",
        "Friendly Environment",
        "Affordable Membership"
    ]
    return render_template("home.html", username=username, highlights=highlights)

@app.route("/about")
def about():
    mission = "To help people live a healthy and active lifestyle"
    facilities = [
        "Cardio Area",
        "Weight Training",
        "Personal Training",
        "Group Classes"
    ]
    return render_template("about.html", mission=mission, facilities=facilities)

@app.route("/membership")
def membership():
    plans = [
        {"name": "Basic", "price": "Rs. 2000 / month"},
        {"name": "Standard", "price": "Rs. 3500 / month"},
        {"name": "Premium", "price": "Rs. 5000 / month"}
    ]
    return render_template("membership.html", plans=plans)

if __name__ == "__main__":
    app.run(debug=True)
