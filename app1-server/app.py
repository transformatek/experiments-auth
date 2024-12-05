from flask import Flask, redirect, url_for, session, jsonify
from flask_appbuilder import AppBuilder, SQLA
from authlib.integrations.flask_client import OAuth

# Initialisation de l'application Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'af2697619faa0487be4ae3d6823ec9788a1e7b966834d6307f1e7b44cdfe6d84'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

# Configuration OAuth avec Authlib
oauth = OAuth(app)

# Enregistrement du client Keycloak
keycloak = oauth.register(
    name='keycloak',
    client_id='app-client1',  # ID du client Keycloak
    client_secret='your-client-secret',  # Secret du client
    server_metadata_url='http://localhost:8080/realms/myrealm/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid profile email'},
)

# Route principale
@app.route('/')
def index():
    return 'Bienvenue sur l\'application Flask avec OAuth2 et Keycloak! <a href="/login">Connexion</a>'

# Route de connexion
@app.route('/login')
def login():
    redirect_uri = url_for('auth_callback', _external=True)
    return keycloak.authorize_redirect(redirect_uri)

# Callback après connexion
@app.route('/callback')
def auth_callback():
    token = keycloak.authorize_access_token()
    if not token:
        return 'Erreur de connexion', 401
    user_info = keycloak.parse_id_token(token)
    session['user'] = user_info
    return jsonify(user_info)

# Route pour récupérer les données utilisateur
@app.route('/user')
def get_user():
    user = session.get('user')
    if not user:
        return jsonify({'error': 'Non connecté'}), 401
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
