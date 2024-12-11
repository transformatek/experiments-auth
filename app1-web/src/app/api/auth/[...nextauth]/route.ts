// src/app/api/auth/[...nextauth]/route.ts
import NextAuth, { AuthOptions, TokenSet } from "next-auth";
import { JWT } from "next-auth/jwt";
import KeycloakProvider from "next-auth/providers/keycloak"


console.log(process.env.KEYCLOAK_CLIENT_ID,
    process.env.KEYCLOAK_CLIENT_SECRET,
    process.env.KEYCLOAK_ISSUER);
function requestRefreshOfAccessToken(token: JWT) {
    // Check if the refreshToken is a string before passing it
    if (typeof token.refreshToken !== 'string') {
        throw new Error('Invalid refresh token');
    }
    return fetch(`${process.env.KEYCLOAK_ISSUER}/protocol/openid-connect/token`, {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({
            client_id: process.env.KEYCLOAK_CLIENT_ID,
            client_secret: process.env.KEYCLOAK_CLIENT_SECRET,
            grant_type: "refresh_token",
            refresh_token: token.refreshToken,  // Ensure this is a string
        }),
        method: "POST",
        cache: "no-store"
    });
}

    
export const authOptions: AuthOptions = {
    providers: [
        KeycloakProvider({
            clientId: process.env.KEYCLOAK_CLIENT_ID,
            clientSecret: process.env.KEYCLOAK_CLIENT_SECRET,
            issuer: process.env.KEYCLOAK_ISSUER
        })
    ],
     session: {
        maxAge: 60 * 30
    },
    callbacks: {
        async jwt({ token, account }) {
            if (account) {
                token.idToken = account.id_token
                token.accessToken = account.access_token
                token.refreshToken = account.refresh_token
                token.expiresAt = account.expires_at
                return token
            }

            // We take a buffer of one minute (60 * 1000 ms)
            const expiresAt = token.expiresAt;
            if (typeof expiresAt === 'number' && Date.now() < (expiresAt * 1000 - 60 * 1000)) {
                return token;
            } else {
                try {
                    const response = await requestRefreshOfAccessToken(token)

                    const tokens: TokenSet = await response.json()

                    if (!response.ok) throw tokens

                    // Ensure expires_in is a number before using it
                    const expiresIn = typeof tokens.expires_in === 'number' ? tokens.expires_in : 3600; // Default to 3600 if invalid

                    const updatedToken: JWT = {
                        ...token, // Keep the previous token properties
                        idToken: tokens.id_token,
                        accessToken: tokens.access_token,
                        expiresAt: Math.floor(Date.now() / 1000 + expiresIn), // Use the validated expiresIn
                        refreshToken: tokens.refresh_token ?? token.refreshToken,
                    }
                    return updatedToken
                } catch (error) {
                    console.error("Error refreshing access token", error)
                    return { ...token, error: "RefreshAccessTokenError" }
                }
            }
        },
    }

}

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST }