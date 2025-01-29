import { useState } from 'react'
import './Profile.css'
import NavBar from '../components/NavBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <NavBar />
      <span className='text-gray-500'>工事中</span>
      <div className='py-10'>
      <a href="/" className='border border-solid border-slate-500 text-gray-500 px-4 py-2 rounded-xl'>トップページ</a>
      </div>
    </>
  )
}

export default App
