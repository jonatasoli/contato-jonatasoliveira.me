import enum


class MAIL_TYPE(enum.Enum):
    lost_password = 'lost_password'
    ticket_email = 'ticket_email'
    token = 'token'
    invite = 'invite'
    welcome = 'welcome'
    share_item_charge = 'share_item_charge'
    manual_transaction_welcome = 'manual_transaction_welcome'
    confirm_reimbursement = 'confirm_reimbursement'
    token_sms_mail = 'token_sms_mail'
    send_reimbursement_order = 'send_reimbursement_order'


class MAIL_DEFAULT(enum.Enum):
    from_default = 'example@mail.com.br'

