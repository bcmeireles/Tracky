from db import mongo
from flask import jsonify, make_response, request

def create_routes(app):
    @app.route('/parcels/create', methods=['POST'])
    def createParcel():
        data = request.get_json()
        label = data.get('label')
        uid = data.get('uid')
        trackingID = data.get('trackingID')
        courier = data.get('courier')
        postalCode = data.get('postalCode')

        print(label, uid, trackingID, courier)

        if not label or not uid or not trackingID or not courier:
            return make_response(jsonify({"requestStatus": "error", "message": "Missing parameters."}), 400)

        try:
            if mongo.createParcel(label, uid, trackingID, courier, postalCode):
                return make_response(jsonify({"requestStatus": "success", "message": "Parcel created successfully."}), 200)
            else:
                return make_response(jsonify({"requestStatus": "error", "message": "Failed to create parcel."}), 400)
        except Exception as e:
            return make_response(jsonify({
                "requestStatus": "error",
                "message": str(e)
            }), 400)