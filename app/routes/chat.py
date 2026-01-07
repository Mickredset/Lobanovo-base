from flask import Blueprint, render_template
from flask_socketio import emit
from ..models import Message, User

bp = Blueprint('chat', __name__)

@bp.route('/chat')
def chat():
    messages = Message.query.order_by(Message.timestamp).all()
    return render_template('chat.html', messages=messages)

@bp.socketio.on('send_message')
def handle_message(data):
    message = Message(content=data['message'], sender_id=data['sender_id'])
    db.session.add(message)
    db.session.commit()
    emit('new_message', {
        'message': data['message'],
        'sender': data['sender'],
        'timestamp': message.timestamp.isoformat()
    }, broadcast=True)
