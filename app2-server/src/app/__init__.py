from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from sqlalchemy import MetaData
from flask_migrate import Migrate

from flask import g
from flask_appbuilder.security.sqla.manager import SecurityManager

class CustomSsoSecurityManager(SecurityManager):
    def oauth_user_info(self, provider, response=None):  # noqa: ARG002
        me = self.appbuilder.sm.oauth_remotes[provider].get("openid-connect/userinfo")
        me.raise_for_status()
        data = me.json()
        return {
            "username": data.get("preferred_username", ""),
            "first_name": data.get("given_name", ""),
            "last_name": data.get("family_name", ""),
            "email": data.get("email", ""),
            "role_keys": data.get("role_keys", []),
        }

    def load_user_jwt(self, _jwt_header, jwt_data):
        username = jwt_data["preferred_username"]
        user = self.find_user(username=username)
        if user.is_active:
            # Set flask g.user to JWT user, we can't do it on before request
            g.user = user
            return user
        return None

app = Flask(__name__)
app.config.from_object('config')

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
db = SQLA(app, metadata=metadata)

migrate = Migrate(app, db, render_as_batch=True)

appbuilder = AppBuilder(app, db.session, security_manager_class=CustomSsoSecurityManager)
# appbuilder = AppBuilder(app, db.session)


# Register views

if __name__ == "__main__":
    app.run(debug=True)

from . import models
from . import views
from . import controllers