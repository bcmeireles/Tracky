from flask import jsonify, make_response, request
from scrapers import gls as glsScraper

def create_routes(app):
    @app.route('/getTracking/gls', methods=['GET'])
    def glsTracker():
        trackingID = request.args.get('trackingID')
        data = glsScraper.trackGLS(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)