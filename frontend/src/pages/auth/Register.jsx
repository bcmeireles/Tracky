import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { auth } from '../../firebase';
import { createUserWithEmailAndPassword, sendEmailVerification } from "firebase/auth";
import './style.css'

import emailIcon from '../../Components/LoginSignup/Assets/email.png'
import passwordIcon from '../../Components/LoginSignup/Assets/password.png'

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
              console.log("Email verification sent. Please check your email.");
            })
        } catch {
            console.log("Sorry, something went wrong. Please try again.");
        }
    } else {
        console.log("Passwords don't match. Please try again.");
    }
  };

  return (
    <div className="register template d-flex justify-content-center align-items-center vh-100 bg-primary">
      <div className='form_container p-5 rounded bg-white'>
        <form>
          <h3 className='text-center'>Register</h3>
          <div className='mb-2 input'>
            <img src={emailIcon} alt="" className='me-2'/>
            <input type="email" placeholder='Email' className="form-control" value={email} onChange={(e) => setEmail(e.target.value)}/>
          </div>
          <div className='mb-2 input'>
            <img src={passwordIcon} alt="" className='me-2'/>
            <input type="password" placeholder='Password' className="form-control" value={password} onChange={(e) => setPassword(e.target.value)}/>
          </div>
          <div className='mb-2 input'>
            <img src={passwordIcon} alt="" className='me-2'/>
            <input type="password" placeholder='Confirm Password' className="form-control" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)}/>
          </div>
          <div className="d-grid">
            <button className="btn btn-primary" onClick={(e) => signupWithUsernameAndPassword(e)}>Register</button>
          </div>
          <p className='text-end mt-2'>
            Already registered? <Link to="/login" className='ms-2'>Login</Link>
          </p>
        </form>
      </div>
    </div>
  )
}

export default Register