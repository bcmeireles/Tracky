import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { auth } from '../../firebase';
import { sendPasswordResetEmail } from 'firebase/auth'; // Import the password reset function
import './style.css';

import { toast } from 'react-toastify';

function ResetPassword() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');

  const onResetPassword = async (e) => {
    e.preventDefault();

    try {
      await sendPasswordResetEmail(auth, email);
      toast.info('Password reset email sent. Please check your email.');
      navigate('/login');
    } catch {
      toast.error('Sorry, something went wrong. Please try again.');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 to-purple-800">
      <div className="bg-white p-8 rounded-lg shadow-md mx-auto form-container">
        <h2 className="text-2xl font-semibold text-center text-purple-700">Reset Password</h2>
        <form className="mt-4">
          <div className="mb-4 flex items-center">
            <span className="inline-block pr-2">
              <i className="fa fa-envelope text-purple-700" style={{ fontSize: '18px' }}></i>
            </span>
            <input
              type="email"
              id="email"
              name="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-purple-300"
              placeholder="Enter your email"
            />
          </div>
          <button
            className="w-full bg-gradient-to-br from-purple-700 to-purple-800 text-white py-2 rounded-lg hover:bg-gradient-to-br hover:from-purple-800 hover:to-purple-900 focus:outline-none focus:ring focus:ring-purple-300"
            onClick={(e) => onResetPassword(e)}
          >
            Reset Password
          </button>
        </form>
        <p className="mt-4 text-center text-gray-600">
          Remember your password? <Link to="/login" className="text-purple-700 hover:underline">Click here</Link>
        </p>
      </div>
    </div>
  );
}

export default ResetPassword;
