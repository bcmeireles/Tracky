import React, { useState } from 'react'
import './style.css'
import { Link, useNavigate } from 'react-router-dom'
import { auth } from '../../firebase';
import { signInWithEmailAndPassword } from 'firebase/auth';

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
          console.log(user.user);
        } else {
          console.log('Please verify your email first.');
        }
      })
    } catch {
      console.log('Sorry, something went wrong. Please try again.');
    }
  }

  return (
    <div className="login template d-flex justify-content-center align-items-center vh-100 bg-primary">
      <div className='form_container p-5 rounded bg-white'>
        <form>
          <h3 className='text-center'>Login</h3>
          <div className='mb-2'>
            <label htmlFor="email">Email</label>
            <input type="email" placeholder='Email' className="form-control" onChange={(e)=>setEmail(e.target.value)}/>
          </div>
          <div className='mb-2'>
            <label htmlFor="password">Password</label>
            <input type="password" placeholder='Password' className="form-control" onChange={(e)=>setPassword(e.target.value)}/>
          </div>
          <div className="d-grid">
            <button className="btn btn-primary" onClick={(e) => onLogin(e)}>Login</button>
          </div>
          <p className='text-end mt-2'>
            Forgot <a href=''>Password?</a><Link to="/register" className='ms-2'>Register</Link>
          </p>
        </form>
      </div>
    </div>
  )
}

export default Login