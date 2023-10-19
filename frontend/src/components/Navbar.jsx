import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

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
        <div className="flex items-center">
          <label className="switch">
            {/* Display the toggle switch */}
            <input type="checkbox" checked={isDarkMode} onChange={toggleDarkMode} />
            <span className="slider round">
              {/* Display the sun and moon icons inside the toggle with vertical alignment */}
              <i
                className={`fa ${isDarkMode ? 'fa-moon-o' : 'fa-sun-o'} text-white hover:underline`}
                style={{ position: 'absolute', top: '50%', transform: 'translateY(-50%)' }}
              ></i>
            </span>
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
