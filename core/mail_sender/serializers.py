from flask_restx import fields
from ext.restplus import api


mail_send = api.model('mail_send', {
    'email_type': fields.String(required=True, description='Type e-mail to send'),
    'user_id':    fields.Integer(required=True, description='Id to user in user database'),
    'to_mail':    fields.String(required=True, description='Recipients to mail'),
    'subject':    fields.String(required=True, description='Subject to mail'),
    'params':     fields.String(require=False, description='Json of params in string format'),
})

