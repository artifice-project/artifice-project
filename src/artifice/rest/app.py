import os
import dill
import datetime
from pprint import pprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask import (
    Flask,
    jsonify,
    request
)
# custom modules


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = "sqlite:///{}".format(os.path.join(BASE_DIR, "site.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_FILE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Egg_db(db.Model, SerializerMixin):
    """
    For ease of standardization, any field which handles a list is
    converted to a string object. When retrieving
    data, this operation is reversed.
    """
    __tablename__ = "egg"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow())
    url = db.Column(db.String(500), unique=False)
    egg = db.Column(db.Text, unique=False, nullable=False)

    @staticmethod
    def serialize(arg):
        return dill.dumps(arg)

    @staticmethod
    def deserialize(arg):
        return dill.loads(arg)


@app.route("/")
def home():
    return "HELLO WORLD"


@app.route("/update", methods=["POST"])
def egg_update():
    data = request.get_json()
    egg = {
        "url" : data["url"],
        "egg" : Egg_db.serialize(data)
    }
    try:
        cls = Egg_db(**egg)
        db.session.add(cls)
        db.session.commit()
        msg, status = "PASS", 200
    except:
        msg, status = "FAIL", 400
    return msg, status


@app.route("/retrieve", methods=["GET"])
def egg_retrieve():
    results = Egg_db.query.all()
    eggs = []
    if results:
        for result in results:
            r = result.to_dict()
            egg = Egg_db.deserialize(r["egg"])
            eggs.append(egg)
    return jsonify(eggs)
