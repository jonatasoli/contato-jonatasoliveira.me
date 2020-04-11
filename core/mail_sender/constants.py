import enum


class URL_ENVIRONMENT(enum.Enum):
    development = 'http://127.0.0.1:5000/mail/send'
    staging     = 'http://partyou-com-gty-stg/mail/send'
    production  = 'http://partyou-com-gty-prod/mail/send'


class MICROSERVICE_TYPE(enum.Enum):
    sms = 'SMS'
    email = 'EMAIL'
    push = 'PUSH'


class MICROSERVICE_ENDPOINT_TYPE(enum.Enum):
    """
    Todos os tipos de e-mail que podem ser enviados no endpoint - Cada microserviço tem seus tipos de endpoints
    :type lost_password: Esqueci minha senha
    :type ticket_email: Ticket
    :type token: Confirmação de cadastro
    :type invite: Envio de cobrança
    :type welcome:  Boas vindas no cadastro convencional
    :type share_item_charge: Lembrete de cobrança
    :type manual_transaction_welcome: Boas vindas pra quem tem o cadastro no lançamento manual
    :type confirm_reimbursement: Confirmação de reembolso
    :type token_sms_mail: Envio de token por e-mail na hora do cadastro
    :type send_reimbursement_order: Envio de reembolso no admin
    """
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


class MICROSERVICE_REQUEST_STATUS(enum.Enum):
    """
    Todos os tipos de status que pode ser retornados pelo messagem broker
    :type created: inserido antes de chamar o serviço
    :type service:_unavailable serviço não disponível
    :type enqueued_fail: não conseguiu colocar na fila
    :type enqueued: obtive 200 da requisição - salva o id do microserviço
    :type processed: status final de sucesso
    :type invalid: dados inválidos para execução da solicitação
    """
    created = 'CREATED'
    service_unavailable = 'SERVICE_UNAVAILABLE'
    enqueued_fail = 'ENQUEUED_FAIL'
    enqueued = 'ENQUEUED'
    processed = 'PROCESSED'
    invalid = 'INVALID'
