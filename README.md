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

## Links

### 1. Research and Documentation 
  - 📄 [Keycloak Documentation](https://www.keycloak.org/documentation)
  - 📄 [Authentik Documentation](https://goauthentik.io/docs)
  - 📄 [Supabase Auth Documentation](https://supabase.com/docs/guides/auth)
  - 📄 [Supabase Auth /nextjs Documentation ](https://supabase.com/docs/guides/auth/quickstarts/nextjs)
  - 📄 [NextAuth.js Documentation](https://next-auth.js.org/providers/keycloak)
  - 📄 [Implementing Authentication in Next.js v13 Application with Keycloak(Part — 1)](https://medium.com/inspiredbrilliance/implementing-authentication-in-next-js-v13-application-with-keycloak-part-1-f4817c53c7ef)- 
  - 📄 [IBuilding a Secure Authentication System with Keycloak, React, and Flask](https://darkaico.medium.com/building-a-secure-authentication-system-with-keycloak-react-and-flask-35aeee04e37a)

### 2. Research and Documentation Videos

    🎥 [Implement OAuth 2.0 Authorization Code flow using authlib in python flask web apps | Single Sign On- Tutoriel vidéo] (https://youtu.be/O065sJQs51U?si=FEUMX_bHF3j4-oI-)
    🎥 [SSO with OIDC: Integrate Keycloak V.25 in Flask for Secure Login & Logout- Tutoriel vidéo] (https://youtu.be/2KQ4BsJf33E?si=7xFDLJAYsMf1QAUN)

## keycloak L

To access the Keycloak admin interface, visit http://localhost:8080.

## Development

Open the project in VS Code.
When prompted, **Open in a Container** and follow the instructions.
Once the container is running, open a terminal to proceed.

### Install and Run App1 (Frontend)

First run
```bash
cd app1
npm install
```

For developement 
```bash
cd app1
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Install and Run App2 (Backend)
Open a new terminal.

First run
```bash
cd app1-server
pip install -r requirements.txt
```

For developement 
```bash
cd app1-server
flask run --port=5000
```
Open [http://localhost:5000](http://localhost:5000) with your browser to see the result.





