import React from 'react';
import './ParcelItem.css'

const getFieldLabel = (fieldName) => {
  return fieldName.replace(/([A-Z])/g, ' $1').replace(/^./, (str) => str.toUpperCase());
};

const ParcelItem = ({ parcel }) => {
  return (
    <div className="card mb-4">
      <div className="icon-container p-2">
        <div className="loading-icon perpetuum-mobile"></div>
      </div>
      <div className="description p-2 d-flex flex-column">
        <h2 className='name text-center'>{parcel.label}</h2>
        {Object.keys(parcel).map((field, index) => (
          field !== "label" && field !== "_id" && field !== "ownerUID" &&
          <p key={index} className='mb-1'>{getFieldLabel(field)}: {parcel[field]}</p>
        ))}
      </div>
    </div>
  );
};

export default ParcelItem;
