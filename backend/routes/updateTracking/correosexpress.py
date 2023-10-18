from flask import jsonify, make_response, request
from scrapers import correosexpress as correosexpressScraper
from db import mongo
import time

def create_routes(app):
    @app.route('/updateTracking/correosexpress', methods=['POST'])
    def correosexpressUpdater():
        data = request.get_json()
        uid = data.get('uid')
        trackingID = data.get('trackingID')

        data = correosexpressScraper.trackCORREOSEXPRESS(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            data['lastChecked'] = int(time.time())
            mongo.updateParcel(uid, trackingID, 'correosexpress', data)

            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)