# backend/run.py
from flask import Flask, send_from_directory
from api.api import api_bp
from api.db import db
from api.config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(api_bp, url_prefix="/api")

    # Serve images from frontend/images folder
    @app.route("/images/<path:filename>")
    def serve_image(filename):
        image_path = os.path.join(os.getcwd(), "../frontend/images")
        return send_from_directory(image_path, filename)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
