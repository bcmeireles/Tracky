import React, { useState, useEffect } from 'react';
import { signOut, getAuth, onAuthStateChanged } from 'firebase/auth';
import { auth } from '../firebase';
import { useNavigate } from 'react-router-dom';
import ParcelContainer from '../components/ParcelContainer';
import Modal from 'react-modal'; 
import { toast } from 'react-toastify';
import Navbar from '../components/Navbar';
import './Modal.css'

function Home({onChangeMode, isDarkMode}) {
    const navigate = useNavigate();
    const [user, setUser] = useState(null);
    const [parcels, setParcels] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false); 
    const [formData, setFormData] = useState({
        label: '',
        trackingID: '',
        postalCode: '',
        courier: 'Select Courier',
    });

    const handleCreateParcel = () => {
        setIsModalOpen(true);
    };

    const handleModalClose = () => {
        setIsModalOpen(false);
    };

    const handleFormSubmit = () => {
        if (formData.label && formData.trackingID && formData.courier !== 'Select Courier') {
            const parcelData = {
                label: formData.label,
                trackingID: formData.trackingID,
                courier: formData.courier,
                uid: user.uid,
            };

            fetch('http://localhost:5000/parcels/create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(parcelData),
            })
                .then(response => {
                    console.log(response);
                    if (response.ok) {
                        toast.success('Parcel created successfully!');
                        handleModalClose();
                    } else {
                        toast.error('Parcel creation failed. Please try again.');
                    }
                })
                .catch(error => {
                    toast.error('An error occurred while creating the parcel.');
                });
        } else {
            toast.error('Please fill in all required fields.');
        }
    };
    

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

    const handleDeleteParcel = (parcelId) => {
        setParcels((prevParcels) => prevParcels.filter((parcel) => parcel._id !== parcelId));
    };

    async function fetchUpdatedParcelData(parcelId, parcelCourier) {
        try {
            const response = await fetch(`http://127.0.0.1:5000/parcels/getone?id=${parcelId}&courier=${parcelCourier}`);
            if (!response.ok) {
                throw new Error('Failed to fetch updated parcel data');
            }
            const data = await response.json();
            return data.parcel;
        } catch (error) {
            console.error('Error fetching updated parcel data:', error);
            throw error;
        }
    }

    const handleUpdateParcel = async (parcelId, courier) => {
        try {
            const updatedParcelData = await fetchUpdatedParcelData(parcelId, courier);

            setParcels((prevParcels) =>
                prevParcels.map((parcel) =>
                    parcel._id === parcelId
                        ? { ...parcel, ...updatedParcelData }
                        : parcel
                )
            );
        } catch (error) {
            console.error('Error updating parcel:', error);
            throw error;
        }
    };

    const modalClassName = `ReactModal__Content${isDarkMode ? '-dark' : ''}`;

    return (
        <div className={`home-container ${isDarkMode ? 'dark' : 'light'}`}>
            <Navbar user={user} parcels={parcels} handleLogout={handleLogout} handleCreateParcel={handleCreateParcel} onChangeMode={onChangeMode} isDarkMode={isDarkMode}/>

            <ParcelContainer parcels={parcels} onDeleteParcel={handleDeleteParcel} onUpdateParcel={handleUpdateParcel} isDarkMode={isDarkMode}/>

            <Modal
                isOpen={isModalOpen}
                onRequestClose={handleModalClose}
                contentLabel="Create Parcel"
                className={modalClassName}
            >
                <h2>Create Parcel</h2>
                <form onSubmit={handleFormSubmit}>
                    <select
                        value={formData.courier}
                        onChange={(e) => setFormData({ ...formData, courier: e.target.value })}
                    >
                        <option value="Select Courier">Select Courier</option>
                        <option value="correosexpress">Correos Express</option>
                        <option value="ctt">CTT</option>
                        <option value="paack">Paack</option>
                        <option value="ups">UPS</option>
                        <option value="yunexpress">YUN Express</option>
                        <option value="gls">GLS</option>
                    </select>

                    <input
                        type="text"
                        placeholder="Label"
                        value={formData.label}
                        onChange={(e) => setFormData({ ...formData, label: e.target.value })}
                    />
                    <input
                        type="text"
                        placeholder="Tracking ID"
                        value={formData.trackingID}
                        onChange={(e) => setFormData({ ...formData, trackingID: e.target.value })}
                    />

                    {formData.courier === "paack" && (
                        <input
                            type="text"
                            placeholder="Postal Code"
                            value={formData.postalCode}
                            onChange={(e) => setFormData({ ...formData, postalCode: e.target.value })}
                        />
                    )}
                    
                    <button type="submit">Create</button>
                </form>
            </Modal>
        </div>
    );
}

export default Home

