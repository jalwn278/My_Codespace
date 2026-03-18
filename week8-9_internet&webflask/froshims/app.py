from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Football"
]

db = SQL("sqlite:///froshims.db")

#register page
@app.route("/")
def index():
    return render_template("index2.html", placeholder=SPORTS)

#delete
@app.route("/deregister",methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")

#validate students & sport
@app.route("/register",methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")

    sports = request.form.getlist("sport")
    if not sports:
        return render_template("error.html", message="Missing sports")

    for sport in sports:
        if sport not in SPORTS:
            return render_template("error.html", message="Invalid sport")

#remember students
    for sport in sports:
        db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

#confirmed
    return redirect("/registrants")

#registrants table
@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", placeholder=registrants)

