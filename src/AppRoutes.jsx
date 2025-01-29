import {
    HashRouter,
    Route,
    Routes
  } from "react-router-dom";
  import Home from './home/Home';
  import Tool from './tool/Tool';
  
  const AppRoutes = () => {
    return (
      <HashRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/tool' element={<Tool />} />
        </Routes>
      </HashRouter>
    )
  }
  
  export default AppRoutes;