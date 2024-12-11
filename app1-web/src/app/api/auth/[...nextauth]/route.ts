// src/app/api/auth/[...nextauth]/route.ts
import NextAuth, { AuthOptions } from "next-auth";
import KeycloakProvider from "next-auth/providers/keycloak"


console.log(process.env.KEYCLOAK_CLIENT_ID,
    process.env.KEYCLOAK_CLIENT_SECRET,
    process.env.KEYCLOAK_ISSUER);

    
export const authOptions: AuthOptions = {
    providers: [
        KeycloakProvider({
            clientId: process.env.KEYCLOAK_CLIENT_ID,
            clientSecret: process.env.KEYCLOAK_CLIENT_SECRET,
            issuer: process.env.KEYCLOAK_ISSUER
        })
    ]
}

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST }