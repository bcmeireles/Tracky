import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function Navbar({ handleCreateParcel, handleLogout }) {
  const [isDarkMode, setDarkMode] = useState(false);

  // Function to toggle between light and dark mode
  const toggleDarkMode = () => {
    setDarkMode(!isDarkMode);
    // Add your code to toggle between light and dark mode here.
  };

  return (
    <nav className="bg-purple-600 p-4">
      <div className="container mx-auto flex items-center justify-between">
        <div className="flex items-center">
          <button onClick={handleCreateParcel} className="text-white hover:underline focus:outline-none ml-4">
            Add Parcel
          </button>
          <button onClick={handleCreateParcel} className="text-white hover:underline focus:outline-none ml-4">
            Go Premium
          </button>
        </div>

        <Link to="/" className="text-white text-xl font-bold">Tracky</Link>

        <div className="flex items-center">
          <label className="text-white mr-2">Light/Dark Mode</label>
          <label className="switch">
            <input type="checkbox" checked={isDarkMode} onChange={toggleDarkMode} />
            <span className="slider round"></span>
          </label>
          <button onClick={handleLogout} className="text-white hover:underline focus:outline-none ml-4">
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
