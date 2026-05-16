from flask import request

from hello_world import app
from hello_world.formater import PLAIN, SUPPORTED, get_formatted


MOJE_IMIE = "Michal "
MSG = "Hello World!"


@app.route("/")
def index():
    output = request.args.get("output", PLAIN)
    return get_formatted(MSG, MOJE_IMIE, output.lower())


@app.route("/outputs")
def supported_output():
    return ", ".join(SUPPORTED)
