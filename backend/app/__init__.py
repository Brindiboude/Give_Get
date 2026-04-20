from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.routes import main
    app.register_blueprint(main)
    
    from app.models import User, Item, Exchange, Message, Review
    with app.app_context():
        db.create_all()
    
    return app
