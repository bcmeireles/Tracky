from flask import jsonify, make_response
from scrapers import paack

def create_routes(app):
    @app.route('/getTracking/ctt')
    def paackTracker():
        data = paack.trackPaack()
        if data['requestStatus'] == 'requestStatus':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)