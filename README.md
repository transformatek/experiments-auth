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

