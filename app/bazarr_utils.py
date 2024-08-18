"""
bazarr_utils.py
This module provides functions to interact with the Bazarr API.
"""

import requests

def get_wanted_subtitles(bazarr_url, api_key):
    """Fetch the list of wanted subtitles from Bazarr."""
    headers = {
        'apikey': api_key
    }
    
    response = requests.get(f"{bazarr_url}/wanted", headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch wanted subtitles: {response.text}")

    return response.json()
