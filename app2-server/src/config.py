from datetime import timedelta
import os
from flask_appbuilder.security.manager import AUTH_OAUTH

basedir = os.path.abspath(os.path.dirname(__file__))

# Secret key pour l'application
SECRET_KEY = "abcdefghijklmnopqrtu"

# Configuration de la base de données
SQLLITE_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", SQLLITE_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuration JWT
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

# Authentification avec OAuth
AUTH_TYPE = AUTH_OAUTH

# Rôles par défaut
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"


AUTH_USER_REGISTRATION = True
# Configuration OAuth pour Keycloak
OAUTH_PROVIDERS = [
    {
        'name': 'keycloak',
        'token_key': 'access_token',
        'icon': 'fa-key',
        'remote_app': {
            'client_id': 'app2-client',
            'client_secret': 'RucCUHrjR9zutmQD04p6dWqDH4QcA18R',
            'api_base_url': 'http://localhost:8080/realms/Authentification/protocol/openid-connect/',
            'client_kwargs': {'scope': 'openid email profile'},
            'access_token_url': 'http://localhost:8080/realms/Authentification/protocol/openid-connect/token',
            'authorize_url': 'http://localhost:8080/realms/Authentification/protocol/openid-connect/auth',
            'userinfo_endpoint': 'http://localhost:8080/realms/Authentification/protocol/openid-connect/userinfo',
            'redirect_uri': 'http://localhost:5000/callback',
        },
    }
]
