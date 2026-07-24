from flask import Flask
from flask_migrate import Migrate
from config import Config
from courses.models import db


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from courses import models

    migrate = Migrate(
        app,
        db
    )

    from courses.routes import courses_bp

    app.register_blueprint(
        courses_bp
    )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        debug=True
    )