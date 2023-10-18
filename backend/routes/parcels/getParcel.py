from db import mongo
from flask import jsonify, make_response, request

def create_routes(app):
    @app.route('/parcels/getone', methods=['GET'])
    def getParcel():
        id = request.args.get('id')
        courier = request.args.get('courier')

        if not id or not courier:
            return make_response({"requestStatus": "error", "message": "Missing parameters."}, 400)
        
        try:
            data = mongo.getParcel(courier, id)

            response = {
                "requestStatus": "success",
                "parcel": data
            }

            return make_response(jsonify(response), 200)
        
        except Exception as e:
            return make_response(jsonify({
                "requestStatus": "error",
                "message": str(e)
            }), 400)