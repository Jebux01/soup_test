import os
from flask import Flask, request
from middleware import validate_request
from controllers.controller_soup import search_words_in_matrix

app = Flask(__name__)


@app.route("/healthcheck", methods=["GET"])
def healtcheck():
    return "OK"


@app.post("/soup")
@validate_request
def soup():
    return search_words_in_matrix(**request.get_json())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host="0.0.0.0", port=port)
