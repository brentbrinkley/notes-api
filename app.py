from flask_api import FlaskAPI
import model
from scales import Scale

DEBUG = True
app = FlaskAPI(__name__)


@app.route("/")
def index():
    """Return our database"""

    notes = [
        {
            "midi": note.midi_val,
            "color": note.color,
            "shape": note.shape,
            "hex": note.hex,
            "common": note.common_notation,
        }
        for note in model.Note.select()
    ]

    return {"notes": notes}


@app.route("/scales-<string:shape>-<string:scale>")
def scales(shape, scale):
    notes = Scale.get_scale(shape, scale)

    scaled_notes = [note for note in model.Note.select() if note.shape in notes]

    scaled_db = [
        {
            "midi": note.midi_val,
            "color": note.color,
            "shape": note.shape,
            "hex": note.hex,
            "common": note.common_notation,
        }
        for note in scaled_notes
    ]

    return {
        "title": f"This is the {shape} {scale} scale",
        "notes": scaled_db,
        "count": len(scaled_db),
    }


if __name__ == "__main__":
    app.run(debug=DEBUG)
