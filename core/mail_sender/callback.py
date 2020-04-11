from flask import Blueprint, request, jsonify

from ext.db import db
from core.mail_sender.models import CommunicationGateway

mail_sender = Blueprint("mail_sender", __name__)


@mail_sender.route("/receive/callback", methods=["POST"])
def receive_callback():
    data = request.get_json()
    original_id = data.get('original_id')
    request_status = data.get('request_status')
    try:
        status_queue = CommunicationGateway.query.filter_by(id=original_id).first()

        if status_queue:
            status_queue.request_status = request_status

            db.session.add(status_queue)
            db.session.commit()

            return jsonify({'response': 'success'}), 201

        return jsonify({'response': 'fail'}), 404
    except Exception as e:
        db.session.rollback()
        raise e
