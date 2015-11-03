from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore


app = Flask(__name__)
app.config.from_pyfile('zgolodniv.cfg')

db = MongoEngine(app)

from zgolodniv.models import User, Role

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)


def register_blueprints(app):
    from zgolodniv.admin import admin
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
