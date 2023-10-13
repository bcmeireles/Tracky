from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['tracky']

class PAACK:
    def __init__(self, trackingID, postalCode, ownerUID, status="unverified"):
        self.trackingID = trackingID
        self.postalCode = postalCode
        self.ownerUID = ownerUID
        self.status = status
        self.description = None
        self.estimated = None

    def save(self):
        db['paack'].insert_one(self.__dict__)

    @classmethod
    def update(cls, trackingID, newDetails):
        db['paack'].update_one({'trackingID': trackingID}, {'$set': newDetails})

    @classmethod
    def find_by_id(cls, trackingID):
        package_data = db['paack'].find_one({'trackingID': trackingID})
        if package_data:
            return package_data
        return None