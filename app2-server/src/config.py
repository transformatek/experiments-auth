import os
from datetime import timedelta
from flask_appbuilder.security.manager import AUTH_OAUTH

# App secret key
SECRET_KEY = "abcdefghijklmnopqrtu"

# SQLAlchemy configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'app.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Authentication type (use modern OAuth)
AUTH_TYPE = AUTH_OAUTH

# OAuth configuration for Keycloak
OAUTH_PROVIDERS = [
    {
        'name': 'keycloak',
        'token_key': 'access_token',
        'icon': 'fa-address-card',
        'remote_app': {
            'client_id': 'app2',
            'client_secret': 'ZrgcL85ztes8kNVd8fhSO6EAgd93J9kq',
            'api_base_url': 'http://localhost:8080/realms/myrealm/protocol/openid-connect',
            'access_token_url': 'http://localhost:8080/realms/myrealm/protocol/openid-connect/token',
            'authorize_url': 'http://localhost:8080/realms/myrealm/protocol/openid-connect/auth',
            'client_kwargs': {'scope': 'openid email profile roles'},
        },
    }
]

# Roles configuration
AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"

# CSRF Protection
CSRF_ENABLED = True

# JWT Token expiration
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

# Languages
LANGUAGES = {
    "en": {"flag": "gb", "name": "English"},
    "fr": {"flag": "fr", "name": "French"},
}
# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role for all users
AUTH_USER_REGISTRATION_ROLE = "Admin"