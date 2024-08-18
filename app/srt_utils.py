import os
from translation import translate_text
from language_utils import get_file_extension, get_language_code_from_extension

def translate_srt_files(folder_path, target_langs, source_lang=None):
    translated_files = []

    if not os.path.isdir(folder_path):
        print(f'Error: {folder_path} is not a valid directory.')
        return translated_files

    # Find all .srt files in the current folder
    for dirpath, _, filenames in os.walk(folder_path):
        existing_srt_files = [f for f in filenames if f.endswith('.srt')]

        for target_lang in target_langs:
            target_file_extension = get_file_extension(target_lang)

            for srt_file in existing_srt_files:
                if srt_file.endswith(target_file_extension):
                    continue  # Skip if the translated file already exists

                base_name = os.path.splitext(srt_file)[0]
                source_lang = source_lang or get_language_code_from_extension(srt_file)

                if not source_lang:
                    print(f'Error: Could not determine source language for {srt_file}')
                    continue

                file_path = os.path.join(dirpath, srt_file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                translated_content = translate_text(content, source_lang, target_lang)

                translated_file_name = f"{base_name}.{target_lang}.srt"
                translated_file_path = os.path.join(dirpath, translated_file_name)

                with open(translated_file_path, 'w', encoding='utf-8') as file:
                    file.write(translated_content)

                translated_files.append(translated_file_path)

    return translated_files
