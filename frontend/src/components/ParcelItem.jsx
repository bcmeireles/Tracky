import React from 'react';
import './ParcelItem.css';
import { toast } from 'react-toastify';

const getFieldLabel = (fieldName) => {
  return fieldName.replace(/([A-Z])/g, ' $1').replace(/^./, (str) => str.toUpperCase());
};

const ParcelItem = ({ parcel }) => {
  const handleUpdateClick = async () => {
    const courier = parcel.courier;
    const updateUrl = `http://127.0.0.1:5000/updateTracking/${courier}`;

    const myToast = toast.loading("Please wait...")
  
    try {
      const response = await fetch(updateUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          trackingID: parcel.trackingID,
          uid: parcel.ownerUID,
        }),
      });
  
      if (response.ok) {
        toast.update(myToast, { render: "Parcel updated successfully!", type: "success", isLoading: false, autoClose: 2000 });
      } else {
        toast.update(myToast, { render: "Parcel update failed. Please try again.", type: "error", isLoading: false, autoClose: 2000 });
      }
    } catch (error) {
      toast.update(myToast, { render: "An error occurred while updating the parcel.", type: "error", isLoading: false, autoClose: 2000 });
    }
  };

  return (
    <div className="card bg-white shadow-md rounded-md p-4 mb-4">
      <div className="flex flex-col">
        <h2 className='text-center text-lg font-bold'>{parcel.label}</h2>
        {Object.keys(parcel).map((field, index) => (
          field !== "label" && field !== "_id" && field !== "ownerUID" &&
          <p key={index} className='mb-1'>{getFieldLabel(field)}: {parcel[field]}</p>
        ))}
        <button onClick={handleUpdateClick}>Update</button>
      </div>
    </div>
  );
};

export default ParcelItem;
