"use client";
import { signIn } from "next-auth/react";

export default function Login() {
    return (
        <div
            style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                backgroundColor: "#f0f0f0"
            }}
        >
            <button
                onClick={() => signIn("keycloak", { callbackUrl: "http://localhost:3000/" })}
                style={{
                    backgroundColor: "#206fba",
                    color: "#fff",
                    border: "none",
                    padding: "12px 24px",
                    fontSize: "16px",
                    borderRadius: "8px",
                    cursor: "pointer",
                    boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)"
                }}
            >
                Sign in with Keycloak
            </button>
        </div>
    );
}
