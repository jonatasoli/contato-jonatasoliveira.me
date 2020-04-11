from ext.db import db
from sqlalchemy.types import JSON


class CommunicationGateway(
    db.Model
):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    target_user_id = db.Column(db.Integer, nullable=False)
    params_hash = db.Column(JSON, nullable=False)
    type = db.Column(db.String(10), nullable=False)
    endpoint_type = db.Column(db.String(30), nullable=True)
    request_status = db.Column(db.String(20), nullable=False)

    def __init__(self, target_user_id, params_hash, type, request_status, endpoint_type=None):
        self.target_user_id = target_user_id
        self.params_hash = params_hash
        self.type = type
        self.request_status = request_status
        self.endpoint_type = endpoint_type
