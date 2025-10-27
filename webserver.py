# webserver.py
from flask import Flask
from threading import Thread
import os

app = Flask(__name__)
_server_started = False

@app.route("/")
def home():
    return "Bot simulator alive!"

def _run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    global _server_started
    if _server_started:
        return
    t = Thread(target=_run, daemon=True)
    t.start()
    _server_started = True
