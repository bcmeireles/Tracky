from flask import jsonify, make_response, request
from scrapers import ctt as cttScraper
from db import mongo
import time

def create_routes(app):
    @app.route('/updateTracking/ctt', methods=['POST'])
    def cttUpdater():
        uid = request.form.get('uid')
        trackingID = request.form.get('trackingID')

        data = cttScraper.trackCTT(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            data['lastChecked'] = int(time.time())
            mongo.updateParcel(uid, trackingID, 'ctt', data)

            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)