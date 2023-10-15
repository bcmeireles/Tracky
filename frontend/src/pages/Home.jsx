import React, { useState, useEffect } from 'react';
import { signOut, getAuth, onAuthStateChanged } from 'firebase/auth';
import { auth } from '../firebase';
import { useNavigate } from 'react-router-dom';

function Home() {
    const navigate = useNavigate();
    const [user, setUser] = useState(null);

    const handleLogout = () => {
        signOut(auth)
            .then(() => {
                // Sign-out successful.
                navigate('/login');
                console.log('Signed out successfully');
            })
            .catch((error) => {
                // An error happened.
            });
    };

    useEffect(() => {
        const auth = getAuth();
        onAuthStateChanged(auth, (user) => {
            if (user) {
                // User is signed in.
                setUser(user);
            } else {
                // No user is signed in.
                setUser(null);
            }
        });
    }, []);


    return (
        <div>
            <p>Welcome Home {user ? user.uid : 'anon'}</p>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Home

