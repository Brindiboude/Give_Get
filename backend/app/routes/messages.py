from flask import Blueprint, request, jsonify
from app import db
from app.models import Message, Exchange
from flask_jwt_extended import jwt_required, get_jwt_identity

messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/exchanges/<int:id>/messages', methods=['GET'])
@jwt_required()
def get_messages(id):
    user_id = get_jwt_identity()
    exchange = Exchange.query.get_or_404(id)
    
    if str(exchange.sender_id) != user_id and str(exchange.receiver_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    messages = Message.query.filter_by(exchange_id=id).all()
    
    return jsonify([{
        'id': msg.id,
        'sender_id': msg.sender_id,
        'content': msg.content,
        'sent_at': msg.sent_at
    } for msg in messages]), 200


@messages_bp.route('/exchanges/<int:id>/messages', methods=['POST'])
@jwt_required()
def send_message(id):
    user_id = get_jwt_identity()
    exchange = Exchange.query.get_or_404(id)
    
    if str(exchange.sender_id) != user_id and str(exchange.receiver_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    
    message = Message(
        exchange_id=id,
        sender_id=user_id,
        content=data['content']
    )
    
    db.session.add(message)
    db.session.commit()
    
    return jsonify({'message': 'Message sent', 'id': message.id}), 201
