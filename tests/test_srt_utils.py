import os
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

import srt_utils


def create_srt_file(path, name, content="1\n00:00:00,000 --> 00:00:02,000\nHello"):
    file_path = Path(path) / name
    file_path.write_text(content, encoding="utf-8")
    return file_path


def test_output_filename_without_language_extension(tmp_path):
    create_srt_file(tmp_path, "movie.en.srt")
    with patch.object(srt_utils, "translate_text", return_value="translated"):
        results = srt_utils.translate_srt_files(str(tmp_path), ["FR"], source_lang="EN")

    expected = tmp_path / "movie.FR.srt"
    assert str(expected) in results
    assert expected.read_text(encoding="utf-8") == "translated"


def test_output_filename_basic(tmp_path):
    create_srt_file(tmp_path, "show.srt")
    with patch.object(srt_utils, "translate_text", return_value="translated"):
        results = srt_utils.translate_srt_files(str(tmp_path), ["ES"], source_lang="EN")

    expected = tmp_path / "show.ES.srt"
    assert str(expected) in results
    assert expected.read_text(encoding="utf-8") == "translated"
