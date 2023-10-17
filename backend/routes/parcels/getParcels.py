from db import mongo
from flask import jsonify, make_response, request

def create_routes(app):
    @app.route('/parcels/get', methods=['GET'])
    def getParcels():
        uid = request.args.get('uid')

        if not uid:
            return make_response({"requestStatus": "error", "message": "Missing 'uid' parameter."}, 400)
        
        try:
            data = mongo.getAllParcels(uid)

            response = {
                "requestStatus": "success",
                "parcelCount": len(data),
                "parcels": data
            }

            return make_response(jsonify(response), 200)
        
        except Exception as e:
            return make_response(jsonify({
                "requestStatus": "error",
                "message": str(e)
            }), 400)