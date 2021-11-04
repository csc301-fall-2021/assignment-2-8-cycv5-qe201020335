import requests
import pytest

BASE = "http://127.0.0.1:5000/"


def test_upload():
    file = {'file': open("test/time_series_test.csv")}
    response = requests.post(BASE + "time_series/death", files=file)
    assert response.content == b'Success'
    file['file'].close()
