import React, { useState } from 'react';
import { BrowserRouter as Router} from 'react-router-dom';
import {Routes, Route} from 'react-router-dom';

import Home from './pages/Home';
import Login from './pages/auth/Login';
import Register from './pages/auth/Register';
import ResetPassword from './pages/auth/ResetPassword';

import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  const [isDarkMode, setIsDarkMode] = useState(true);

  const handleChangeMode = () => {
    setIsDarkMode(!isDarkMode);
  }
 
  return (
    <Router>
      <div>
        <section>                              
            <Routes>                                                                        
              <Route path="/home" element={<Home onChangeMode={handleChangeMode} isDarkMode={isDarkMode} />}/>
              <Route path="/login" element={<Login/>}/>
              <Route path="/register" element={<Register/>}/>
              <Route path="/resetpassword" element={<ResetPassword/>}/>
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
          theme="dark"
          />
      </div>
    </Router>
  );
}
 
export default App;