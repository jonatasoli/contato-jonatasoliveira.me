from flask import Blueprint
from flask_restx import Resource

from ext.restplus import api
from core import mail_sender
from core.example.constants import MAIL_TYPE, MAIL_DEFAULT
from core.mail_sender.serializers import mail_send

example = Blueprint('example', __name__, url_prefix='/example/1')
ns = api.namespace('example', description='SEND MAIL operations')


@ns.route('/send_ticket')
class SendTicket(Resource):
    """SEND params to ticket mail"""

    @ns.expect(mail_send)
    def post(self):
        """Send Ticket Email"""
        api_payload = api.payload
        output = mail_sender.send_ticket_mail(
            email_type=MAIL_TYPE.ticket_email.value,
            user_id=api_payload.get('user_id'),
            from_mail=MAIL_DEFAULT.from_default.value,
            to_mail=api_payload.get('to_mail'),
            subject=api_payload.get('subject'),
            ticket_params=api_payload.get('params'))
        return {'message': 'colocado na fila!'}, 200


@ns.route('/send_lost_password')
class SendLostPassword(Resource):
    """SEND params to ticket mail"""

    @ns.expect(mail_send)
    def post(self):
        """Send MAIL"""
        api_payload = api.payload
        output = mail_sender.send_lost_password_mail(
            email_type=MAIL_TYPE.lost_password.value,
            user_id=api_payload.get('user_id'),
            from_mail=MAIL_DEFAULT.from_default.value,
            to_mail=api_payload.get('to_mail'),
            subject=api_payload.get('subject'),
            ticket_params=api_payload.get('params'))
        return {'message': 'colocado na fila!'}, 200


@ns.route('/send_welcome')
class SendWelcome(Resource):
    """SEND params to welcome mail"""

    @ns.expect(mail_send)
    def post(self):
        """Send WELCOME MAIL"""
        api_payload = api.payload
        output = mail_sender.send_welcome_mail(
            email_type=MAIL_TYPE.welcome.value,
            user_id=api_payload.get('user_id'),
            from_mail=MAIL_DEFAULT.from_default.value,
            to_mail=api_payload.get('to_mail'),
            subject=api_payload.get('subject'),
            ticket_params=api_payload.get('params'))
        return {'message': 'colocado na fila!'}, 200


@ns.route('/send_confirm_reimbursement')
class SendConfirmReimbursement(Resource):
    """SEND params to confirm reimbursement to signup mail"""

    @ns.expect(mail_send)
    def post(self):
        """Send CONFIRM REIMBURSEMENT MAIL"""
        api_payload = api.payload
        output = mail_sender.send_confirm_reimbursement_mail(
            email_type=MAIL_TYPE.confirm_reimbursement.value,
            user_id=api_payload.get('user_id'),
            from_mail=MAIL_DEFAULT.from_default.value,
            to_mail=api_payload.get('to_mail'),
            subject=api_payload.get('subject'),
            ticket_params=api_payload.get('params'))
        return {'message': 'colocado na fila!'}, 200

