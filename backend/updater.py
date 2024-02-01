import db.mongo as mongo
import time

from scrapers import ctt as cttScraper
from scrapers import ups as upsScraper

db = mongo.db

for collection in db.list_collection_names():
    for parcel in db[collection].find():
        print(parcel)
        if parcel["courier"] == "ctt":
            print("Updating CTT parcel: " + parcel["trackingID"])
            data = cttScraper.trackCTT(parcel["trackingID"])
            if data['requestStatus'] == 'success':
                del data['requestStatus']
                data['lastChecked'] = int(time.time())
                mongo.updateParcel(parcel["ownerUID"], parcel["trackingID"], 'ctt', data)
            else:
                print("Error updating parcel: " + parcel["trackingID"])
        elif parcel["courier"] == "ups":
            print("Updating UPS parcel: " + parcel["trackingID"])
            data = upsScraper.trackUPS(parcel["trackingID"])
            if data['requestStatus'] == 'success':
                del data['requestStatus']
                data['lastChecked'] = int(time.time())
                mongo.updateParcel(parcel["ownerUID"], parcel["trackingID"], 'ups', data)
            else:
                print("Error updating parcel: " + parcel["trackingID"])