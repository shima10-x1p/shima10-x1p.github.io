import {
    HashRouter,
    Route,
    Routes
} from 'react-router-dom';
import Home from './home/Home';
import Profile from './profile/Profile';
import Tool from './tools/Tools';
import YtTimeStamp from './tools/YtTimeStamp/YtTimeStamp';

const AppRoutes = () => {
    return (
        <HashRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/profile" element={<Profile />} />
                <Route path="/tools" element={<Tool />} />
                <Route path="/tools/yt-timestamp" element={<YtTimeStamp />} />
            </Routes>
        </HashRouter>
    );
}

export default AppRoutes;