import NextAuth, { NextAuthOptions } from 'next-auth';
import KeycloakProvider from 'next-auth/providers/keycloak';

console.log(process.env.KEYCLOAK_CLIENT_ID,
    process.env.KEYCLOAK_CLIENT_SECRET,
    process.env.KEYCLOAK_ISSUER);

export const authOptions: NextAuthOptions = {
    providers: [
        KeycloakProvider({
            clientId: process.env.KEYCLOAK_CLIENT_ID!,
            clientSecret: process.env.KEYCLOAK_CLIENT_SECRET!,
            issuer: process.env.KEYCLOAK_ISSUER!,
        }),
    ],
    // callbacks: {
    //     async jwt({ token, account }) {
    //         if (account) {
    //             token.accessToken = account.access_token;
    //             token.refreshToken = account.refresh_token;
    //             token.accessTokenExpires = account.expires_at ? account.expires_at * 1000 : undefined;
    //         }
    //         return token;
    //     },
    // },
};



const handler = NextAuth(authOptions);
export { handler as GET, handler as POST }
