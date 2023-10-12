from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['tracky']

class CTT:
    def __init__(self, status):
        self.status = status # delivered, in-progress, ...

    def save(self):
        db['ctt'].insert_one(self.__dict__)

    def update(self):
        db['ctt'].update_one({'_id': self._id}, {'$set': self.__dict__})

    @classmethod
    def find_by_id(cls, post_id):
        package_data = db['ctt'].find_one({'_id': post_id})
        if package_data:
            return cls(**package_data)
        return None