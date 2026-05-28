import os
from pathlib import Path

from flask import Flask, send_file, abort

os.chdir(Path(__file__).parent.resolve())

app = Flask(__name__)


@app.route("/sub/<uid>")
def sub(uid):
    path = f"generator/data/subs/{uid}.yaml"

    try:
        return send_file(
            path,
            mimetype="text/yaml"
        )
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000
    )
