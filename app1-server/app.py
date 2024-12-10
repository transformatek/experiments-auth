from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

# Initialisation de l'application Flask
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key') 

# Initialisation de l'extension OAuth
oauth = OAuth(app)

# Enregistrement du client Keycloak
keycloak = oauth.register(
    name='keycloak',
    client_id='app2-client',  
    client_secret='RucCUHrjR9zutmQD04p6dWqDH4QcA18R', 
    server_metadata_url='http://localhost:8080/realms/Authentification/.well-known/openid-configuration', 
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
@app.route('/callback')
def callback():
    try:
        # Récupérer le token d'accès après la redirection de Keycloak
        token = keycloak.authorize_access_token()
        user_info = keycloak.parse_id_token(token)

        # Stocker les informations utilisateur dans la session
        session['user'] = user_info
        return redirect('/profile')
    except Exception as e:
        return f"Erreur d'authentification: {str(e)}"

@app.route('/logout')
def logout():
    session.clear() 
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)






