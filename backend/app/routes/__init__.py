from flask import Blueprint

main = Blueprint('main', __name__)

from app.routes.auth import auth_bp

@main.route('/')
def index():
    return {'message': 'Give_Get API is running'}
