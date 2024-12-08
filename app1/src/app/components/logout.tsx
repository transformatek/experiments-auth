"use client";
import { signOut } from "next-auth/react";

export default function Logout() {
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
                onClick={() => signOut()}
                style={{
                    backgroundColor: "#eda879", 
                    color: "#fff",
                    border: "none",
                    padding: "12px 24px",
                    fontSize: "16px",
                    borderRadius: "8px",
                    cursor: "pointer",
                    boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)"
                }}
            >
                Sign out of Keycloak
            </button>
        </div>
    );
}
