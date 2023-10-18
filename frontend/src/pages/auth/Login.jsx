import React, { useState } from 'react'
import './style.css'
import { Link, useNavigate } from 'react-router-dom'
import { auth } from '../../firebase';
import { signOut, signInWithEmailAndPassword } from 'firebase/auth';

import { toast } from 'react-toastify';

function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const onLogin = async (e) => {
    e.preventDefault();
    try {
      await signInWithEmailAndPassword(auth, email, password)
      .then((user) => {
        if (user.user.emailVerified) {
          toast.success('Successfully logged in.');
          navigate('/home')
        } else {
          toast.warning('Please verify your email first.');
          signOut(auth)
            .then(() => {
                //
            })
            .catch((error) => {
              toast.error(error.message);
            });
        }
      })
    } catch {
      toast.error('Sorry, something went wrong. Please try again.');
    }
  }

  return (
    <div className="login flex justify-center items-center h-screen bg-black">
      <div className='form-container p-5 rounded bg-white'>
        <form>
          <h3 className='text-center'>Login</h3>
          <div className='mb-2'>
            <i className='fa fa-envelope me-2' style={{ 'font-size': '24px' }}></i>
            <input type="email" placeholder='Email' className="form-input" onChange={(e) => setEmail(e.target.value)} />
          </div>
          <div className='mb-2'>
            <i className='fa fa-lock me-2' style={{ 'font-size': '36px' }}></i>
            <input type="password" placeholder='Password' className="form-input" onChange={(e) => setPassword(e.target.value)} />
          </div>
          <div className="mt-4">
            <button className="btn-primary w-full" onClick={(e) => onLogin(e)}>Login</button>
          </div>
          <p className='text-right mt-2 grid'>
            <a href='/resetpassword' className='text-blue-500'>Forgot Password? Click here</a>
            <Link to="/register" className='ml-2 text-blue-500'>Register</Link>
          </p>
        </form>
      </div>
    </div>
  )
  
}

export default Login