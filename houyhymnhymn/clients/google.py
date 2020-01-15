import os

from google.oauth2 import service_account

import googleapiclient.discovery
import googleapiclient.errors


class GoogleAPI:

    def __init__(self, credentials_config, api_name=None, api_version=None, scopes=None, debug=False):

        if debug:
            os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

        self.api_name    = api_name
        self.api_version = api_version
        self.scopes      = scopes

        self.credentials = self._build_credentials(credentials_config)
        self.client      = self._build_client()

    def _build_credentials(self, credentials_config):

        CREDENTIAL_ACTIONS = {
                'service_account_file': self._credentials_from_SAC
        }

        auth_type = credentials_config['type']
        auth_cred = credentials_config['cred']

        return CREDENTIAL_ACTIONS[auth_type](auth_cred)

    def _credentials_from_SAC(self, credentials):
        return service_account.Credentials.from_service_account_file(credentials, scopes=self.scopes)

    def _build_client(self):
        return googleapiclient.discovery.build(self.api_name, self.api_version, credentials=self.credentials)


class YoutubeAPI(GoogleAPI):

    def __init__(self, credentials_config, scopes=None, debug=False):

        super().__init__(
            credentials_config,
            api_name='youtube',
            api_version='v3',
            scopes=scopes,
            debug=debug,
        )


    def search(self, query, max_results=25):

        req = self.client.search().list(
            part='snippet',
            maxResults=max_results,
            q=query
        )

        resp = req.execute()
        return resp