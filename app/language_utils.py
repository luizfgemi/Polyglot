from supported_languages import LANGUAGES

def get_file_extension(language_code):
    return LANGUAGES.get(language_code, {}).get("extension", f".{language_code.lower()}.srt")

def get_language_code_from_extension(file_name):
    for language_code, info in LANGUAGES.items():
        if file_name.endswith(info["extension"]):
            return language_code
    return None
