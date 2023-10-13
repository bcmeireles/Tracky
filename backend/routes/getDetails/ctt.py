from flask import jsonify, make_response
from scrapers import ctt

def create_routes(app):
    @app.route('/getTracking/ctt')
    def cttTracker():
        data = ctt.trackCTT()
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)