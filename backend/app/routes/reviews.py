from flask import Blueprint, request, jsonify
from app import db
from app.models import Review, Exchange
from flask_jwt_extended import jwt_required, get_jwt_identity

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/exchanges/<int:id>/reviews', methods=['POST'])
@jwt_required()
def create_review(id):
    user_id = get_jwt_identity()
    exchange = Exchange.query.get_or_404(id)
    
    if exchange.status != 'completed':
        return jsonify({'error': 'Exchange is not completed'}), 400
    
    if str(exchange.sender_id) != user_id and str(exchange.receiver_id) != user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    existing = Review.query.filter_by(
        exchange_id=id,
        reviewer_id=user_id
    ).first()
    
    if existing:
        return jsonify({'error': 'You already reviewed this exchange'}), 409
    
    data = request.get_json()
    
    reviewed_id = exchange.receiver_id if str(exchange.sender_id) == user_id else exchange.sender_id
    
    review = Review(
        reviewer_id=user_id,
        reviewed_id=reviewed_id,
        exchange_id=id,
        rating=data['rating'],
        comment=data.get('comment')
    )
    
    db.session.add(review)
    db.session.commit()
    
    return jsonify({'message': 'Review created', 'id': review.id}), 201
