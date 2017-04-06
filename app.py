from oauthlib.common import Request
from oauthlib.oauth2 import AuthorizationCodeGrant, RequestValidator, BearerToken
import os
import sqlalchemy


class MyRequestValidator(RequestValidator):
    def validate_client_id(self, client_id, request, *args, **kargs):
        return True

client_id = os.environ['TWITTER_CLIENT_ID']

uri = ''
body = {}
headers = headers

request = Request(uri, body=body, headers=headers)

request_validator = MyRequestValidator()
beaer_token = BearerToken(request_validator)
client = AuthorizationCodeGrant(request, beaer_token)
