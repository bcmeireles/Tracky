from flask import jsonify, make_response, request
from scrapers import yunexpress

def create_routes(app):
    @app.route('/getTracking/yunexpress', methods=['GET'])
    def yunexpressTracker():
        trackingID = request.args.get('trackingID')

        if not trackingID:
            return make_response({"requestStatus": "error", "message": "Missing 'trackingID' parameter."}, 400)

        data = yunexpress.trackYunexpress(trackingID)

        if data['requestStatus'] == 'success':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)