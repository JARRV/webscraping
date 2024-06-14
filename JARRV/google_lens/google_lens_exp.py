from serpapi import google_search
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('GOOGLE_LENS_API')

def google_lens_search(img_url):
    params = {
        "engine":"google_lens",
        "url": img_url,
        "api_key":api_key,
        'no_cache': False,
    }

    search = google_search(params)
    results = search.get_dict()
    visual_matches = results['visual_matches']
    print(visual_matches)
