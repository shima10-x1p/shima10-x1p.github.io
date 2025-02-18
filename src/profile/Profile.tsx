import './Profile.css'
import Navbar from '@/components/custom/Navbar'
import { Button } from '../components/ui/button'


function Profile() {
  return (
    <>
      <Navbar />
       <Button asChild variant="outline" size="lg" className='mt-10'>
          <a className='text-slate-500' href="/#/">トップページ</a>
       </Button>
    </>
  )
}

export default Profile
