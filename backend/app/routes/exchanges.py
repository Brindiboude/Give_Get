from flask import Blueprint, request, jsonify
from app import db
from app.models import Exchange, Item
from flask_jwt_extended import jwt_required, get_jwt_identity

exchanges_bp = Blueprint('exchanges', __name__)

@exchanges_bp.route('/exchanges', methods=['POST'])
@jwt_required()
def create_exchange():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    item_offered = Item.query.get_or_404(data['item_offered_id'])
    item_requested = Item.query.get_or_404(data['item_requested_id'])
    
    if item_offered.status != 'available' or item_requested.status != 'available':
        return jsonify({'error': 'One or both items are not available'}), 400
    
    if str(item_offered.user_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    exchange = Exchange(
        item_offered_id=item_offered.id,
        item_requested_id=item_requested.id,
        sender_id=user_id,
        receiver_id=item_requested.user_id,
        status='pending'
    )
    
    db.session.add(exchange)
    db.session.commit()
    
    return jsonify({'message': 'Exchange proposed', 'id': exchange.id}), 201


@exchanges_bp.route('/exchanges/<int:id>', methods=['GET'])
@jwt_required()
def get_exchange(id):
    exchange = Exchange.query.get_or_404(id)
    
    return jsonify({
        'id': exchange.id,
        'item_offered_id': exchange.item_offered_id,
        'item_requested_id': exchange.item_requested_id,
        'sender_id': exchange.sender_id,
        'receiver_id': exchange.receiver_id,
        'status': exchange.status
    }), 200


@exchanges_bp.route('/exchanges/<int:id>/accept', methods=['PUT'])
@jwt_required()
def accept_exchange(id):
    user_id = get_jwt_identity()
    exchange = Exchange.query.get_or_404(id)
    
    if str(exchange.receiver_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    if exchange.status != 'pending':
        return jsonify({'error': 'Exchange is not pending'}), 400
    
    exchange.status = 'accepted'
    
    Item.query.get(exchange.item_offered_id).status = 'unavailable'
    Item.query.get(exchange.item_requested_id).status = 'unavailable'
    
    db.session.commit()
    
    return jsonify({'message': 'Exchange accepted'}), 200


@exchanges_bp.route('/exchanges/<int:id>/decline', methods=['PUT'])
@jwt_required()
def decline_exchange(id):
    user_id = get_jwt_identity()
    exchange = Exchange.query.get_or_404(id)
    
    if str(exchange.receiver_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    if exchange.status != 'pending':
        return jsonify({'error': 'Exchange is not pending'}), 400
    
    exchange.status = 'declined'
    
    db.session.commit()
    
    return jsonify({'message': 'Exchange declined'}), 200


@exchanges_bp.route('/exchanges/<int:id>/complete', methods=['PUT'])
@jwt_required()
def complete_exchange(id):
    user_id = get_jwt_identity()
    exchange = Exchange.query.get_or_404(id)
    
    if str(exchange.receiver_id) != user_id and str(exchange.sender_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    if exchange.status != 'accepted':
        return jsonify({'error': 'Exchange is not accepted'}), 400
    
    exchange.status = 'completed'
    
    db.session.commit()
    
    return jsonify({'message': 'Exchange completed'}), 200
