from pymongo import MongoClient
from db.mongo import client

db = client['tracky']

class UPS:
    def __init__(self, label, trackingID, ownerUID, status="unverified"):
        self.label = label
        self.trackingID = trackingID
        self.ownerUID = ownerUID
        self.courier = "ups"
        self.status = status
        self.lastUpdateDate = None
        self.lastUpdateTime = None
        self.description = None
        self.location = None
        self.leftAt = None
        self.progress = None
        self.lastChecked = None

    def save(self):
        db['ups'].insert_one(self.__dict__)