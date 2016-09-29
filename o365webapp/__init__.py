import config
import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

import models
import views
