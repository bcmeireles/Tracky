from flask import jsonify, make_response
from scrapers import ups

def create_routes(app):
    @app.route('/getTracking/ups')
    def upsTracker():
        data = ups.trackUPS()
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)