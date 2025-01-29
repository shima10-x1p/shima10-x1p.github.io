import { useState } from 'react'
import './Home.css'
import NavBar from '../components/NavBar'
import InfoCard from '../components/InfoCard'
import LikesCard from '../components/LikesCard'
import YouTubeEmbedApp from '../components/YoutubeEmbedApp'
import xIcon from '../assets/twitter.svg'
import githubIcon from '../assets/github.svg'
import editIcon from '../assets/edit.svg'
import boxIcon from '../assets/box.svg'
import userIcon from '../assets/user.svg'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <NavBar />
      <div className='grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3'>
        <InfoCard title={"Twitter（現X）"} icon_src={xIcon} link={"https://x.com/shima10_x1p"} />
        <InfoCard title={"Github"} icon_src={githubIcon} link={"https://github.com/shima10-x1p"} />
        <InfoCard title={"Zenn"} icon_src={editIcon} link={"https://zenn.dev/shima10_x1p"} />
        <InfoCard title={"Profile"} icon_src={userIcon} link={"#"} />
        <InfoCard title={"Tool Box"} icon_src={boxIcon} link={"/#/tool"} />
      </div>
      <div>
        <LikesCard />
      </div>
      
      <YouTubeEmbedApp />
    </>
  )
}

export default App
