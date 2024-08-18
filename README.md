# Polyglot

Polyglot is a simple API for translating subtitle files (.srt) using the DeepL translation service. It supports multiple languages and can translate entire folders of subtitle files.

## Features

- Translate individual text strings.
- Translate .srt files in bulk from a specified folder.
- Supports multiple languages.
- Automatically saves translated subtitles with appropriate file extensions.
- Determines source language based on .srt file extension.

## Requirements

- Docker
- Docker Compose
- DeepL API Key (sign up at [DeepL](https://www.deepl.com/pro#developer) to get your API key)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/subtitle-translator.git
cd subtitle-translator
```

### Configuration

- Open docker-compose.yml and replace your_api_key_here with your actual DeepL API key.
- Update the volume path ./path/to/your/subtitles to point to the folder where your .srt files are located.


### Build and Run
```bash
docker-compose build
docker-compose up
```

## API Endpoints
### Translate Text
- Endpoint: /translate
- Method: POST
- Request Body:

```json
{
    "text": "Hello, world!",
    "source_lang": "EN",
    "target_lang": "ES"
}
```

- Response:
```json
{
    "translated_text": "¡Hola, mundo!"
}
```

### Get Supported Languages
- Endpoint: /languages
- Method: GET
- Response:
```json
{
    "EN": {"name": "English", "extension": ".en.srt"},
    "DE": {"name": "German", "extension": ".de.srt"},
    "FR": {"name": "French", "extension": ".fr.srt"},
    "ES": {"name": "Spanish", "extension": ".es.srt"},
    "IT": {"name": "Italian", "extension": ".it.srt"},
    "NL": {"name": "Dutch", "extension": ".nl.srt"},
    "PL": {"name": "Polish", "extension": ".pl.srt"},
    "RU": {"name": "Russian", "extension": ".ru.srt"},
    "PT": {"name": "Portuguese", "extension": ".pt.srt"},
    "JA": {"name": "Japanese", "extension": ".ja.srt"},
    "ZH": {"name": "Chinese", "extension": ".zh.srt"},
    "DA": {"name": "Danish", "extension": ".da.srt"},
    "FI": {"name": "Finnish", "extension": ".fi.srt"},
    "SV": {"name": "Swedish", "extension": ".sv.srt"},
    "NO": {"name": "Norwegian", "extension": ".no.srt"},
    "CS": {"name": "Czech", "extension": ".cs.srt"},
    "HU": {"name": "Hungarian", "extension": ".hu.srt"},
    "RO": {"name": "Romanian", "extension": ".ro.srt"},
    "SK": {"name": "Slovak", "extension": ".sk.srt"},
    "TR": {"name": "Turkish", "extension": ".tr.srt"},
    "BG": {"name": "Bulgarian", "extension": ".bg.srt"},
    "EL": {"name": "Greek", "extension": ".el.srt"},
    "TH": {"name": "Thai", "extension": ".th.srt"},
    "VI": {"name": "Vietnamese", "extension": ".vi.srt"},
    "KO": {"name": "Korean", "extension": ".ko.srt"},
    "HR": {"name": "Croatian", "extension": ".hr.srt"},
    "LT": {"name": "Lithuanian", "extension": ".lt.srt"},
    "LV": {"name": "Latvian", "extension": ".lv.srt"},
    "SL": {"name": "Slovenian", "extension": ".sl.srt"}
}
```

### Translate a Single Movie or Series

To translate subtitles for a single movie or series, you can use the `/translate_srt` endpoint. Here’s an example request:

```bash
curl -X POST http://localhost:5000/translate_srt -H "Content-Type: application/json" -d '{
    "folder_path": "/media/Filmes/Exterminador do Futuro",
    "target_langs": ["PT-BR", "ES"],
    "source_lang": "EN"  # Optional
}
```
- Request Body:
- folder_path: Path to the folder containing the movie or series subtitles.
- target_langs: Array of target languages for translation.
- source_lang: (Optional) The source language of the subtitles.


```json
{
    "folder_path": "/subtitles",
    "target_lang": "PT-BR"
}
```

- Response:
```json
{
    "translated_files": [
        "/media/Filmes/Exterminador do Futuro/pt-BR.srt",
        "/media/Filmes/Exterminador do Futuro/es.srt"
    ]
}
```

## Determining Source Language
The source language is automatically determined based on the file extension of the .srt files. The mapping between file extensions and language codes is defined in the supported_languages.py file.
If the source language cannot be determined from the file extension, the API will return an error response with a status code of 400 and an error message indicating that the source language could not be determined.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
