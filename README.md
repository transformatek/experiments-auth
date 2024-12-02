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

