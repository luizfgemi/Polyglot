import os
import requests

def translate_text(text, source_lang, target_lang):
    """Translate text from source language to target language using DeepL API."""
    auth_key = os.getenv('DEEPL_AUTH_KEY')
    if not auth_key:
        raise ValueError('DEEPL_AUTH_KEY environment variable is not set')

    url = "https://api.deepl.com/v2/translate"
    params = {
        'auth_key': auth_key,
        'text': text,
        'target_lang': target_lang
    }
    if source_lang:
        params['source_lang'] = source_lang

    response = requests.post(url, data=params)
    if response.status_code != 200:
        raise Exception(f'Translation error: {response.text}')

    translation = response.json()
    return translation['translations'][0]['text']
