import os
from flask import Flask
from flask_cors import CORS
from uuid import uuid4


def create_app():
    """ Creates a Flask Application Factory
    Parameters:
        None
    """
    app = Flask(__name__)
    CORS(app)

    app.config.from_mapping(
        SECRET_KEY=uuid4().hex
    )

    # Imports
    from . import v1
    app.register_blueprint(v1.bp)

    # Initializes the application
    return app
