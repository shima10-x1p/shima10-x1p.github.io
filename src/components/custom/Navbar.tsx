import icon from "/src/assets/images/user_icon.jpg"

const Navbar = () => {
    return (
        <nav className='mx-auto'>
            <div className="flex">
                <a href="/" className="flex py-4 my-3 items-center">
                    <img className='rounded-full' width={100} height={100} src={icon} alt="" />
                    <span className="font-semibold text-slate-500 text-3xl px-7">
                        しま (@shima10_x1p)
                    </span>
                </a>
            </div>
        </nav>
    );
};

export default Navbar;