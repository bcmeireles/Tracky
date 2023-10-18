from pymongo import MongoClient
from db.mongo import client

db = client['tracky']

class YUNEXPRESS:
    def __init__(self, label, trackingID, ownerUID, status="unverified"):
        self.label = label
        self.trackingID = trackingID
        self.ownerUID = ownerUID
        self.courier = "yunexpress"
        self.status = status
        self.lastUpdateDate = None
        self.lastUpdateTime = None
        self.description = None
        self.location = None
        self.lastChecked = None

    def save(self):
        db['yunexpress'].insert_one(self.__dict__)