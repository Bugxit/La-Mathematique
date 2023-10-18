from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)



@app.route("/")
def welcome_page():
   return render_template("welcome_page.html")



@app.route("/cours")
def cours():
   return render_template("cours.html")

@app.route("/exercices")
def exercices():
   return render_template("exercices.html")



@app.route("/cours/premiere/suites_numeriques")
def cours_suites_numeriques():
    return render_template("cours_suites_numériques.html")

@app.route("/exercices/premiere/suites_numeriques")
def exercices_suites_numeriques():
    global answer_ex_1
    answer_ex_1 = randint(1,6)
    return render_template("exercices_suites_numériques.html", answer_ex_1 = answer_ex_1)

@app.route('/exercices/premiere/suites_numeriques', methods=['POST'])
def check_answers_1():
    if int(request.form['answer_ex_1']) == answer_ex_1:
        return 'Good answer !'
    else:
        return 'Wrong answer!'



@app.route("/cours/premiere/polynomes_second")
def cours_polynomes_second():
    return render_template("cours_polynomes_second.html")

@app.route("/exercices/premiere/polynomes_second")
def exercices_polynomes_second():
    return 'Comming soon !'
    #return render_template("exercices_polynomes_second.html")



@app.route("/cours/premiere/derivation")
def cours_derivation():
    return render_template("cours_derivation.html")

@app.route("/exercices/premiere/derivation")
def exercices_derivation():
    return 'Comming soon !'
    #return render_template("exercices_derivation.html")


if __name__ == "__main__":
     app.run(host='0.0.0.0')
