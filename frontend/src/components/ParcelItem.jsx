import React from 'react';
import './ParcelItem.css';
import { toast } from 'react-toastify';

const getFieldLabel = (fieldName) => {
  return fieldName.replace(/([A-Z])/g, ' $1').replace(/^./, (str) => str.toUpperCase());
};

const ParcelItem = ({ parcel, onDeleteParcel, onUpdateParcel, isDarkMode }) => {
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
        onUpdateParcel(parcel._id, parcel.courier);
      } else {
        toast.update(myToast, { render: "Parcel update failed. Please try again.", type: "error", isLoading: false, autoClose: 2000 });
      }
    } catch (error) {
      toast.update(myToast, { render: "An error occurred while updating the parcel.", type: "error", isLoading: false, autoClose: 2000 });
    }
  };

  const handleDeleteClick = async () => {
    
    const deleteUrl = 'http://127.0.0.1:5000/parcels/delete';

    const myToast = toast.loading("Please wait...")

    try {
      const response = await fetch(deleteUrl, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          trackingID: parcel.trackingID,
          uid: parcel.ownerUID,
          courier: parcel.courier,
        }),
      });

      if (response.ok) {
        toast.update(myToast, { render: "Parcel deleted successfully!", type: "success", isLoading: false, autoClose: 2000 });
        onDeleteParcel(parcel._id);
      } else {
        toast.update(myToast, { render: "Parcel deletion failed. Please try again.", type: "error", isLoading: false, autoClose: 2000 });
      }
    } catch (error) {
      toast.update(myToast, { render: "An error occurred while deleting the parcel.", type: "error", isLoading: false, autoClose: 2000 });
    }
  };

  const calculateProgress = () => {
    if (parcel.progress !== undefined && parcel.progress > 1) {
      return parcel.progress; 
    } else if (parcel.status === 'confirmed' || parcel.status === 'waiting' || parcel.status === 'unverified') {
      return 0;
    } else if (parcel.status === 'intransit') {
      return 50;
    } else if (parcel.status === 'delivered') {
      return 100;
    }
    console.log(parcel.label)
    return 50;
  };

  const progressValue = calculateProgress();

  const getProgressColorClass = (mode) => {
    if (progressValue == 0) {
      if (mode === 0) {
        return 'bg-red-500';
      } else {
        return 'bg-red-100'
      }
    } else if (progressValue == 100) {
      if (mode === 0) {
        return 'bg-green-500';
      } else {
        return 'bg-green-100'
      }
    }
    if (mode === 0) {
      return 'bg-yellow-500';
    } else {
      return 'bg-yellow-100'
    }
  };

  const calculateTimeAgo = () => {
    const now = new Date();
    const lastCheckedTime = new Date(parcel.lastChecked * 1000); // Convert seconds to milliseconds
    const diffMs = now - lastCheckedTime;
    const seconds = Math.floor(diffMs / 1000);
    if (seconds < 60) {
      return `${seconds} seconds ago`;
    }
    const minutes = Math.floor(seconds / 60);
    if (minutes < 60) {
      return `${minutes} minutes ago`;
    }
    const hours = Math.floor(minutes / 60);
    if (hours > 470000)
      return "Never"
    return `${hours} hours ago`;
  };

  const timeAgo = calculateTimeAgo();

  const trackingLinkBuilder = (parcel) => {
    if (parcel.courier === 'correosexpress') {
      return `https://s.correosexpress.com/SeguimientoSinCP/search?shippingNumber=${parcel.trackingID}`;
    } else if (parcel.courier === 'ctt') {
      return `https://appserver.ctt.pt/CustomerArea/PublicArea_Detail?IsFromPublicArea=true&ObjectCodeInput=${parcel.trackingID}&SearchInput=${parcel.trackingID}`;
    } else if (parcel.courier === 'paack') {
      return `https://mydeliveries.paack.app/tracking/order?tracking_number=${parcel.trackingID}&postal_code=${parcel.postalCode}`;
    } else if (parcel.courier === 'ups') {
      return `https://www.ups.com/track?loc=pt_PT&Requester=SBN&tracknum=${parcel.trackingID}&AgreeToTermsAndConditions=yes/trackdetails`;
    } else if (parcel.courier === 'yunexpress') {
      return `https://m.yuntrack.com/parcelTracking?id=${parcel.trackingID}`;
    } else if (parcel.courier === 'gls') {
      return `https://www.gls-portugal.pt/pt/seguimiento-envio/?match=${parcel.trackingID}&international=1`
    }
  }

  return (
    <div className={`card ${isDarkMode ? 'text-white card-background-dark' : 'text-black card-background-light'} p-4 rounded-lg shadow-md mb-4 flex flex-col justify-between p-30`}>
      <h3 className="text-xl font-semibold mb-2 relative text-center flex items-center">
        <img src={`/${parcel.courier}.png`} alt={parcel.courier} className="mr-2 courier-logo" /> {parcel.label}
        <div className='absolute top-0 right-0'>
          <div className='flex flex-col'>
            <a href={trackingLinkBuilder(parcel)} target="_blank" rel="noopener noreferrer">
              <i className={`fa fa-external-link ${isDarkMode ? 'text-gray-300' : 'text-gray-600'} hover:text-blue-500`} style={{ cursor: 'pointer' }}></i>
            </a>
            <a onClick={() => handleDeleteClick(parcel.id)}>
              <i className={`fa fa-trash ${isDarkMode ? 'text-gray-300' : 'text-gray-600'} hover:text-blue-500`} style={{ cursor: 'pointer' }}></i>
            </a>
          </div>
        </div>
      </h3>
      <div className="mb-2">
         {parcel.lastUpdateDate && <p><strong>Last Update Date</strong>: {parcel.lastUpdateDate}</p>}
         {parcel.lastUpdateTime && <p><strong>Last Update Time</strong>: {parcel.lastUpdateTime}</p>}
         {parcel.location && <p><strong>Location</strong>: {parcel.location}</p>}
         {parcel.description && <p><strong>Description</strong>: {parcel.description}</p>}
         {parcel.leftAt && <p><strong>Left At</strong>: {parcel.leftAt}</p>}
         {parcel.receptorName && <p><strong>Receptor Name</strong>: {parcel.receptorName}</p>}
         {parcel.reason && <p><strong>Reason</strong>: {parcel.reason}</p>}
      </div>
      <div className="mt-4 flex">
        <button
          className={`cursor-pointer border-solid border-2 hover:text-blue-700 ${isDarkMode ? 'text-white' : 'text-black'} px-3 py-1 rounded-lg`}
          onClick={() => handleUpdateClick(parcel.id)}
          style={{borderColor: `${isDarkMode ? '#232b54' : '#7faef5'}`}}
        >
          Update
        </button>
        <div className={`text-sm ${isDarkMode ? 'text-gray-200' : 'text-gray-800'} ml-auto`}>
          <div className="text-center">Last checked</div>
          <div className="text-center">{timeAgo}</div>
        </div>
      </div>
      <div className={`h-4 mt-4 relative ${getProgressColorClass(1)} rounded-lg`}>
        <div
          className={`h-full ${getProgressColorClass(0)} rounded-lg`}
          style={{width: `${progressValue}%`}}
        ></div>
      </div>
    </div>
  );
};

export default ParcelItem;
