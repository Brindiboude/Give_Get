from flask import Blueprint, request, jsonify
from app import db
from app.models import Item
from flask_jwt_extended import jwt_required, get_jwt_identity

items_bp = Blueprint('items', __name__)

@items_bp.route('/items', methods=['GET'])
def get_items():
    category = request.args.get('category')
    condition = request.args.get('condition')
    
    query = Item.query.filter_by(status='available')
    
    if category:
        query = query.filter_by(category=category)
    if condition:
        query = query.filter_by(condition=condition)
    
    items = query.all()
    
    return jsonify([{
        'id': item.id,
        'title': item.title,
        'description': item.description,
        'category': item.category,
        'condition': item.condition,
        'size': item.size,
        'photo_url': item.photo_url,
        'status': item.status,
        'user_id': item.user_id
    } for item in items]), 200


@items_bp.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    item = Item(
        user_id=user_id,
        title=data['title'],
        description=data.get('description'),
        category=data['category'],
        condition=data['condition'],
        size=data.get('size'),
        photo_url=data.get('photo_url'),
        status='available'
    )
    
    db.session.add(item)
    db.session.commit()
    
    return jsonify({'message': 'Item created', 'id': item.id}), 201


@items_bp.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item = Item.query.get_or_404(id)
    
    return jsonify({
        'id': item.id,
        'title': item.title,
        'description': item.description,
        'category': item.category,
        'condition': item.condition,
        'size': item.size,
        'photo_url': item.photo_url,
        'status': item.status,
        'user_id': item.user_id
    }), 200


@items_bp.route('/items/<int:id>', methods=['PUT'])
@jwt_required()
def update_item(id):
    user_id = get_jwt_identity()
    item = Item.query.get_or_404(id)
    
    if str(item.user_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    
    item.title = data.get('title', item.title)
    item.description = data.get('description', item.description)
    item.category = data.get('category', item.category)
    item.condition = data.get('condition', item.condition)
    item.size = data.get('size', item.size)
    item.photo_url = data.get('photo_url', item.photo_url)
    
    db.session.commit()
    
    return jsonify({'message': 'Item updated'}), 200


@items_bp.route('/items/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_item(id):
    user_id = get_jwt_identity()
    item = Item.query.get_or_404(id)
    
    if str(item.user_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(item)
    db.session.commit()
    
    return jsonify({'message': 'Item deleted'}), 200
