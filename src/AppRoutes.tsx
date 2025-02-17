import {
    HashRouter,
    Route,
    Routes
} from 'react-router-dom';
import Home from './home/Home';
import Profile from './profile/Profile';
import Tool from './tools/Tools';

const AppRoutes = () => {
    return (
        <HashRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="/tools" element={<Tool />} />
            </Routes>
        </HashRouter>
    );
}

export default AppRoutes;