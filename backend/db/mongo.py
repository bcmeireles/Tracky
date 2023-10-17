from pymongo import MongoClient
from models.ctt import CTT
from models.paack import PAACK
from models.ups import UPS
from models.yunexpress import YUNEXPRESS

client = MongoClient('mongodb://localhost:27017/')
db = client['tracky']

def getAllParcels(uid):
    parcels = []

    for collection in db.list_collection_names():
        for parcel in db[collection].find({'ownerUID': uid}):
            parcel['_id'] = str(parcel['_id'])
            parcels.append(parcel)

    return parcels

def getParcel(uid, trackingID):
    for collection in db.list_collection_names():
        parcel = db[collection].find_one({'trackingID': trackingID, 'ownerUID': uid})
        if parcel:
            parcel['_id'] = str(parcel['_id'])
            return parcel

    return None

def createParcel(uid, trackingID, courier):
    if courier == 'ctt':
        parcelObj = CTT(trackingID, uid)
        parcelObj.save()
    
    elif courier == 'paack':
        parcelObj = PAACK(trackingID, uid)
        parcelObj.save()

    elif courier == 'ups':
        parcelObj = UPS(trackingID, uid)
        parcelObj.save()

    elif courier == 'yunexpress':
        parcelObj = YUNEXPRESS(trackingID, uid)
        parcelObj.save()

    return True

def deleteParcel(uid, trackingID, courier):
    try:
        db[courier].delete_one({'trackingID': trackingID, 'ownerUID': uid})
        return True
    except:
        return False