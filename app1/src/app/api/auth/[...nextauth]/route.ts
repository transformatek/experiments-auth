import NextAuth, { NextAuthOptions } from 'next-auth';
import KeycloakProvider from 'next-auth/providers/keycloak';

// Define the `authOptions`
export const authOptions: NextAuthOptions = {
    providers: [
        KeycloakProvider({
            clientId: process.env.KEYCLOAK_CLIENT_ID!,
            clientSecret: process.env.KEYCLOAK_CLIENT_SECRET!,
            issuer: 'http://localhost:8080/auth/realms/my-app-realm',
        }),
    ],
};

// Export the default NextAuth handler
export default NextAuth(authOptions);
