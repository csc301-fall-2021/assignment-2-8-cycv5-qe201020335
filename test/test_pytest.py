import subprocess

import requests
import pytest
# from main import app as flask_app

BASE = "http://127.0.0.1:5000/"


# @pytest.fixture
# def app():
#     flask_app.run(debug=True)


def test_upload():
    subprocess.Popen(["python", "main.py"])
    file = {'file': open("test/time_series_test.csv")}
    response = requests.post(BASE + "time_series/death", files=file)
    assert response.content == b'Success'
    file['file'].close()
