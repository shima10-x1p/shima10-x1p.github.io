import React from 'react';

const Navbar = () => {
    return (
        <nav className='mx-auto'>
            <div className="flex">
                <a href="#" className="flex py-4 my-3 items-center">
                    <img className='rounded-full' width={100} height={100} src="/src/assets/mOlgmiSO_400x400.jpg" alt="" />
                    <span className="font-semibold text-gray-500 text-3xl px-7">
                        しま (@shima10_x1p)
                    </span>
                </a>
            </div>
        </nav>
    );
};

export default Navbar;
