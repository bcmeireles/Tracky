from flask import Flask
from flask_cors import CORS
from routes.getTracking import ctt, ups, paack, yunexpress
from routes.parcels import getParcels, createParcel, deleteParcel, updateParcel

app = Flask(__name__)
CORS(app)

ctt.create_routes(app)
ups.create_routes(app)
paack.create_routes(app)
yunexpress.create_routes(app)

getParcels.create_routes(app)
createParcel.create_routes(app)
deleteParcel.create_routes(app)
updateParcel.create_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
