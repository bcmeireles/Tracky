from flask import Flask
from flask_cors import CORS
from routes.getDetails import ctt, ups, paack

app = Flask(__name__)
CORS(app)

ctt.create_routes(app)
ups.create_routes(app)
paack.create_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
