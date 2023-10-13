from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['tracky']

class CTT:
    def __init__(self, trackingID, ownerUID, status="unverified"):
        self.trackingID = trackingID
        self.ownerUID = ownerUID
        self.status = status
        self.lastUpdateDate = None
        self.lastUpdateTime = None
        self.description = None
        self.location = None
        self.reason = None
        self.receptorName = None
        self.progress = None

    def save(self):
        db['ctt'].insert_one(self.__dict__)

    @classmethod
    def update(cls, trackingID, newDetails):
        db['ctt'].update_one({'trackingID': trackingID}, {'$set': newDetails})

    @classmethod
    def find_by_id(cls, trackingID):
        package_data = db['ctt'].find_one({'trackingID': trackingID})
        if package_data:
            return package_data
        return None