from hashlib import sha256

from flask import Flask, jsonify, request, abort, Response

from dutchdomains.domains import get_domains

app = Flask(__name__)

KEY = "1234"

@app.route("/", methods=['POST'])
def post_index():
    """
    Request should be a POSTed json {'token': "...", 'urls': ["...", ...]}
    """
    body = request.get_json() or {}
    token = body.get('token')
    urls = body.get('urls')
    if not (token and urls):
        show_index()
    verify_token(token, urls)
    result = get_domains_dict(urls)
    return jsonify(result)

@app.route("/", methods=['GET'])
def index():
    token = request.args.get('token')
    urls = request.args.getlist('url')
    if not (token and urls):
        show_index()
    verify_token(token, urls)
    result = dict(get_domains(urls))
    return jsonify(result)


def verify_token(token, urls):
    plaintext = "|".join([KEY] + urls)
    hash = sha256(plaintext.encode('utf-8')).hexdigest()
    if token != hash:
        abort(Response('Invalid token\n', 401))


def show_index():
    abort(Response("Welcome to the Dutch domain API.\n"
                   'Please either POST with json body: {"token": "..", "urls": ["..", ..]} \n'
                   "or GET with a (repeated) url and token GET argument\n", 400))


