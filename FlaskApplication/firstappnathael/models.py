from flask import request
from .tools.tools import orderby

def liste_eleves(mysql,view_parent):
    """ récupère les informations nécessairent à l'affichage de la listes des élèves
     dans la base, sous la forme d'un dictionnaire"""
    order_by = orderby(request.args.get("orderby"))
    requete = f'SELECT idEleve,nom,prenom,DATE_FORMAT(dateDeNaissance, "%d/%m/%Y") FROM eleves{order_by}'
    data = mysql.request_Data_Base(requete)

    return {"titre_cols":["id","Nom","Prenom","date de naissance"],
                           "datas" : data,
                           "titre":"Listes des élèves",
                           "type":"affichage_liste",
                           "orderby":["idEleve","nom","prenom",""],
                           "view":view_parent}



def liste_profs(mysql,view_parent):
    """récupère les informations nécessairent à l'affichage de la listes des professeurs
     dans la base, sous la forme d'un dictionnaire"""
    order_by = orderby(request.args.get("orderby"))
    requete = f'SELECT idProf,nom,matiere FROM professeurs{order_by}'
    data = mysql.request_Data_Base(requete)
    return {"titre_cols": ["id", "Nom", "Matiere"],
            "datas": data,
            "titre": "Liste des Professeurs",
            "type": "affichage_liste",
            "orderby": ["idProf", "nom", "matiere"],
            "view":view_parent}

def liste_bulletins(mysql,view_parent):
    """récupère les informations nécessairent à l'affichage de la listes des bulletins
    dans la base, sous la forme d'un dictionnaire"""
    order_by = orderby(request.args.get("orderby"))
    requete = f'SELECT DISTINCT nom,prenom,email FROM eleves,notes WHERE notes.idEleve = eleves.idEleve {order_by}'
    data = mysql.request_Data_Base(requete)

    return {"titre_cols": ["Nom", "Prenom"],
            "datas": data,
            "titre": "Listes des Bulletins",
            "type": "affichage_liste",
            "orderby": ["nom", "prenom", ""],
            "view": view_parent}

# SELECT  AVG(notes.note) FROM eleves,notes WHERE notes.idEleve = eleves.idEleve and eleves.nom="TOUILLE";
# SELECT professeurs.matiere, notes.note FROM eleves,professeurs,notes WHERE notes.idEleve = eleves.idEleve and notes.idProf = professeurs.idProf and eleves.nom="TOUILLE";
def bulletin(mysql,nom=None,prenom=None):
    """récupère les informations nécessairent à l'affichage d'un bulletin
    dans la base, sous la forme d'un dictionnaire"""
    order_by = orderby(request.args.get("orderby"))

    requete = f"SELECT AVG(notes.note) FROM eleves,notes WHERE notes.idEleve = eleves.idEleve and eleves.nom='{nom}' and eleves.prenom='{prenom}'"
    moyenne = mysql.request_Data_Base(requete)
    if moyenne[0][0] is None:
        moyenne = ""
        notes = ""
    else :
        requete2 = f"SELECT professeurs.matiere, notes.note FROM eleves,professeurs,notes WHERE notes.idEleve = eleves.idEleve and notes.idProf = professeurs.idProf and eleves.nom='{nom}' and eleves.prenom='{prenom}'"
        notes = mysql.request_Data_Base(requete2)
        moyenne = f"{moyenne[0][0]:2.2f}"
    return {"titre_cols": ["Matiere", "Notes"],
            "moyenne" : moyenne,
            "notes" : notes,
            "titre" : "Matières & Notes",
            "type" : "affichage_liste"}