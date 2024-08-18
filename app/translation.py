import os
import requests

def translate_text(text, source_lang, target_lang):
    auth_key = os.getenv('DEEPL_AUTH_KEY')
    url = "https://api.deepl.com/v2/translate"
    params = {
        'auth_key': auth_key,
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang
    }

    response = requests.post(url, data=params)
    if response.status_code != 200:
        raise Exception(f'Translation error: {response.text}')

    translation = response.json()
    return translation['translations'][0]['text']
