from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['tracky']

class UPS:
    def __init__(self, trackingID, ownerUID, status="unverified"):
        self.trackingID = trackingID
        self.ownerUID = ownerUID
        self.status = status
        self.lastUpdateDate = None
        self.lastUpdateTime = None
        self.description = None
        self.location = None
        self.leftAt = None
        self.progress = None

    def save(self):
        db['ups'].insert_one(self.__dict__)

    @classmethod
    def update(cls, trackingID, newDetails):
        db['ups'].update_one({'trackingID': trackingID}, {'$set': newDetails})

    @classmethod
    def find_by_id(cls, trackingID):
        package_data = db['ups'].find_one({'trackingID': trackingID})
        if package_data:
            return package_data
        return None