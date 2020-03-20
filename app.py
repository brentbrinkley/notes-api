from flask_api import FlaskAPI
from controllers.notes_controller import get_notes, get_scales

# Cofig

app = FlaskAPI(__name__)
debug = True

# Routes
@app.route("/")
def index():
    return get_notes()


@app.route("/scales-<string:shape>-<string:scale>")
def scales(shape, scale):
    return get_scales(shape, scale)


if __name__ == "__main__":
    app.run(debug=True)
