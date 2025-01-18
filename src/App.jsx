import { useState } from 'react'
import './App.css'
import NavBar from './components/NavBar'
import InfoCard from './components/InfoCard'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <NavBar />
      <div className='grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3'>
        <InfoCard title={"X"} icon_src={"/src/assets/twitter.svg"} link={"https://x.com/shima10_x1p"}/>
        <InfoCard title={"Github"} icon_src={"/src/assets/github.svg"} link={"https://github.com/shima10-x1p"}/>
        <InfoCard title={"Zenn"} icon_src={"/src/assets/edit.svg"} link={"https://zenn.dev/shima10_x1p"}/>
      </div>
    </>
  )
}

export default App
