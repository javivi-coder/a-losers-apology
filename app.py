from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = "jwe25627411"

@app.route("/", methods=["GET", "POST"])
def index():

    if "step" not in session:
        session["step"] = 1
        session["no_count"] = 0

    if request.method == "POST":

       if request.form.get("action") == "next":
           session["step"] += 1
       elif request.form.get("action") == "no":
           session["no_count"] += 1
       elif request.form.get("action") == "yes":
           session["step"] = 5
    return render_template(
        "index.html",
        step=session["step"],
        no_count=session["no_count"]
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)