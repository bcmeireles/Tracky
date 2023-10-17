from flask import jsonify, make_response, request
from scrapers import paack

def create_routes(app):
    @app.route('/getTracking/paack', methods=['GET'])
    def paackTracker():
        trackingID = request.args.get('trackingID')
        postalCode = request.args.get('postalCode')
        
        if not trackingID or not postalCode:
            return make_response({"requestStatus": "error", "message": "Missing 'trackingID' and/or 'postalCode' parameters."}, 400)
        
        data = paack.trackPaack(trackingID, postalCode)
        
        if data['requestStatus'] == 'success':
            del data['requestStatus']
            return make_response(jsonify(data), 200)
        else:
            return make_response(jsonify(data), 400)
