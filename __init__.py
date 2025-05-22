from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'app web de chiffrement/déchiffrement! Utilisez /encrypt/<clé>/<valeur> ou /decrypt/<clé>/<valeur>"

@app.route('/encrypt/<string:cle>/<string:valeur>')
def encrypt_personnalise(cle, valeur):
    try:
        f = Fernet(cle.encode())
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur chiffrée : {token.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"

@app.route('/decrypt/<string:cle>/<string:valeur>')
def decrypt_personnalise(cle, valeur):
    try:
        f = Fernet(cle.encode())
        valeur_bytes = valeur.encode()
        decrypted = f.decrypt(valeur_bytes)
        return f"Valeur déchiffrée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"
      
if __name__ == "__main__":
  app.run(debug=True)
