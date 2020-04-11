def register_blueprints(app):

    # config test app blueprint remove it
    from core.example.resources import example
    app.register_blueprint(example, url_prefix="/example")
    # config mail send blueprint

    from core.mail_sender import callback
    app.register_blueprint(callback.mail_sender, url_prefix="/mail_sender")

    return app
