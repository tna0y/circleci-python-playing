import pytest
import requests

class TestHWApp:

    def test_hw(self):
        resp = requests.get('http://localhost:5000/hw')
        assert resp.status_code == 200
        assert resp.text == 'Hello, World'

    def test_fail(self):
        assert False
