from db import mongo
from flask import jsonify, make_response, request

def create_routes(app):
    @app.route('/parcels/update', methods=['PUT'])
    def updateParcel():
        uid = request.form.get('uid')
        trackingID = request.form.get('trackingID')
        courier = request.form.get('courier')
        newDetails = request.form.get('newDetails')

        if not uid or not trackingID or not courier or not newDetails:
            return make_response({"requestStatus": "error", "message": "Missing parameters."}, 400)

        try:
            existingParcel = mongo.getParcel(uid, trackingID)

            if existingParcel:
                if mongo.updateParcel(uid, trackingID, courier, newDetails):
                    return make_response({"requestStatus": "success", "message": "Parcel updated successfully."}, 200)
                else:
                    return make_response({"requestStatus": "error", "message": "Failed to update parcel."}, 400)
            else:
                return make_response({"requestStatus": "error", "message": "Parcel not found."}, 404)
        except Exception as e:
            return make_response(jsonify({
                "requestStatus": "error",
                "message": str(e)
            }), 400)