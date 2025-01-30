import { useState } from 'react'
import './Tool.css'
import NavBar from '../components/NavBar'
import YouTubeEmbedApp from '../components/YoutubeEmbedApp'
import { Card, CardContent } from '../components/ui/card'

import ytIcon from '../assets/youtube.svg'

function Button({ children, onClick, variant }) {
	const baseStyle = "px-4 py-2 rounded-md focus:outline-none transition-all";
	const styles = {
		default: "border border-solid border-slate-700 text-gray-500 hover:bg-gray-400",
		outline: "border border-solid border-slate-800 text-gray-500 px-4 py-2 rounded-xl hover:bg-gray-400 hover:text-white",
	};
	return (
		<button onClick={onClick} className={`${baseStyle} ${styles[variant]}`}>{children}</button>
	);
}

const tabs = [
	{ id: "tab1", label: "Youtube埋め込み", content: <YouTubeEmbedApp />, img: ytIcon },
	{ id: "tab2", label: "工事中", content: <><span className='text-gray-500'>工事中</span></> },
];

function Tool() {
	const [activeTab, setActiveTab] = useState(tabs[0].id);

	return (
		<>
			{/* ナビゲーションバー */}
			<NavBar />
			{/* 切り替えボタン */}
			<div className="p-4">
				<div className="flex space-x-2 mb-4">
					{tabs.map((tab) => (
						<Button
							key={tab.id}
							onClick={() => setActiveTab(tab.id)}
							variant={activeTab === tab.id ? "default" : "outline"}
						>
							<div className='flex items-center'>
								<img src={tab.img} alt="" />
								<span className="text-gray-500 px-2 mb-1">
									{tab.label}
								</span>
							</div>
						</Button>
					))}
				</div>
				{tabs.find(tab => tab.id === activeTab)?.content}
			</div>
		</>

	);
}

export default Tool
