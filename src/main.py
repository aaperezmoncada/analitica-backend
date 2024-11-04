import os
import traceback
import logging
import time

from flask import Flask, jsonify
from flask_cors import CORS
from src.blueprints.services import services_bp

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

def create_app(config_name, local=False):
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(services_bp, url_prefix='/analitica')
    app_context = app.app_context()
    app_context.push()

    @app.errorhandler(Exception)
    def handle_exception(err):
        trace = traceback.format_exc()
        logger.info("Log error: " + str(trace))
        return jsonify({"message": err.description}), err.code

    return app

app = create_app('analitica')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)