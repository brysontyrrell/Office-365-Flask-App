from . import db
from .oauth_helpers import (
    datetime_from_timestamp,
    refresh_oauth_token
)
import datetime


class O365OAuthToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String, nullable=False)
    refresh_token = db.Column(db.String, nullable=False)
    expires_on = db.Column(db.DateTime, nullable=False)
    user_email = db.Column(db.String, index=True, unique=True, nullable=False)
    token_type = db.Column(db.String)
    resource = db.Column(db.String)
    scope = db.Column(db.String)

    @property
    def token(self):
        if (self.expires_on - datetime.timedelta(minutes=10)) > datetime.datetime.utcnow():
            return self.access_token
        else:
            token = refresh_oauth_token(self.refresh_token)
            self.access_token = token['access_token']
            self.refresh_token = token['refresh_token']
            self.expires_on = datetime_from_timestamp(token['expires_on'])
            db.session.add(self)
            db.session.commit()

        return self.access_token
