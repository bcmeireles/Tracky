import React from 'react';
import ParcelItem from './ParcelItem';

function ParcelContainer({ parcels, onDeleteParcel, onUpdateParcel, isDarkMode }) {
  return (
    <div className="container mx-auto mt-8">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-4 pl-8 pr-8">
        {parcels.map((parcel, index) => (
          <ParcelItem
            key={index}
            parcel={parcel}
            onDeleteParcel={onDeleteParcel}
            onUpdateParcel={onUpdateParcel}
            isDarkMode={isDarkMode}
          />
        ))}
      </div>
    </div>
  );
}

export default ParcelContainer;
