import React, { useState, useEffect } from 'react';
import { signOut, getAuth, onAuthStateChanged } from 'firebase/auth';
import { auth } from '../firebase';
import { useNavigate } from 'react-router-dom';
import ParcelContainer from '../components/ParcelContainer';

import { toast } from 'react-toastify';

function Home() {
    const navigate = useNavigate();
    const [user, setUser] = useState(null);
    const [parcels, setParcels] = useState([]);

    

    const handleLogout = () => {
        signOut(auth)
            .then(() => {
                // Sign-out successful.
                navigate('/login');
                toast.success('Signed out successfully');
            })
            .catch((error) => {
                toast.error(error.message);
            });
    };

    useEffect(() => {
        const auth = getAuth();
        onAuthStateChanged(auth, (user) => {
            if (user) {
                setUser(user);
                fetch(`http://127.0.0.1:5000/parcels/get?uid=${user.uid}`).then(response => {
                    return response.json();
                }).then(data => {
                    setParcels(data.parcels);
                });
            } else {
                setUser(null);
            }
        });
    }, []);

    return (
        <div>
            <p>Welcome {user ? user.uid : 'anon'} you have {parcels.length} {parcels.length === 1 ? 'parcel' : 'parcels'} being tracked</p>
            <button onClick={handleLogout}>Logout</button>

            <ParcelContainer parcels={parcels} />
        </div>
    );
}

export default Home

