import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar({ handleCreateParcel, handleLogout, isDarkMode, onChangeMode }) {
  return (
    <nav className={`p-4 ${isDarkMode ? 'bg-232b54' : 'bg-7faef5'}`}>
      <div className="container mx-auto flex items-center justify-between">
        <div className="flex items-center">
          <button
            onClick={handleCreateParcel}
            className='text-white hover:underline focus:outline-none ml-4'
          >
            Add Parcel
          </button>
          <button
            onClick={handleCreateParcel}
            className='text-white hover:underline focus:outline-none ml-4'
          >
            Go Premium
          </button>
        </div>
        <div className="flex items-center">
          <label className="switch">
            {/* Display the toggle switch */}
            <input type="checkbox" checked={isDarkMode} onChange={onChangeMode} />
            <span className="slider round">
              <i
                className={`fa ${isDarkMode ? 'fa-moon-o' : 'fa-sun-o'} text-white`}
                style={{
                  position: 'absolute',
                  top: '50%',
                  transform: 'translateY(-50%)',
                  left: isDarkMode ? '6px' : 'auto',
                  right: isDarkMode ? 'auto' : '6px',
                }}
              ></i>
            </span>
          </label>
          <button
            onClick={handleLogout}
            className='text-white hover:underline focus:outline-none ml-4'
          >
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
