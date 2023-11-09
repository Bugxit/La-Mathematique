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
    global suites_numeriques_answer_1, suites_numeriques_answer_2
    suites_numeriques_answer_1, suites_numeriques_answer_2 = randint(1,6), randint(1,6)
    return render_template("exercices_suites_numériques.html", 
                           answer_ex_1 = suites_numeriques_answer_1, 
                           answer_ex_2 = suites_numeriques_answer_2)

@app.route('/exercices/premiere/suites_numeriques', methods=['POST'])
def check_answers_2():
    if request.form['answer_ex_1'] != "" and int(request.form['answer_ex_1']) == suites_numeriques_answer_1:
        suites_numeriques_gb_answer_1 = "bel et bien"
    else:
        suites_numeriques_gb_answer_1 = "cepedant"
    if request.form['answer_ex_2'] != "":
        if int(request.form['answer_ex_2']) == suites_numeriques_answer_2:
            suites_numeriques_gb_answer_2 = "bel et bien"
        else:
            suites_numeriques_gb_answer_2 = "cepedant"
    else:
        suites_numeriques_gb_answer_2 = "ta pas répondu... triste"
    return render_template("answers_exercices_suites_numeriques.html",
                           gb_answer_ex_1 = suites_numeriques_gb_answer_1,
                           gb_answer_ex_2 = suites_numeriques_gb_answer_2, 
                           answer_ex_1 = suites_numeriques_answer_1, 
                           answer_ex_2 = suites_numeriques_answer_2,
                           sent_answer_ex_1 = int(request.form['answer_ex_1']),
                           sent_answer_ex_2 = request.form['answer_ex_2'])

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
     app.run(host='0.0.0.0', port="7000")
