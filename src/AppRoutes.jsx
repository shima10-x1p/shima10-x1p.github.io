import {
    BrowserRouter,
    Route,
    Routes
  } from "react-router-dom";
  import Home from './home/Home';
  import Tool from './tool/Tool';
  
  const AppRoutes = () => {
    return (
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/tool' element={<Tool />} />
        </Routes>
      </BrowserRouter>
    )
  }
  
  export default AppRoutes;