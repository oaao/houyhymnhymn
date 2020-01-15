from local_settings import GOOGLE_CREDENTIALS_FILE

GOOGLE_CREDENTIALS = {
    'type': 'service_account_file',
    'cred': GOOGLE_CREDENTIALS_FILE
}

YOUTUBE_SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']