import os
import requests

def translate_text(text, source_lang, target_lang):
    """Translate text from source language to target language using DeepL API."""
    auth_key = os.getenv('DEEPL_AUTH_KEY')
    url = "https://api.deepl.com/v2/translate"
    params = {
        'auth_key': auth_key,
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang
    }

    try:
        response = requests.post(url, data=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f'Translation error: {e}') from e

    translation = response.json()
    return translation['translations'][0]['text']
