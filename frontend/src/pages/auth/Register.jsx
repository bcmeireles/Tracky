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
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-600 to-purple-800">
      <div className="bg-white p-8 rounded-lg shadow-md mx-auto form-container">
        <h2 className="text-2xl font-semibold text-center text-purple-700">Register</h2>
        <form className="mt-4">
          <div className="mb-4 flex items-center">
            <span className="inline-block pr-2">
              <i className="fa fa-envelope text-purple-700" style={{ 'font-size': '18px' }}></i>
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
          <div className="mb-4 flex items-center">
            <span className="inline-block pr-2">
              <i className="fa fa-lock text-purple-700" style={{ 'font-size': '29px' }}></i>
            </span>
            <input
              type="password"
              id="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-purple-300"
              placeholder="Enter your password"
            />
          </div>
          <div className="mb-4 flex items-center">
            <span className="inline-block pr-2">
              <i className="fa fa-lock text-purple-700" style={{ 'font-size': '29px' }}></i>
            </span>
            <input
              type="password"
              id="verifyPassword"
              name="verifyPassword"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-purple-300"
              placeholder="Verify your password"
            />
          </div>
          <button
            className="w-full bg-gradient-to-br from-purple-700 to-purple-800 text-white py-2 rounded-lg hover:bg-gradient-to-br hover:from-purple-800 hover:to-purple-900 focus:outline-none focus:ring focus:ring-purple-300"
            onClick={(e) => signupWithUsernameAndPassword(e)}
          >
            Register
          </button>
        </form>
        <p className="mt-4 text-center text-gray-600">
          Already have an account? <Link to="/login" className="text-purple-700 hover:underline">Click here</Link>
        </p>
      </div>
    </div>
  );
  
}

export default Register