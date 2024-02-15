import pytest
import requests
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from client.client import get_data, post_data

# Test pour get_data
def test_get_data():
    response = get_data("http://127.0.0.1:5000/villes")

    assert isinstance(response, list)

# Test pour post_data
def test_post_data():
    data = {"prix": 300}

    status = post_data("http://127.0.0.1:5000/prix/Centre/Berlin", data)

    assert status == 405

