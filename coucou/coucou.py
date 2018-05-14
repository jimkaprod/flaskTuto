#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request
from PIL import Image
# from io import StringIO
from io import BytesIO
from flask import make_response, abort, redirect, url_for

app = Flask(__name__)

@app.route('/coucou')
def dire_coucou():
  return 'Coucou !'


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'GET':
    #afficher forms
    return 'FORMULAIRE'
  else:
    #traiter les données recues
    #Afficher merci
    return 'MERCI'

@app.route('/bonjour/la')
@app.route('/ici')
@app.route('/la')
def ici():
  abort(500)
  return 'Le chemin racine est : ' + request.path


@app.route('/discussion')
@app.route('/discussion/page/<int:num_page>')
def mon_chat(num_page = 1):
  premier_msg = 1 + 50 * (num_page-1)
  dernier_msg = premier_msg + 50
  return 'affichage des messages de {} à {}'.format(premier_msg, dernier_msg)

@app.route('/afficher')
@app.route('/afficher/mon_nom_est_<nom>_et_mon_prenom_est_<prenom>')
def mon_minou(nom = None, prenom=None):
  if nom is None or prenom is None:
    return "Entrez votre nom et votre prenom dans l'url"
  return 'Vous vous appelez {} {}'.format(nom, prenom)

@app.route('/image')
def genere_image():
  mon_image = BytesIO()
  Image.new("RGB", (300,300), "#92C41D").save(mon_image, 'BMP')
  reponse = make_response(mon_image.getvalue())
  reponse.mimetype = "image/bmp"  # à la place de "text/html"
  return reponse

@app.route('/404')
def page_non_trouvee():
  return "Cette page devrait vous avoir renvoyé une erreur 404",404

@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
  return "Ma super jolie page {}".format(error.code),error.code


@app.route('/profil')
def profil():
    utilisateur_non_identifie=0
    if utilisateur_non_identifie:
      return redirect(url_for('page_de_login'))
    return "Vous êtes bien identifié, voici la page demandée : ..."


@app.route('/login')
def page_de_login():
  return "page login"

if __name__ == '__main__':
  app.debug =True
  app.run()

