import Navbar from "../components/custom/Navbar"
import YtTimeStamp from "./YtTimeStamp/YtTimeStamp"
import { Button } from '../components/ui/button'

const Tool = () => {
    return (
        <>
            <Navbar />
            <h1 className='text-2xl font-bold mb-5 text-center text-slate-500'>YouTubeリンクにタイムスタンプつけるやつ (GPT-4o)</h1>
            <YtTimeStamp />

            <Button asChild variant="outline" size="lg" className='mt-10'>
                <a className='text-slate-500' href="/">トップページ</a>
            </Button>
        </>
    )
}

export default Tool