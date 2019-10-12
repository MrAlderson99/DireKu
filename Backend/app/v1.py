from . import database
from dotenv import load_dotenv  # Development ONLY to be removed in production
from flask import Blueprint, jsonify, request
import os  # Development ONLY to be removed in production
from uuid import uuid4

bp = Blueprint('v1', __name__, url_prefix="/api/v1")


# Verifies API KEY
@bp.before_request
def check_api_key():
    """ Checks API Key can submit data
    Parameters:
        None
    """
    if request.method in ["POST", "PUT", "DELETE"]:

        try:

            request.headers["API-Key"]

        except KeyError:

            return send_response(400)

        # API_KEY is for development ONLY. Update with user account tokens
        if request.headers["API-Key"] != os.getenv("API_KEY"):

            return send_response(401)


# Index Endpoint
@bp.route('/')
def index():
    """ Index of API v1
    Parameters:
        None
    """
    return send_response(200)


def send_response(status_code, method=None, data=None):
    """ Sends JSON Response
    Parameters:
        status_code (integer): Status Code to send to client.
        method (string): Method used on API Endpoint.
        data (JSON): Data to be returned to client.
    """
    json_response = {}

    if status_code == 200 and method is None and data is None:

        json_response["status"] = "Ok"
        json_response["message"] = "Request successful"

    if status_code == 200 and method == "GET" and data is not None:

        return jsonify(data), status_code

    if status_code == 200 and method == "PUT" and data is None:

        json_response["status"] = "Ok"
        json_response["message"] = "Object successfully updated"

    if status_code == 200 and method == "DELETE" and data is None:

        json_response["status"] = "Ok"
        json_response["message"] = "Object successfully deleted"

    if status_code == 201:

        json_response["status"] = "Created"
        json_response["message"] = "Object successfully created"

    if status_code == 400:

        json_response["status"] = "Bad Request"
        json_response["message"] = "Invalid request or parameters"

    if status_code == 401:

        json_response["status"] = "Unauthorized"
        json_response["message"] = "Invalid credentials"

    if status_code == 404:

        json_response["status"] = "Not Found"
        json_response["message"] = "Requested object was not found"

    if status_code == 405:

        json_response["status"] = "Method Not Allowed"
        json_response["message"] = "Disallowed method used on this endpoint"

    return jsonify(json_response), status_code
