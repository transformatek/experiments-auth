
# Setup the Identity provider and describe

## Step 1: Running the Identity Provider

### 1.1 Install Docker (if not installed)
- Si Docker n'est pas installé, suivez les instructions sur le site officiel de Docker pour l'installer.

### 1.2 Start Keycloak with Docker

Créez un fichier `docker-compose.yml` pour lancer Keycloak dans un conteneur Docker.

```bash
keycloak_web:
    image: quay.io/keycloak/keycloak:23.0.7
    container_name: keycloak_web
    environment:
      KC_DB: postgres
      KC_DB_URL: jdbc:postgresql://keycloakdb:5432/keycloak
      KC_DB_USERNAME: keycloak
      KC_DB_PASSWORD: password

      KC_HOSTNAME: keycloack.local
      KC_HOSTNAME_PORT: 8080
      KC_HOSTNAME_STRICT: false
      KC_HOSTNAME_STRICT_HTTPS: false

      KC_LOG_LEVEL: info
      KC_METRICS_ENABLED: true
      KC_HEALTH_ENABLED: true
      KEYCLOAK_ADMIN: admin
      KEYCLOAK_ADMIN_PASSWORD: admin
    command: start-dev
    depends_on:
      - keycloakdb
    ports:
      - 8080:8080

  keycloakdb:
    image: postgres:15
    volumes:
      - postgres-data-keycloak:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: keycloak
      POSTGRES_USER: keycloak
      POSTGRES_PASSWORD: password

volumes:
  postgres-data:
  postgres-data-keycloak:
```
- Accédez à Keycloak sur http://localhost:8080.

## Step 2: Create a Realm/Project in the Identity Provider

### 2.1 Keycloak: Create a Realm
1. **Login to the Admin Console**:
   - Open your browser and navigate to [http://localhost:8080/auth/admin/](http://localhost:8080/auth/admin/).
   - Use the credentials `admin/admin` (or those you have set in the Docker configuration).
   
2. **Create a Realm**:
   - After logging in, click on **Realms** in the left sidebar.
   - Click on **Add realm**.
   - Provide a name for your realm (e.g., `my-app-realm`) and click **Create**.
   - A realm in Keycloak is a logical grouping of applications, users, and roles. Each realm is isolated from others.

3. **Configure the Realm**:
   - In the realm settings, you can adjust configurations like login themes, password policies, etc.
   - For instance, you can select the **Login Theme** to customize the appearance of the login page for your users.



## Step 3: Configure Clients for Backend and Frontend

### 3.1 Backend Configuration (Flask Example)

#### 3.1.1 Create a Client in Keycloak for Flask
1. **Add a Client**:
   - In the Keycloak admin console, select your realm (`my-app-realm`).
   - Click on **Clients** in the left sidebar, then click **Create**.
   - Fill in the following fields:
     - **Client ID**: `app1-client`
     - **Client Protocol**: OpenID Connect
     - **Root URL**: `http://localhost:5000` (adjust if your backend runs on a different port).
   
2. **Set Redirect URIs**:
   - In the **Valid Redirect URIs** field, add:
     - `http://localhost:5000/*`
   - This will allow the Flask backend to accept redirects after authentication.
   
3. **Save the Client**:
   - Click **Save** to create the client configuration.

4. **Retrieve the Client Secret**:
   - Go to the **Credentials** tab of the client and copy the **Client Secret**. You will need this to configure Flask.

#### 3.1.2 Backend Configuration (Flask)

In your Flask app, you'll need to install the `Flask-OIDC` library and configure it to communicate with Keycloak.

```bash
pip install Flask-OIDC
```
Ensuite, configurez votre application Flask pour qu'elle communique avec Keycloak.

Dans votre fichier de configuration, par exemple **config.py**, ajoutez les paramètres suivants :

```bash
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
            'redirect_uri': [
            "http://localhost:7000/*"
        ],
        },
]
```

## Step 4: Configure a Client for NextJS (Frontend)

### 4.1. **Create a client for the frontend** :
by adding a Client ID (for example, `nextjs-frontend`) and the Root URL of your NextJS application (e.g., `http://localhost:3000`).
### 4.2. **Add appropriate redirect URIs** :
to allow redirection after authentication (e.g., `http://localhost:3000/*`).


## Step 5: Configure Authentication in NextJS (Frontend)

### 5.1 Install NextAuth

To manage authentication with Keycloak in NextJS, install `next-auth` by running the following command:

```bash
npm install next-auth
```
