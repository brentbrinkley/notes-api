from flask_api import FlaskAPI
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

DEBUG = True

app = FlaskAPI(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/notes_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

CORS(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String, nullable=False)
    shape = db.Column(db.String, nullable=False)
    midi_val = db.Column(db.Integer, nullable=False)
    common_notation = db.Column(db.String, nullable=False)
    svg = db.Column(db.String, nullable=False)
    note_filtered = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"note number: {self.midi_val}, note color: {self.color}, note shape: {self.shape}"
