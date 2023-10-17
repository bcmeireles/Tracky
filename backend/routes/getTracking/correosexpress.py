from flask import jsonify, make_response, request
from scrapers import correosexpress as correosexpressScraper

def create_routes(app):
    @app.route('/getTracking/correosexpress', methods=['GET'])
    def correosexpressTracker():
        trackingID = request.args.get('trackingID')
        data = correosexpressScraper.trackCORREOSEXPRESS(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)