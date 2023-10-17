import React, {useState, useEffect} from 'react';
import { BrowserRouter as Router} from 'react-router-dom';
import {Routes, Route} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import Home from './pages/Home';
import Login from './pages/auth/Login';
import Register from './pages/auth/Register';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
 
  return (
    <Router>
      <div>
        <section>                              
            <Routes>                                                                        
               <Route path="/" element={<Home/>}/>
               <Route path="/login" element={<Login/>}/>
               <Route path="/register" element={<Register/>}/>
               <Route path="/home" element={<Home/>}/>
            </Routes>                    
        </section>
        <ToastContainer
          position="top-center"
          autoClose={2000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme="colored"
          />
      </div>
    </Router>
  );
}
 
export default App;