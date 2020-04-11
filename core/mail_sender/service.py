from abc import ABC, abstractclassmethod

import requests

from flask import current_app as app

from ext.db import db
from core.mail_sender.constants import URL_ENVIRONMENT, MICROSERVICE_REQUEST_STATUS, MICROSERVICE_TYPE
from core.mail_sender.models import CommunicationGateway


class MailSender(ABC):

    def __init__(self,
                 email_type=None,
                 user_id=None,
                 from_mail=None,
                 to_mail=None,
                 subject=None,
                 ):
        self.email_type = email_type
        self.user_id = user_id
        self.from_mail = from_mail
        self.to_mail = to_mail
        self.subject = subject

    @property
    def get_user_id(self):
        return self.user_id

    def publish_email_in_topic(self, user_id, endpoint_type):
        # TODO Decompor em 3 métodos
        url_env = app.config.get('ENV_URL_SERVICES')

        if url_env == 'staging':
            url = URL_ENVIRONMENT.staging.value
        elif url_env == 'production':
            url = URL_ENVIRONMENT.production.value
        else:
            url = URL_ENVIRONMENT.development.value

        data = self.generate_data()
        publisher_status = None
        try:
            import ipdb; ipdb.set_trace()
            publisher_status = CommunicationGateway(
                target_user_id=user_id,
                params_hash=data,
                type=MICROSERVICE_TYPE.email.value,
                endpoint_type=endpoint_type,
                request_status=MICROSERVICE_REQUEST_STATUS.created.value
            )
            db.session.add(publisher_status)
            db.session.commit()
            data['original_id'] = publisher_status.id
            publisher_status.params_hash = data

            db.session.add(publisher_status)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': 'Problema ao salvar a requisição',
                    'status': 404}

        response = None

        try:
            response = requests.post(url=url, json=data, timeout=3)

        except requests.exceptions.Timeout as errt:
            publisher_status.request_status = MICROSERVICE_REQUEST_STATUS.enqueued_fail.value

            db.session.add(publisher_status)
            db.session.commit()

            response_string = {'message': 'Serviço fora do ar', 'status': 400}
            return response_string
        except Exception as e:
            print('Problema no envio do e-mail {}'.format(e))

        if response is None or response.status_code != 201:
            try:
                publisher_status.request_status = MICROSERVICE_REQUEST_STATUS.invalid.value
                db.session.add(publisher_status)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
            print(f'Não foi possível enviar o email {str(data)}')
            return {'message': 'Problema ao comunicar-se com o serviço',
                    'status': response.status_code if response is not None else ''}
        return response.json()

    @abstractclassmethod
    def generate_data(self):
        """Abstract class to create mail json
            Return a specific json to email type
        """


class LostPassword(MailSender):
    def __init__(self, lost_password_params, email_type, user_id, from_mail, to_mail, subject):
        super().__init__(email_type=email_type, user_id=user_id, from_mail=from_mail, to_mail=to_mail, subject=subject)
        self.lost_password_params = lost_password_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'lost_password_params': self.lost_password_params
        }


class Ticket(MailSender):
    def __init__(self, email_type, user_id, from_mail, to_mail, subject, ticket_params):
        super().__init__(email_type=email_type, user_id=user_id, from_mail=from_mail, to_mail=to_mail, subject=subject)
        self.ticket_params = ticket_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'ticket_params': self.ticket_params
        }


class TokenSignUp(MailSender):
    def __init__(self, token_params, email_type, user_id, from_mail, to_mail, subject):
        super().__init__(email_type, user_id, from_mail, to_mail, subject)
        self.token_params = token_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'token_params': self.token_params
        }


class Welcome(MailSender):
    def __init__(self, welcome_params, email_type, user_id, from_mail, to_mail, subject):
        super().__init__(email_type, user_id, from_mail, to_mail, subject)
        self.welcome_params = welcome_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'welcome_params': self.welcome_params
        }


class SendShareItemCharge(MailSender):
    def __init__(self, share_item_charge_params, email_type, user_id, from_mail, to_mail, subject):
        super().__init__(email_type, user_id, from_mail, to_mail, subject)
        self.share_item_charge_params = share_item_charge_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'share_item_charge_params': self.share_item_charge_params
        }


class SendManualTransactionWelcome(MailSender):
    def __init__(self, manual_transaction_welcome_params, email_type, user_id, from_mail, to_mail, subject):
        super().__init__(email_type, user_id, from_mail, to_mail, subject)
        self.manual_transaction_welcome_params = manual_transaction_welcome_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'manual_transaction_welcome_params': self.manual_transaction_welcome_params
        }


class SendConfirmReimbursement(MailSender):

    def __init__(self, confirm_reimbursement_params, email_type, user_id, from_mail, to_mail, subject):
        super().__init__(email_type, user_id, from_mail, to_mail, subject)
        self.confirm_reimbursement_params = confirm_reimbursement_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'confirm_reimbursement_params': self.confirm_reimbursement_params
        }


class SendTokenSms(MailSender):
    def __init__(self, token_sms_params, email_type, user_id, from_mail, to_mail, subject):
        super().__init__(email_type, user_id, from_mail, to_mail, subject)
        self.token_sms_params = token_sms_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'token_sms_params': self.token_sms_params
        }


class SendReimbursementOrder(MailSender):
    def __init__(self, reimbursement_order_params, email_type, user_id, from_mail, to_mail, subject):
        super().__init__(email_type, user_id, from_mail, to_mail, subject)
        self.reimbursement_order_params = reimbursement_order_params

    def generate_data(self):
        return {
            'email_type': self.email_type,
            'user_id': self.user_id,
            'from_mail': self.from_mail,
            'to_mail': self.to_mail,
            'subject': self.subject,
            'reimbursement_order_params': self.reimbursement_order_params
        }
