import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { auth } from '../../firebase';
import { createUserWithEmailAndPassword, sendEmailVerification } from "firebase/auth";
import './style.css'

import { toast } from 'react-toastify';

function Register() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const signupWithUsernameAndPassword = async (e) => {
    e.preventDefault();

    if (password === confirmPassword) {
        try {
            await createUserWithEmailAndPassword(auth, email, password).then((user) => {
              sendEmailVerification(user.user);
              toast.info("Email verification sent. Please check your email.");
              navigate('/login');
            })
        } catch {
            toast.error("Sorry, something went wrong. Please try again.");
        }
    } else {
        toast.error("Passwords don't match. Please try again.");
    }
  };

  return (
    <div className="register flex justify-center items-center min-h-screen bg-primary">
      <div className='form_container p-5 rounded bg-white'>
        <form>
          <h3 className='text-center'>Register</h3>
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
          <div className='mb-2'>
            <i className='fa fa-lock me-2 text-3xl'></i>
            <input
              type="password"
              placeholder='Password'
              className="form-input"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className='mb-2'>
            <i className='fa fa-lock me-2 text-3xl'></i>
            <input
              type="password"
              placeholder='Confirm Password'
              className="form-input"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
          </div>
          <div className="mt-4">
            <button
              className="btn-primary w-full"
              onClick={(e) => signupWithUsernameAndPassword(e)}
            >
              Register
            </button>
          </div>
          <p className='text-right mt-2'>
            Already registered? <Link to="/login" className='ml-2 text-blue-500'>Login</Link>
          </p>
        </form>
      </div>
    </div>
  )
  
}

export default Register