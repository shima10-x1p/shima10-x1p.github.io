import {
    HashRouter,
    Route,
    Routes
  } from "react-router-dom";
  import Home from './home/Home';
  import Tool from './tool/Tool';
  import Profile from './profile/Profile'
  
  const AppRoutes = () => {
    return (
      <HashRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/tool' element={<Tool />} />
          <Route path='/profile' element={<Profile />} />
        </Routes>
      </HashRouter>
    )
  }
  
  export default AppRoutes;