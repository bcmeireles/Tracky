from flask import jsonify, make_response, request
from scrapers import ups

def create_routes(app):
    @app.route('/getTracking/ups', methods=['GET'])
    def upsTracker():
        trackingID = request.args.get('trackingID')
        data = ups.trackUPS(trackingID)
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)