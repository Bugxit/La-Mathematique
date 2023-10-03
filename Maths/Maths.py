from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome_page():
   return render_template("welcome_page.html")

@app.route("/suites_numériques")
def goodbye():
    return render_template("suites_numériques.html")


if __name__ == "__main__":
    app.run(port=777)