import sys
import os
from unittest.mock import patch
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser import analyze_page


def test_valid_url():
    result = analyze_page("https://example.com")
    assert "status" in result


def test_invalid_url():
    result = analyze_page("abcd.invalid")
    assert "error" in result


@patch("parser.requests.get")
def test_request_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout

    result = analyze_page("https://example.com")

    assert "error" in result