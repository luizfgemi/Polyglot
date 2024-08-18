"""
language_utils.py
This module provides utility functions for language handling.
"""

from supported_languages import LANGUAGES

def get_file_extension(language_code):
    """Return the corresponding file extension for a given language code."""
    return LANGUAGES.get(language_code, {}).get("extension", f".{language_code.lower()}.srt")

def get_language_code_from_extension(file_name):
    """Determine the language code from the file extension."""
    for language_code, info in LANGUAGES.items():
        if file_name.endswith(info["extension"]):
            return language_code
    return None
