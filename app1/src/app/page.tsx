// src/app/page.tsx
import { getServerSession } from 'next-auth'
import { authOptions } from './api/auth/[...nextauth]/route'
import Logout from './components/logout'
import Login from './components/login'
export default async function Home() {
  const session = await getServerSession(authOptions)
  if (session) {
    return <div>
      <div>Your name is {session.user?.name}</div>
      <div><Logout /> </div>
    </div>
  }
  return (
    <div>
      <Login />
    </div>
  )
}