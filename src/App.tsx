import './App.css'
import Navbar from '@/components/custom/Navbar'
import BigButton from '@/components/custom/BigButton'

import icon_twitter from "/src/assets/twitter.svg"
import icon_github from "/src/assets/github.svg"
import icon_zenn from "/src/assets/edit.svg"

function App() {
  return (
    <>
      <Navbar />
      <div className='grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3'>
        <BigButton title={"Twitter（現X）"} icon_src={icon_twitter} link={"https://x.com/shima10_x1p"} />
        <BigButton title={"GitHub"} icon_src={icon_github} link={"https://github.com/shima10-x1p"} />
        <BigButton title={"Zenn"} icon_src={icon_zenn} link={"https://zenn.dev/shima10_x1p"} />
      </div>
    </>
  )
}

export default App
