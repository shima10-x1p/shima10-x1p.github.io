import { useState } from 'react'
import './Tool.css'
import NavBar from '../components/NavBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <NavBar />
      <h2>ほげ</h2>
      {/* <Link to='/'>ホーム</Link> */}
    </>
  )
}

export default App
