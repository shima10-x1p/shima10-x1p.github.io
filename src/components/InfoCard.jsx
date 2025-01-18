import React from "react";

const InfoCard = ({title, icon_src, link}) => {
    return (
        <div className="border border-slate-800 rounded-xl">
            <div className="flex py-3 px-3">
                <a href={link} className="flex items-center">
                    <img src={icon_src} alt="" />
                    <span className="text-gray-500 px-4">
                        {title}
                    </span>
                </a>

            </div>
        </div>
    );
};

export default InfoCard