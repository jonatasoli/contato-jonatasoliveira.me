# APP
from app.services.raiser import Raiser
from app.utils.Constants import SLACK_CHANNELS

class MailSenderException(Raiser):
    _channel        = SLACK_CHANNELS.mail_sender.value

    def __init__(self, msg):
        super(MailSenderException, self).__init__(
            msg,
            self._channel
        )
