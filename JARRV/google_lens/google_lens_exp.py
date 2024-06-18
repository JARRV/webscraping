import serpapi
from dotenv import load_dotenv
import os

import serpapi.google_search
load_dotenv()
api_key = os.getenv('GOOGLE_LENS_API')

def google_lens_search(img_url):
    params = {
        "engine":"google_lens",
        "url": 'https://mir-s3-cdn-cf.behance.net/user/230/f4400225849403.5d4bcc7dd8a59.jpg',
        "api_key":api_key,
        'no_cache': False,
    }

    search = serpapi.search(params=params)
    #results = search.get_dict()
    visual_matches = search['visual_matches']
    
    #visual_matches = results['visual_matches']
    return visual_matches #visual_matches
