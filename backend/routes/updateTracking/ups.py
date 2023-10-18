from flask import jsonify, make_response, request
from scrapers import ups as upsScraper
from db import mongo
import time

def create_routes(app):
    @app.route('/updateTracking/ups', methods=['POST'])
    def upsUpdater():
        data = request.get_json()
        uid = data.get('uid')
        trackingID = data.get('trackingID')

        data = upsScraper.trackUPS(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            data['lastChecked'] = int(time.time())
            mongo.updateParcel(uid, trackingID, 'ups', data)

            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)