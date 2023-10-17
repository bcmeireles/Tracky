from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['tracky']

class CORREOSEXPRESS:
    def __init__(self, label, trackingID, ownerUID, status="unverified"):
        self.label = label
        self.trackingID = trackingID
        self.ownerUID = ownerUID
        self.courier = "correosexpress"
        self.status = status
        self.lastUpdateDate = None
        self.lastUpdateTime = None
        self.description = None
        self.location = None
        self.lastChecked = None

    def save(self):
        db['correosexpress'].insert_one(self.__dict__)

    @classmethod
    def update(cls, trackingID, newDetails):
        try:    
            db['correosexpress'].update_one({'trackingID': trackingID}, {'$set': json.loads(newDetails)})
            return True
        except:
            return False

    @classmethod
    def find_by_id(cls, trackingID):
        package_data = db['correosexpress'].find_one({'trackingID': trackingID})
        if package_data:
            return package_data
        return None