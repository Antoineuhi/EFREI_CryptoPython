from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #changing
                                                                                                                                                                                                                                                       
app = Flask(__name__)

key = Fernet.generate_key()
f = Fernet(key)
@app.route('/')
def home():
    return "Bienvenue ! Utilisez /encrypt/<clé>/<valeur> ou /decrypt/<clé>/<valeur>"

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
@app.route('/encrypt/<string:cle>/<string:valeur>')
def encrypt_personnalise(cle, valeur):
    try:
        f = Fernet(cle.encode())
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"

@app.route('/decrypt/<string:valeur>')
def decryptage(valeur):
@app.route('/decrypt/<string:cle>/<string:valeur>')
def decrypt_personnalise(cle, valeur):
    try:
        f = Fernet(cle.encode())
        valeur_bytes = valeur.encode()
        decrypted = f.decrypt(valeur_bytes)
        return f"Valeur décryptée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"
        return f"Erreur : {str(e)}"

if __name__ == "__main__":
  app.run(debug=True)
