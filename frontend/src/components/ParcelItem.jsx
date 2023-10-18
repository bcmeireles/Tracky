import React from 'react';
import './ParcelItem.css'

const getFieldLabel = (fieldName) => {
  return fieldName.replace(/([A-Z])/g, ' $1').replace(/^./, (str) => str.toUpperCase());
};

const ParcelItem = ({ parcel }) => {
  return (
    <div className="card bg-white shadow-md rounded-md p-4 mb-4">
      <div className="flex flex-col">
        <h2 className='text-center text-lg font-bold'>{parcel.label}</h2>
        {Object.keys(parcel).map((field, index) => (
          field !== "label" && field !== "_id" && field !== "ownerUID" &&
          <p key={index} className='mb-1'>{getFieldLabel(field)}: {parcel[field]}</p>
        ))}
      </div>
    </div>
  );
};

export default ParcelItem;
