import React from "react";

interface ChildProps {
    title: string;
    icon_src: string;
    link: string;
}

const BigButton: React.FC<ChildProps> = ({ title, icon_src, link }) => {
    return (
        <a href={link} className="hover:opacity-60">
            <div className="border border-slate-700 rounded-xl py-3 px-4">
                <div className="flex items-center">
                    <img src={icon_src} alt="" />
                    <span className="text-slate-500 px-4">
                        {title}
                    </span>
                </div>
            </div>
        </a>

    )
}

export default BigButton;