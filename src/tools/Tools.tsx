import Navbar from "../components/custom/Navbar"
import YtTimeStamp from "./YtTimeStamp/YtTimeStamp"
import { Button } from '../components/ui/button'
import BigButton from '../components/custom/BigButton'

import icon_youtube from "../assets/youtube.svg"

const Tool = () => {
    return (
        <>
            <Navbar />
            <h1 className='text-2xl font-bold mb-5 text-center text-slate-500'>ツール集</h1>
            <div className='grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3'>
                <BigButton title={"YouTubeリンクにタイムスタンプつけるやつ"} icon_src={icon_youtube} link={"/#/tools/yt-timestamp"} />
            </div>

            <Button asChild variant="outline" size="lg" className='mt-10'>
                <a className='text-slate-500' href="/#/">トップページ</a>
            </Button>
        </>
    )
}

export default Tool