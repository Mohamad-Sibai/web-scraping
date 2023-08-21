import json

from bson import json_util
from bson.json_util import dumps
from flask import Flask, render_template, jsonify
from flask_cors import CORS

from pymongo import MongoClient

app = Flask(__name__)
cors = CORS(app)

@app.route('/data')
def index():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['db_news']
    collection = db['articles']
    data = collection.find()
    list_cur = list(data)
    json_data = dumps(list_cur)
    #json_data = json.loads(data)
    return json_data
    ##return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
