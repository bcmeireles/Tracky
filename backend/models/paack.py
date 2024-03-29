from pymongo import MongoClient
from db.mongo import client

db = client['tracky']

class PAACK:
    def __init__(self, label, trackingID, postalCode, ownerUID, status="unverified"):
        self.label = label
        self.trackingID = trackingID
        self.postalCode = postalCode
        self.ownerUID = ownerUID
        self.courier = "paack"
        self.status = status
        self.description = None
        self.estimated = None
        self.lastChecked = None

    def save(self):
        db['paack'].insert_one(self.__dict__)