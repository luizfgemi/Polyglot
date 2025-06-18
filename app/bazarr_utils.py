"""Utility functions for interacting with Bazarr."""

import requests

def get_wanted_subtitles(bazarr_url, api_key):
    """Return wanted subtitles from Bazarr using the provided API key."""
    headers = {
        "apikey": api_key
    }

    try:
        response = requests.get(f"{bazarr_url}/wanted", headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch wanted subtitles: {e}") from e

    return response.json()
