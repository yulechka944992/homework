import pytest
from unittest.mock import patch,mock_open
import json

from src.utils import load_json


def test_load_json():
    """Тест загрузки JSON-файла"""
    test_data = [{'id': 1}, {'id': 2}, {'id': 3}]
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            result = load_json('data.json')
            assert result == test_data

def test_json_not_exist():

    with patch("os.path.exists", return_value=False):
        result = load_json('missing.json')
        assert result == []

def test_file_exists_but_not_list():

    test_data = {'id': 1}
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            result = load_json('not_a_list.json')
            assert result == []

def test_file_exists_but_invalid_json():

    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data='invalid.json')):
            result = load_json('invalid.json')
            assert result == []
