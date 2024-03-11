from flask import Flask, session, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .goals import goals as goals_blueprint

    app.register_blueprint(goals_blueprint)

    # Initial setup - if run for the first time, create database and import users
    from .models import User

    with app.app_context():
        try:
            if not (User.query.first()):
                raise RuntimeError("Missing user")
        except:
            # create databases
            db.create_all()
            # insert user
            db.session.add(
                User(forename="Ronald", surname="McDonald", username="r.mcdonald")
            )
            db.session.commit()

    # handle logged in user
    @app.before_request
    def before_request():
        if session.get("active_user"):
            # active user ID found in session - fetch and add to 'g'  (global request object)
            try:
                g.current_user = User.query.filter_by(id=session["active_user"]).one()
            except NoResultFound:
                # if unknown user, log out
                g.current_user = None
                session.pop("active_user")
        else:
            g.current_user = None

    return app
