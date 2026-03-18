from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    #if "name" in request.args:
        #name = request.args["name"]
    #else:
        #name = "world"
    return render_template("index1.html") #when i submit the name will transport to greet.html by app.py and the URL will go from .../ to .../greet?name=x


@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", placeholder=request.form.get("name","world")) # args support get form support post
