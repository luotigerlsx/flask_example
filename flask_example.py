# -*- coding:utf-8 -*-

import json
import logging

from flask import Flask, url_for, request, render_template
from flask import redirect, make_response, jsonify, abort

from config import DevelopmentConfig
from app.module_one import bp_module_one
from authentic import requires_auth

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(bp_module_one, url_prefix='/module_one_prefix')


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/')
def login():
    return redirect(url_for('module_one.module_one_index'))


@app.route('/users/<int:userid>', methods=['GET'])
@requires_auth
def api_users(userid):
    users = {'1': 'john', '2': 'steve', '3': 'bill'}

    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        abort(404)


@app.route('/messages', methods=['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
