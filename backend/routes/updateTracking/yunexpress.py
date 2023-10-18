from flask import jsonify, make_response, request
from scrapers import yunexpress as yunexpressScraper
from db import mongo
import time

def create_routes(app):
    @app.route('/updateTracking/yunexpress', methods=['POST'])
    def yunexpressUpdater():
        uid = request.form.get('uid')
        trackingID = request.form.get('trackingID')

        data = yunexpressScraper.trackYunexpress(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            data['lastChecked'] = int(time.time())
            mongo.updateParcel(uid, trackingID, 'yunexpress', data)

            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)