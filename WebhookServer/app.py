from flask import Flask, Response, jsonify, redirect, render_template, request
from WebhookServer.utilies import log
from config_priv import client_id, client_secret, scope
import requests

app = Flask(__name__)


@app.route("/login", methods=['GET'])
def login():
    state = "state"  # ???
    url = f"https://todoist.com/oauth/authorize?client_id={client_id}&scope={scope}&state={state}"
    return redirect(url, code=302)


@app.route("/access_token", methods=['GET'])
def access_token():
    code = request.args.get("code")
    state = request.args.get("state")
    requests.post("https://todoist.com/oauth/access_token", json={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code
    })
    return render_template('base.html', content="Verified")


@app.route("/payload", methods=['GET', 'POST'])
def payload():
    log()
    return jsonify({'status': 'accepted', 'health': 'ok'}), 200
