

from flask import Flask, render_template, url_for, request
from firstappnathael.tools.mysqlquery import MysqlQuery
from firstappnathael.tools.tools import nom_fonction_en_cours
from .models import liste_eleves, liste_profs, liste_bulletins, bulletin

#Création de l'application Flask
app = Flask(__name__)

#Chargement du fichier de configuration config.py (MySQL,....)
app.config.from_object("config")

#Creation de l'objet mysql pour gérer le dialogue avec la base de données
mysql = MysqlQuery(app)

@app.route("/")
def home():
    return render_template("pages/index.html",menu = app.config.get("MENU"), menu_actif=1,titre = "Accueil")

@app.route("/liste_eleve")
def affiche_liste_eleves():
    return render_template("pages/affichage_liste.html",menu = app.config.get("MENU"), menu_actif=2, **liste_eleves(mysql,nom_fonction_en_cours()))

@app.route("/liste_professeur")
def affiche_liste_profs():
   return render_template("pages/affichage_prof.html",menu = app.config.get("MENU"), menu_actif=3,**liste_profs(mysql,nom_fonction_en_cours()))

@app.route("/liste_bulletins")
def affiche_liste_bulletins():

    return render_template("pages/liste_bulletin.html", menu = app.config.get("MENU"), menu_actif=4, **liste_bulletins(mysql, nom_fonction_en_cours()))


@app.route("/bulletin", methods=["GET", "POST"])
@app.route("/bulletin/pages/<int:page>" , methods=["GET", "POST"])
def affiche_bulletin():
    if request.method == "POST":
        nom = request.form.get("nom")
        prenom = request.form.get("prenom")
    else :
        nom = request.args.get("nom")
        prenom = request.args.get("prenom")

    return render_template("pages/bulletin.html",menu = app.config.get("MENU"), menu_actif=5, **bulletin(mysql, nom, prenom))

@app.route("/recherche")
def recherche():
    return render_template("pages/recherche.html", menu = app.config.get("MENU"), menu_actif=6, titre = "Recherche")


if __name__ == "__main__":
    app.run()