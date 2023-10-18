from flask import Flask
from flask_cors import CORS
from routes.getTracking import ctt, ups, paack, yunexpress, correosexpress
from routes.parcels import getParcels, createParcel, deleteParcel, updateParcel, getParcel
from routes.updateTracking import ctt as cttUpdater
from routes.updateTracking import ups as upsUpdater
from routes.updateTracking import paack as paackUpdater
from routes.updateTracking import yunexpress as yunexpressUpdater
from routes.updateTracking import correosexpress as correosexpressUpdater


app = Flask(__name__)
CORS(app)

ctt.create_routes(app)
ups.create_routes(app)
paack.create_routes(app)
yunexpress.create_routes(app)
correosexpress.create_routes(app)

getParcels.create_routes(app)
createParcel.create_routes(app)
deleteParcel.create_routes(app)
updateParcel.create_routes(app)
getParcel.create_routes(app)

cttUpdater.create_routes(app)
upsUpdater.create_routes(app)
paackUpdater.create_routes(app)
yunexpressUpdater.create_routes(app)
correosexpressUpdater.create_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
