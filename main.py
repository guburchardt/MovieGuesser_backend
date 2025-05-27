from flask import Flask
from flask_cors import CORS
from src.interfaces.api.routes import api
from src.infrastructure.config.settings import settings

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.register_blueprint(api, url_prefix='/api')
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=settings.DEBUG) 