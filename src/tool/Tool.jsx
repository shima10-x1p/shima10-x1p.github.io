import { useState } from 'react'
import './Tool.css'
import NavBar from '../components/NavBar'
import YouTubeEmbedApp from '../components/YoutubeEmbedApp'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <NavBar />
      <span className="flex font-medium text-gray-500 text-2xl">
        Youtube埋め込み
      </span>
      <YouTubeEmbedApp />
      <a href="/" className='border border-solid border-slate-500 text-gray-500 px-4 py-2 rounded-xl'>トップページ</a>
    </>
  )
}

export default App
