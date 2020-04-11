from flask import Blueprint
from flask_restx import Resource

from ext.restplus import api
from core import mail_sender
from core.example.constants import MAIL_TYPE, MAIL_DEFAULT
from core.mail_sender.serializers import mail_send

example = Blueprint('example', __name__, url_prefix='/example/1')
ns = api.namespace('example', description='SEND MAIL operations')


@ns.route('/mail')
class SendToken(Resource):
    """SEND param to create mail"""

    @ns.expect(mail_send)
    def post(self):
        """Send MAIL"""
        import ipdb; ipdb.set_trace()
        api_payload = api.payload
        output =None
        if api_payload.get('email_type') == MAIL_TYPE.ticket_email.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.ticket_email.value,
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        elif api_payload.get('email_type') == MAIL_TYPE.confirm_reimbursement.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.confirm_reimbursement.value,
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        if api_payload.get('email_type') == MAIL_TYPE.invite.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.invite.value,
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        if api_payload.get('email_type') == MAIL_TYPE.lost_password.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.lost_password.value,
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        if api_payload.get('email_type') == MAIL_TYPE.manual_transaction_welcome.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.manual_transaction_welcome.value:
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        if api_payload.get('email_type') == MAIL_TYPE.share_item_charge.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.share_item_charge.value,
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        if api_payload.get('email_type') == MAIL_TYPE.token.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.token.value,
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        if api_payload.get('email_type') == MAIL_TYPE.token_sms_mail.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.token_sms_mail.value,
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        if api_payload.get('email_type') == MAIL_TYPE.welcome.value:
            output = mail_sender.send_ticket_mail(
                email_type=MAIL_TYPE.welcome.value,
                user_id=api_payload.get('user_id'),
                from_mail=MAIL_DEFAULT.from_default.value,
                to_mail=api_payload.get('to_mail'),
                subject=api_payload.get('subject'),
                ticket_params=api_payload.get('params'))
        return {'message': 'colocado na fila!'}, 200

