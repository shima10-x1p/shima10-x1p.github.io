import {
    HashRouter,
    Route,
    Routes
} from 'react-router-dom';
import Home from './home/Home';
import Profile from './profile/Profile';

const AppRoutes = () => {
    return (
        <HashRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/profile" element={<Profile />} />
            </Routes>
        </HashRouter>
    );
}

export default AppRoutes;