import React from 'react';
import ParcelItem from './ParcelItem';

function ParcelContainer({ parcels, onDeleteParcel, onUpdateParcel }) {
    return (
        <div className="container h-screen m-0">
            {parcels.map((parcel, index) => (
                <ParcelItem
                    key={index}
                    parcel={parcel}
                    onDeleteParcel={onDeleteParcel}
                    onUpdateParcel={onUpdateParcel}
                />
            ))}
        </div>
    );
}

export default ParcelContainer;