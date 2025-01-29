import React from "react";

const LikesCard = () => {
    return (
        <div className="border border-slate-800 rounded-xl my-5">
            <div className="flex py-3 px-2 items-center">
                {/* <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#64748a" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="feather feather-heart"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg> */}
                <p className="pl-3 text-gray-500">推し：</p>
                <div className="flex items-center">
                    <a href="https://www.youtube.com/@SuoSango" className="flex items-center">
                        <span className="text-gray-500">
                            💞🦩
                        </span>
                    </a>
                    <a href="https://www.youtube.com/@TodoKohaku" className="flex items-center">
                        <span className="text-gray-500">
                            🍯
                        </span>
                    </a>
                    <a href="https://www.youtube.com/@KitakojiHisui" className="flex items-center">
                        <span className="text-gray-500">
                        ❇️
                        </span>
                    </a>
                </div>
            </div>
        </div>
    );
};

export default LikesCard