from flask import jsonify, make_response, request
from scrapers import ctt as cttScraper

def create_routes(app):
    @app.route('/getTracking/ctt', methods=['GET'])
    def cttTracker():
        trackingID = request.args.get('trackingID')
        data = cttScraper.trackCTT(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)