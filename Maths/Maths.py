from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)


#Starting pages
@app.route("/")
def welcome_page():
   return render_template("welcome_page.html")

@app.route("/cours")
def cours():
   return render_template("cours.html")

@app.route("/exercices")
def exercices():
   return render_template("exercices.html")

#suites_numeriques
@app.route("/cours/premiere/suites_numeriques")
def cours_suites_numeriques():
    return render_template("cours_suites_numériques.html")

@app.route("/exercices/premiere/suites_numeriques")
def exercices_suites_numeriques():
    global CorrectAnswerQuestion1_suites_numeriques, CorrectAnswerQuestion2_suites_numeriques
    CorrectAnswerQuestion1_suites_numeriques, CorrectAnswerQuestion2_suites_numeriques = randint(1,16), randint(1,16)
    return render_template(
                           "exercices_suites_numériques.html", 
                           CorrectAnswerQuestion1 = CorrectAnswerQuestion1_suites_numeriques, 
                           CorrectAnswerQuestion2 = CorrectAnswerQuestion2_suites_numeriques
                           )

@app.route('/exercices/premiere/suites_numeriques', methods=['POST'])
def check_answers_suites_numeriques():
    DidNotAnswerQuestion1_1, DidNotAnswerQuestion1_2, DidNotAnswerQuestion2_1, DidNotAnswerQuestion2_2 = "", "", "", ""

    #Question 1 :
    if request.form['POST_UserAnswerQuestion1_suites_numeriques'] == "":
        DidNotAnswerQuestion1_1, DidNotAnswerQuestion1_2 = "n'", "pas"
        TrueOrFalseQuestion1 = ""
    elif request.form['POST_UserAnswerQuestion1_suites_numeriques'] == str(CorrectAnswerQuestion1_suites_numeriques):
        TrueOrFalseQuestion1 = "bel et bien"
    else:
        TrueOrFalseQuestion1 = "cependant"

    #Question 2 :
    if request.form['POST_UserAnswerQuestion2_suites_numeriques'] == "":
        DidNotAnswerQuestion2_1, DidNotAnswerQuestion2_2 = "n'", "pas"
        TrueOrFalseQuestion2 = ""
    elif request.form['POST_UserAnswerQuestion2_suites_numeriques'] == str(CorrectAnswerQuestion2_suites_numeriques):
        TrueOrFalseQuestion2 = "bel et bien"
    else:
        TrueOrFalseQuestion2 = "cependant"

    #Puis :
    return render_template(
                           "answers_exercices_suites_numeriques.html",
                           TrueOrFalseQuestion1 = TrueOrFalseQuestion1,
                           TrueOrFalseQuestion2 = TrueOrFalseQuestion2, 
                           CorrectAnswerQuestion1 = CorrectAnswerQuestion1_suites_numeriques, 
                           CorrectAnswerQuestion2 = CorrectAnswerQuestion2_suites_numeriques,
                           UserAnswerQuestion1 = request.form['POST_UserAnswerQuestion1_suites_numeriques'],
                           UserAnswerQuestion2 = request.form['POST_UserAnswerQuestion2_suites_numeriques'],
                           DidNotAnswerQuestion1_1 = DidNotAnswerQuestion1_1,
                           DidNotAnswerQuestion1_2 = DidNotAnswerQuestion1_2,
                           DidNotAnswerQuestion2_1 = DidNotAnswerQuestion2_1,
                           DidNotAnswerQuestion2_2 = DidNotAnswerQuestion2_2
                           ) 

#polynomes_second
@app.route("/cours/premiere/polynomes_second")
def cours_polynomes_second():
    return render_template("cours_polynomes_second.html")

@app.route("/exercices/premiere/polynomes_second")
def exercices_polynomes_second():
    return 'Comming soon !'
    #return render_template("exercices_polynomes_second.html")

#nombre_derive_fonction_derivee
@app.route("/cours/premiere/nombre_derive_fonction_derivee")
def cours_derivation():
    return render_template("cours_derivation.html")

@app.route("/exercices/premiere/nombre_derive_fonction_derivee")
def exercices_derivation():
    return 'Comming soon !'
    #return render_template("exercices_derivation.html")
    
#applications_derivation
@app.route("/cours/premiere/application_derivation")
def cours_application_derivation():
    return render_template("application_derivation.html")

#fonction_exponentielle
@app.route("/cours/premiere/fonction_exponentielle")
def cours_fonction_exponentielle():
    return render_template("fonction_exponentielle.html")

if __name__ == "__main__":
     app.run(host='0.0.0.0', port="5000")
