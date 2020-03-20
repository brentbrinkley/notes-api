import models.note_model as model
from helpers.scales import Scale


def get_notes():
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


def get_scales(shape, scale):
    """Gets our notes organized based on root note and scale"""
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
