from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                                                                                                                                       
app = Flask(__name__)

CLE_FERNET = "vbI_R_JlMaSxrQHHZYYEw0q_Hs-jVaTAmH5cbL0vDpY="

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>App de Chiffrement/Déchiffrement</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h2 class="mb-4 text-center">Chiffrement / Déchiffrement</h2>
        <form method="POST">
            <div class="mb-3">
                <label for="text" class="form-label">Texte</label>
                <input type="text" class="form-control" name="text" required>
            </div>
            <div class="d-flex gap-2">
                <button type="submit" name="action" value="encrypt" class="btn btn-primary w-50">🔐 Chiffrer</button>
                <button type="submit" name="action" value="decrypt" class="btn btn-success w-50">🔓 Déchiffrer</button>
            </div>
        </form>
        {% if result %}
        <div class="alert alert-info mt-4">
            <strong>Résultat :</strong><br> {{ result }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            texte = request.form['text']
            action = request.form['action']
            fernet = Fernet(CLE_FERNET.encode())

            if action == 'encrypt':
                result = fernet.encrypt(texte.encode()).decode()
            elif action == 'decrypt':
                result = fernet.decrypt(texte.encode()).decode()
        except Exception as e:
            result = f"Erreur : {str(e)}"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
