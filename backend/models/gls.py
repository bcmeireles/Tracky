from db.mongo import client

db = client['tracky']

class GLS:
    def __init__(self, label, trackingID, ownerUID, status="unverified"):
        self.label = label
        self.trackingID = trackingID
        self.ownerUID = ownerUID
        self.courier = "gls"
        self.status = status
        self.lastUpdateDate = None
        self.lastUpdateTime = None
        self.description = None
        self.location = None
        self.lastChecked = None

    def save(self):
        db['gls'].insert_one(self.__dict__)