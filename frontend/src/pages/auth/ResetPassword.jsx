import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { auth } from '../../firebase';
import { sendPasswordResetEmail } from 'firebase/auth'; // Import the password reset function
import './style.css';

import { toast } from 'react-toastify';

function ResetPassword() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');

  const resetPassword = async (e) => {
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
    <div className="reset-password flex justify-center items-center min-h-screen bg-primary">
      <div className='form-container p-5 rounded bg-white'>
        <form>
          <h3 className='text-center'>Reset Password</h3>
          <div className='mb-2'>
            <i className='fa fa-envelope me-2 text-2xl'></i>
            <input
              type="email"
              placeholder='Email'
              className="form-input"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="mt-4">
            <button
              className="btn-primary w-full"
              onClick={(e) => resetPassword(e)}
            >
              Reset Password
            </button>
          </div>
          <p className='text-right mt-2'>
            Remember your password? <Link to="/login" className='ml-2 text-blue-500'>Login</Link>
          </p>
        </form>
      </div>
    </div>
  )  
}

export default ResetPassword;
