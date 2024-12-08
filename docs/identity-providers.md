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

# Setup Identity Provider for Single Sign-On (SSO)

## Prerequisites

- **Docker**: Utilisé pour déployer et exécuter le fournisseur d'identité (par exemple, Keycloak).
- **Flask**: Framework backend pour Python.
- **NextJS**: Framework frontend pour React.
- **Fournisseur d'Identité**: Choisissez un fournisseur comme Keycloak, Authentik, ou Supabase Auth.
- **Environnement de développement**: Installez les outils nécessaires tels que Node.js, Python, et Docker.
