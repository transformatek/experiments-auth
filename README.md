# Experiments-auth
Experiments different authentication providers

## User Story
We have two 02 applications, developed using Python/Flask and NextJS. We want to deleagte the Authentication and Authorization to an Identity Provider like Keycloack or Authentik Supabase Auth.
- [ ] The user shouldbe able to access both applications using a single sign on (SSO),
- [ ] Sign-on page must be customized to Owner theme,
- [ ] The user should be able to connect using social mdia like Facebook or LinkedIn.
- [ ] The user should have access to his data only (not all users data),

## Steps 
- [ ] Add an MD file with a list of Open source Identity Providers,
- [ ] Create a starter apps (backend/frontend) named app1 and app 2, each running in a different port (ex 5000/7000 | 3000/4000), 
- [ ] Setup the Identity provider and describe the setup steps in an MD file in `docs` folder,
- [ ] Setup the authentication system in both frontend and backend,
- [ ] Create fake model/view/Api for testing the backend,
- [ ] Create a React Page that make the calls to the Api and get user data to test the frontend,
- [ ] Add Identity Providers comparison (Pros, Cons) to the above MD file.

# Requirements 
- [ ] Test each Identity provider in a different branch,
- [ ] Use devContainer extension to hanlde developement environement.



# Open Source Identity Providers

## Keycloak
- **Description**: Keycloak is an open-source identity and access management solution that provides centralized authentication and authorization for applications and services. It supports Single Sign-On (SSO), multi-factor authentication (MFA), and standard protocols like OAuth2, OpenID Connect, and SAML. Keycloak integrates with external systems like LDAP and Active Directory. It offers a user-friendly admin interface for managing users and permissions.
- **Advantages**:
  - Highly customizable.
  - User, group, and role management.
  - Supports social authentication (Google, Facebook, etc.).
- **Disadvantages**:
  - Steep learning curve.
  - Can be heavy for small projects.

## Authentik
- **Description**: Authentik is a secure Identity Provider (IdP) and Single Sign-On (SSO) solution designed for flexibility and versatility. It allows administrators to manage user authentication across various environments and supports major protocols like OAuth2, SAML, LDAP, and SCIM. With features for user profile management and recovery, it integrates easily into existing tech stacks. Authentik offers both an open-source version and an enterprise version with additional support and features.
- **Advantages**:
  - Easy to configure.
  - Lightweight and fast.
- **Disadvantages**:
  - Fewer advanced features.
  - Smaller community.

## Supabase Auth
- **Description**: Supabase Auth is an open-source authentication solution that provides secure sign-up, login, and user management for web and mobile applications. It supports authentication via email, social logins, and third-party providers like OAuth. Supabase Auth is integrated with the Supabase platform, making it easy to set up and manage. It offers features like multi-factor authentication (MFA) and session management.
- **Advantages**:
  - Simple to set up.
  - Integration with the Supabase database.
- **Disadvantages**:
  - Less flexible for complex requirements.


## Links

### 1. Research and Documentation 
  - 📄 [Keycloak Documentation](https://www.keycloak.org/documentation)
  - 📄 [Authentik Documentation](https://goauthentik.io/docs)
  - 📄 [Supabase Auth Documentation](https://supabase.com/docs/guides/auth)
  - 📄 [Supabase Auth /nextjs Documentation ](https://supabase.com/docs/guides/auth/quickstarts/nextjs)
  - 📄 [NextAuth.js Documentation](https://next-auth.js.org/providers/keycloak)

# Setup Identity Provider for Single Sign-On (SSO)

## Prerequisites

- **Docker**: Utilisé pour déployer et exécuter le fournisseur d'identité (par exemple, Keycloak).
- **Flask**: Framework backend pour Python.
- **NextJS**: Framework frontend pour React.
- **Fournisseur d'Identité**: Choisissez un fournisseur comme Keycloak, Authentik, ou Supabase Auth.
- **Environnement de développement**: Installez les outils nécessaires tels que Node.js, Python, et Docker.

## Step 1: Running the Identity Provider


### 1.1 Install Docker (if not installed)
- Si Docker n'est pas installé, suivez les instructions sur le site officiel de Docker pour l'installer.

### 1.2 Start Keycloak with Docker

Créez un fichier `docker-compose.yml` pour lancer Keycloak dans un conteneur Docker.

keycloak_web:
    image: quay.io/keycloak/keycloak:23.0.7
    container_name: keycloak_web
    environment:
      KC_DB: postgres
      KC_DB_URL: jdbc:postgresql://keycloakdb:5432/keycloak
      KC_DB_USERNAME: keycloak
      KC_DB_PASSWORD: password

      KC_HOSTNAME: localhost
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

Dans votre fichier de configuration, par exemple config.py, ajoutez les paramètres suivants :

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
    }
]


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
