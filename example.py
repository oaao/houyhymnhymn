import pprint

from houyhymnhymn.clients.google import YoutubeAPI
from houyhymnhymn.config import GOOGLE_CREDENTIALS, YOUTUBE_SCOPES

def search():

    yt = YoutubeAPI(GOOGLE_CREDENTIALS, scopes=YOUTUBE_SCOPES)

    query = input('Search query:\n')
    n     = int(input('Max number of results:\n'))

    try:
        resp = yt.search(query, max_results=n)
        pprint.pprint(resp, indent=2)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    search()
