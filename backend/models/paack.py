from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
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

    @classmethod
    def update(cls, trackingID, newDetails):
        try:
            db['paack'].update_one({'trackingID': trackingID}, {'$set': json.loads(newDetails)})
            return True
        except:
            return False
        
    @classmethod
    def find_by_id(cls, trackingID):
        package_data = db['paack'].find_one({'trackingID': trackingID})
        if package_data:
            return package_data
        return None