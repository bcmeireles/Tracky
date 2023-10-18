import React from 'react'
import ParcelItem from './ParcelItem'


function ParcelContainer({parcels}) {
  return (
    <div className="container h-screen m-0">
        {parcels.map((parcel, index) => (
              <ParcelItem key={index} parcel={parcel} />
            ))}
    </div>
  )
}

export default ParcelContainer