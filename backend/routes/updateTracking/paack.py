from flask import jsonify, make_response, request
from scrapers import paack as paackScraper
from db import mongo
import time

def create_routes(app):
    @app.route('/updateTracking/paack', methods=['POST'])
    def paackUpdater():
        data = request.get_json()
        uid = data.get('uid')
        trackingID = data.get('trackingID')
        postalCode = mongo.getPaackPostal(trackingID)

        data = paackScraper.trackPaack(trackingID, postalCode)

        if data['requestStatus'] == 'success':
            del data['requestStatus']
            data['lastChecked'] = int(time.time())
            mongo.updateParcel(uid, trackingID, 'paack', data)

            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)