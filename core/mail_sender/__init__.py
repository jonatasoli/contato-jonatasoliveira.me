from .constants import MICROSERVICE_ENDPOINT_TYPE
from .service import LostPassword, SendConfirmReimbursement, SendManualTransactionWelcome, \
    SendReimbursementOrder, SendShareItemCharge, SendTokenSms, Ticket, TokenSignUp, Welcome


def send_lost_password_mail(email_type, user_id, from_mail, to_mail, subject, lost_password_params):
    """
    Email esqueci minha senha
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param lost_password_params: json with (link, link_button, link_text)
    :return: json result status to invite and message id in service
    """
    mail = LostPassword(email_type=email_type,
                        user_id=user_id,
                        from_mail=from_mail,
                        to_mail=to_mail,
                        subject=subject,
                        lost_password_params=lost_password_params)
    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.lost_password.value
    )


def send_ticket_mail(email_type, user_id, from_mail, to_mail, subject, ticket_params):
    """
    e-mail com ticket(s)
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param ticket_params: json with (link, link_button, link_text)
    :return: json result status to invite and message id in service
    """
    mail = Ticket(email_type=email_type,
                  user_id=user_id,
                  from_mail=from_mail,
                  to_mail=to_mail,
                  subject=subject,
                  ticket_params=ticket_params)

    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.ticket_email.value
    )


def send_token_mail(email_type, user_id, from_mail, to_mail, subject, token_params):
    """
    E-mail de confirmação de Cadastro
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param token_params: json with (link e username)
    :return: json result status to invite and message id in service
    """
    mail = TokenSignUp(email_type=email_type,
                       user_id=user_id,
                       from_mail=from_mail,
                       to_mail=to_mail,
                       subject=subject,
                       token_params=token_params)
    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.token.value
    )


def send_welcome_mail(email_type, user_id, from_mail, to_mail, subject, welcome_params):
    """
    Boas vindas a partyou
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param welcome_params: json with (username)
    :return: json result status to invite and message id in service
    """
    mail = Welcome(email_type=email_type,
                   user_id=user_id,
                   from_mail=from_mail,
                   to_mail=to_mail,
                   subject=subject,
                   welcome_params=welcome_params)
    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.welcome.value
    )


def send_share_item_charge_mail(email_type, user_id, from_mail, to_mail, subject, share_item_charge_params):
    """
    Lembrete de pagamento
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param share_item_charge_params: json with (
        guest_name, admin_name, formatted_price_cents_with_fee, item_name, event_external_url, link_button, link_text)

    :return: json result status to invite and message id in service
    """
    mail = SendShareItemCharge(email_type=email_type,
                               user_id=user_id,
                               from_mail=from_mail,
                               to_mail=to_mail,
                               subject=subject,
                               share_item_charge_params=share_item_charge_params)
    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.share_item_charge.value
    )


def send_manual_transaction_welcome_mail(email_type, user_id, from_mail, to_mail, subject,
                                         manual_transaction_welcome_params):
    """
    Boas vindas para quem vem de lançamento manual
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param manual_transaction_welcome_params: json with (service_email, username, communication_name,
        user_email, url_blog, link)
    :return: json result status to invite and message id in service
    """
    mail = SendManualTransactionWelcome(email_type=email_type,
                                        user_id=user_id,
                                        from_mail=from_mail,
                                        to_mail=to_mail,
                                        subject=subject,
                                        manual_transaction_welcome_params=manual_transaction_welcome_params)
    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.manual_transaction_welcome.value
    )


def send_confirm_reimbursement_mail(email_type, user_id, from_mail, to_mail, subject, confirm_reimbursement_params):
    """
    Confirmação de reembolso
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param confirm_reimbursement_params: json with (username, reimbursement_value, bank_name, office, account, person_name)
    :return: json result status to invite and message id in service
    """
    mail = SendConfirmReimbursement(email_type=email_type,
                                    user_id=user_id,
                                    from_mail=from_mail,
                                    to_mail=to_mail,
                                    subject=subject,
                                    confirm_reimbursement_params=confirm_reimbursement_params)
    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.confirm_reimbursement.value
    )


def send_token_sms_mail(email_type, user_id, from_mail, to_mail, subject, token_sms_params):
    """
    Envio de token por e-mail no cadastro
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param token_sms_params: json with (text to body e-mail)
    :return: json result status to invite and message id in service
    """
    mail = SendTokenSms(email_type=email_type,
                        user_id=user_id,
                        from_mail=from_mail,
                        to_mail=to_mail,
                        subject=subject,
                        token_sms_params=token_sms_params)
    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.token_sms_mail.value
    )


def send_reimbursement_order_mail(email_type, user_id, from_mail, to_mail, subject, reimbursement_order_params):
    """
    Envio de reembolso - esse template é do admin
    :param email_type: type to template to send e-mail
    :param user_id: user to receive e-mail
    :param from_mail: e-mail to send
    :param to_mail: e-mail user to receive e-mail
    :param subject: subject in e-mail
    :param reimbursement_order_params: json with (text to body e-mail)
    :return: json result status to invite and message id in service
    """
    mail = SendReimbursementOrder(email_type=email_type,
                                  user_id=user_id,
                                  from_mail=from_mail,
                                  to_mail=to_mail,
                                  subject=subject,
                                  reimbursement_order_params=reimbursement_order_params)
    mail.publish_email_in_topic(
        user_id=user_id,
        endpoint_type=MICROSERVICE_ENDPOINT_TYPE.send_reimbursement_order.value
    )
