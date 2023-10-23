from flask import jsonify, make_response, request
from scrapers import gls as glsScraper
from db import mongo
import time

def create_routes(app):
    @app.route('/updateTracking/gls', methods=['POST'])
    def glsUpdater():
        data = request.get_json()
        uid = data.get('uid')
        trackingID = data.get('trackingID')

        data = glsScraper.trackGLS(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            data['lastChecked'] = int(time.time())
            mongo.updateParcel(uid, trackingID, 'gls', data)

            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)