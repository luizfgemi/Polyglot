import requests

def get_wanted_subtitles(bazarr_url, api_key):
    headers = {
        'apikey': api_key
    }

    try:
        response = requests.get(f"{bazarr_url}/wanted", headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch wanted subtitles: {str(e)}")

    return response.json()
