import React from 'react';
import { Link } from 'react-router-dom';

const Layout = ({ children }) => {
    return (
        // <div className="bg-cover bg-center min-h-screen" style={{ backgroundImage: `url('https://img.itch.zone/aW1nLzExNzIzMjYwLmpwZw==/original/p4cvl4.jpg')` }}>
        <div className="bg-cover  bg-center min-h-screen"
            // style={{ backgroundImage: `url('https://media.istockphoto.com/photos/outer-space-universe-nebula-stars-star-cluster-blue-purple-pink-picture-id1173422519?k=20&m=1173422519&s=170667a&w=0&h=8YwfxbMeJm2R34p_WEhcVmVMCaYCZIZwX_j3K7i_klM=')` }}
        >
            <nav className="bg-green-50 opacity-70 p-4 m-4 fixed top-0 left-0 right-0 z-50 transition-all duration-500 ease-in-out transform hover:shadow-lg  rounded-lg shadow-md "> {/* Added transition and transform properties */}
                <div className="container mx-auto flex justify-between items-center">
                    <div className='w-16 h-2'>
                        <img src="https://wonderai.app/img/wonder_logo.bc672048.png" alt="" />
                    </div>
                    <div className="flex space-x-4">
                    </div>
                    <Link to="/" className="text-black flex-1 text-center py-2">Logout</Link>
                </div>
            </nav>
            <div className="mt-0">
                {children}
            </div>
        </div>
    );
};

export default Layout;
