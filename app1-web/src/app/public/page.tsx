// src/app/public/page.tsx
import { getServerSession } from 'next-auth';
import { authOptions } from '@/app/api/auth/[...nextauth]/route';
import Logout from '@/components/logout';
import Login from '@/components/login';

export default async function Public() {
    const session = await getServerSession(authOptions)
    if (session) {
        return <div >
            <div>You are accessing a public page</div>
            <div>Your name is {session.user?.name}</div>
            <div>
                <Logout />
            </div>
        </div>
    }
    return (
        <div >
            <div>You are accessing a public page</div>
            <div>
                <Login />
            </div>
        </div>
    )
}