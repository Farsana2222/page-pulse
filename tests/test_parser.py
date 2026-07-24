import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser import analyze_page


def test_valid_url():
    result = analyze_page("https://example.com")
    assert "status" in result


def test_invalid_url():
    result = analyze_page("abcd.invalid")
    assert "error" in result