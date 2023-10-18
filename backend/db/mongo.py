from pymongo import MongoClient
import json
from models.ctt import CTT
from models.paack import PAACK
from models.ups import UPS
from models.yunexpress import YUNEXPRESS
from models.correosexpress import CORREOSEXPRESS

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

def createParcel(label, uid, trackingID, courier):
    if courier == 'ctt':
        parcelObj = CTT(label, trackingID, uid)
        parcelObj.save()
    
    elif courier == 'paack':
        parcelObj = PAACK(label, trackingID, uid)
        parcelObj.save()

    elif courier == 'ups':
        parcelObj = UPS(label, trackingID, uid)
        parcelObj.save()

    elif courier == 'yunexpress':
        parcelObj = YUNEXPRESS(label, trackingID, uid)
        parcelObj.save()

    elif courier == 'correosexpress':
        parcelObj = CORREOSEXPRESS(label, trackingID, uid)
        parcelObj.save()

    return True

def deleteParcel(uid, trackingID, courier):
    try:
        db[courier].delete_one({'trackingID': trackingID, 'ownerUID': uid})
        return True
    except:
        return False
    

def updateParcel(uid, trackingID, courier, newDetails):
    try:    
        db[courier].update_one({'trackingID': trackingID}, {'$set': newDetails})
        return True
    except Exception as e:
        print(e)
        return False

def find_by_id(trackingID, courier):
    package_data = db[courier].find_one({'trackingID': trackingID})
    if package_data:
        return package_data
    return None