import React, { useState, useEffect } from 'react';
import { signOut, getAuth, onAuthStateChanged } from 'firebase/auth';
import { auth } from '../firebase';
import { useNavigate } from 'react-router-dom';
import ParcelItem from '../components/ParcelItem';
import ParcelContainer from '../components/ParcelContainer';

function Home() {
    const navigate = useNavigate();
    const [user, setUser] = useState(null);
    const [parcels, setParcels] = useState([]);

    

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

                fetch(`http://127.0.0.1:5000/parcels/get?uid=${user.uid}`).then(response => {
                    return response.json();
                }).then(data => {
                    console.log(data);
                    setParcels(data.parcels);
                });

            } else {
                // No user is signed in.
                setUser(null);
            }
        });
    }, []);

    

    return (
        <div>
            <p>Welcome {user ? user.uid : 'anon'} you have {parcels.length} parcel(s) being tracked</p>
            <button onClick={handleLogout}>Logout</button>

            <ParcelContainer parcels={parcels} />
        </div>
    );
}

export default Home

