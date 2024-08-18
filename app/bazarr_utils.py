import requests

def get_wanted_subtitles(bazarr_url, api_key):
    """
    Fetch the list of wanted subtitles from Bazarr.
    
    :param bazarr_url: The URL of the Bazarr API.
    :param api_key: Bazarr API Key for authentication.
    :return: List of wanted subtitle files.
    """
    headers = {
        'apikey': api_key
    }
    
    response = requests.get(f"{bazarr_url}/wanted", headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch wanted subtitles: {response.text}")

    return response.json()
