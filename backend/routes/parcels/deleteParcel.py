from db import mongo
from flask import jsonify, make_response, request

def create_routes(app):
    @app.route('/deleteParcel', methods=['POST'])
    def deleteParcel():
        uid = request.form.get('uid')
        trackingID = request.form.get('trackingID')
        courier = request.form.get('courier')

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