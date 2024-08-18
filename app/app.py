"""
app.py
This module provides the main Flask application for subtitle translation.
"""

from flask import Flask, request, jsonify
from translation import translate_text
from srt_utils import translate_srt_files
from supported_languages import LANGUAGES
from bazarr_utils import get_wanted_subtitles
import os

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    """Translate a given text to a target language."""
    data = request.json
    text = data.get('text')
    source_lang = data.get('source_lang')  # Source language
    target_lang = data.get('target_lang', 'EN')  # Default target language is English

    translated_text = translate_text(text, source_lang, target_lang)
    return jsonify({'translated_text': translated_text})

@app.route('/languages', methods=['GET'])
def get_languages():
    """Get the list of supported languages."""
    return jsonify(LANGUAGES)

@app.route('/translate_srt', methods=['POST'])
def translate_srt():
    """Translate subtitles in a specified folder."""
    data = request.json
    folder_path = data.get('folder_path')  # Single folder path
    target_langs = data.get('target_langs', ['EN'])  # List of target languages
    source_lang = data.get('source_lang')  # Optional source language

    translated_files = translate_srt_files(folder_path, target_langs, source_lang)
    return jsonify({'translated_files': translated_files})

@app.route('/translate_bulk', methods=['POST'])
def translate_bulk():
    """Translate subtitles in multiple root folders."""
    data = request.json
    root_folders = data.get('root_folders', [])  # List of root folders
    target_langs = data.get('target_langs', ['EN'])  # List of target languages
    source_lang = data.get('source_lang')  # Optional source language

    all_translated_files = []
    for folder in root_folders:
        translated_files = translate_srt_files(folder, target_langs, source_lang)
        all_translated_files.extend(translated_files)

    return jsonify({'translated_files': all_translated_files})

@app.route('/translate_wanted', methods=['POST'])
def translate_wanted():
    """Fetch wanted subtitles from Bazarr and translate them."""
    data = request.json
    bazarr_url = "http://bazarr:6767/api"  # URL do Bazarr dentro do Docker Compose
    api_key = os.getenv('BAZARR_API_KEY')
    target_langs = data.get('target_langs', ['EN'])  # List of target languages
    source_lang = data.get('source_lang')  # Optional source language

    # Get wanted subtitles from Bazarr
    wanted_subtitles = get_wanted_subtitles(bazarr_url, api_key)

    translated_files = []
    for item in wanted_subtitles:
        folder_path = item['path']  # Assuming 'path' contains the folder path
        translated_files.extend(translate_srt_files(folder_path, target_langs, source_lang))

    return jsonify({'translated_files': translated_files})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
