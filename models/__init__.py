from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'TV',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)


# db.init_app(app)

class ItemInfo(db.Document):
    title = db.StringField()
    url = db.StringField()
    person_num = db.IntField()
    cate = db.StringField()
    anchor = db.StringField()
    data_from = db.StringField()
    img_name = db.StringField()
    img_url = db.StringField()
    meta = {'collection': 'anytv_info'}
