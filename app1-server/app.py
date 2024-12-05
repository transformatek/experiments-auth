from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

# Initialisation de l'application Flask
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')  # Clé secrète pour Flask

# Initialisation de l'extension OAuth
oauth = OAuth(app)

# Enregistrement du client Keycloak
keycloak = oauth.register(
    name='keycloak',
    client_id='your-client-id',  # Remplacez par votre client_id Keycloak
    client_secret='your-client-secret',  # Remplacez par votre client_secret Keycloak
    server_metadata_url='http://localhost:8080/realms/your-realm/.well-known/openid-configuration',  # URL de configuration de Keycloak
    client_kwargs={'scope': 'openid profile email'}
)

@app.route('/')
def home():
    return 'Bienvenue sur l\'application Flask avec Keycloak! <a href="/login">Se connecter</a>'

@app.route('/login')
def login():
    # Redirection vers Keycloak pour l'authentification
    redirect_uri = url_for('auth', _external=True)
    return keycloak.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():
    # Récupération du token d'accès après redirection de Keycloak
    token = keycloak.authorize_access_token()
    user = keycloak.parse_id_token(token)
    
    # Enregistrement des informations utilisateur dans la session
    session['user'] = user
    return redirect('/profile')

@app.route('/profile')
def profile():
    user = session.get('user')
    if user:
        return f'Bonjour {user["name"]}! <br><a href="/logout">Déconnexion</a>'
    return 'Utilisateur non connecté!'

@app.route('/logout')
def logout():
    session.clear()  # Effacer la session de l'utilisateur
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
