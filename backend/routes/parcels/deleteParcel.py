from db import mongo
from flask import jsonify, make_response, request

def create_routes(app):
    @app.route('/parcels/delete', methods=['DELETE'])
    def deleteParcel():
        data = request.get_json()
        uid = data.get('uid')
        trackingID = data.get('trackingID')
        courier = data.get('courier')

        if not uid or not trackingID or not courier:
            return make_response(jsonify({"requestStatus": "error", "message": "Missing parameters."}), 400)

        try:
            if mongo.deleteParcel(uid, trackingID, courier):
                return make_response(jsonify({"requestStatus": "success", "message": "Parcel deleted successfully."}), 200)
            else:
                return make_response(jsonify({"requestStatus": "error", "message": "Failed to delete parcel."}), 400)
        except Exception as e:
            return make_response(jsonify({
                "requestStatus": "error",
                "message": str(e)
            }), 400)