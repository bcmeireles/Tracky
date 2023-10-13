from flask import jsonify, make_response
from scrapers import yunexpress

def create_routes(app):
    @app.route('/getTracking/yunexpress')
    def yunexpressTracker():
        data = yunexpress.trackYunexpress()
        if data['requestStatus'] == 'requestStatus':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)