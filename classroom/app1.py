from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", placeholder=request.form.get("name","world"))
    else:
        return render_template("index.html")
