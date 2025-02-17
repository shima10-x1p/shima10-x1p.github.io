import './Home.css'
import { Separator } from '@/components/ui/Separator'
import Navbar from '@/components/custom/Navbar'
import BigButton from '@/components/custom/BigButton'

import icon_twitter from "/src/assets/twitter.svg"
import icon_github from "/src/assets/github.svg"
import icon_zenn from "/src/assets/edit.svg"
import icon_user from "/src/assets/user.svg"

import icon_ngo from "/src/assets/ngo.svg"
import icon_koha from "/src/assets/koha.svg"

function Home() {
  return (
    <>
      <Navbar />
      <div className='grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3'>
        <BigButton title={"Twitter（現X）"} icon_src={icon_twitter} link={"https://x.com/shima10_x1p"} />
        <BigButton title={"GitHub"} icon_src={icon_github} link={"https://github.com/shima10-x1p"} />
        <BigButton title={"Zenn"} icon_src={icon_zenn} link={"https://zenn.dev/shima10_x1p"} />
        <BigButton title={"Profile"} icon_src={icon_user} link={"/#/profile"} />
      </div>
      <Separator className='my-10'/>
      <h1 className='text-2xl font-bold mb-5 text-left text-slate-500'>リンク集</h1>
      <div className='grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3'>
        <BigButton title={"周央サンゴ(ch)"} icon_src={icon_ngo} link={"https://www.youtube.com/@SuoSango"} />
        <BigButton title={"東堂コハク(ch)"} icon_src={icon_koha} link={"https://www.youtube.com/@TodoKohaku"} />
      </div>
    </>
  )
}

export default Home
