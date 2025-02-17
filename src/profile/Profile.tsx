import './Profile.css'
import Navbar from '@/components/custom/Navbar'
import { Button } from '@/components/ui/Button'


function Profile() {
  return (
    <>
      <Navbar />
       <Button asChild variant="outline">
          <a className='text-slate-500' href="/">トップページ</a>
       </Button>
    </>
  )
}

export default Profile
