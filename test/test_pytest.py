import subprocess
from time import sleep

import requests
import pytest
# from main import app as flask_app

BASE = "http://127.0.0.1:5000/"

server = subprocess.Popen(["python", "main.py"])
sleep(2)
# @pytest.fixture
# def test_app():
#     subprocess.Popen(["python", "main.py"])


def test_upload_time_series():
    file = {'file': open("test/time_series_test.csv")}
    response = requests.post(BASE + "time_series/death", files=file)
    assert response.content == b'Success'
    file['file'].close()


def test_upload_daily_report():
    file = {'file': open("test/daily_report_test.csv")}
    response = requests.post(BASE + "daily_reports", files=file)
    assert response.content == b'Success'
    file['file'].close()
