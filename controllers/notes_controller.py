import models.note_model as model
from helpers.scales import Scale


def get_notes():
    """Snags the values from our database
    
    Returns:
        dictionary -- gives us back a dictionary of our note values in an arry
    """

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
    """Gets our note data based on a root note and scale
    
    Arguments:
        shape {string} -- takes a shape string based on various note values
        scale {string} -- takes a scale based on most of known music scales
    
    Returns:
        dictionary -- returns our scaled note value along with other helpful data
    """ """Gets our notes organized based on root note and scale"""
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
