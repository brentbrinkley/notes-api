from model import *

from scales import Scale

####################################################
# Index
####################################################


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
        for note in Note.query.all()
    ]

    return {"notes": notes}


####################################################
# Scales
####################################################


@app.route("/scales-<string:shape>-<string:scale>")
def scales(shape, scale):
    """Scaled version of our notes database that returns a note databank sorted by scale"""

    notes = Scale.get_scale(Note, shape, scale)

    scaled_notes = [note for note in Note.query.all() if note.shape in notes]

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

    return {"notes": scaled_db, "count": len(scaled_db)}

