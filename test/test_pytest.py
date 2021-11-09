import subprocess
from time import sleep
import os

import requests
import pytest

BASE = "http://127.0.0.1:5000/"

os.environ["FLASK_APP"] = "main"
server = subprocess.Popen(["flask", "run"])  # start server

sleep(3)


def test_upload_time_series_death():
    file = {'file': open("test/time_series_test.csv")}
    response = requests.post(BASE + "time_series/death", files=file)
    assert response.content == b'Success'
    file['file'].close()


def test_upload_time_series_confirmed():
    file = {'file': open("test/time_series_test.csv")}
    response = requests.post(BASE + "time_series/confirmed", files=file)
    assert response.content == b'Success'
    file['file'].close()


def test_upload_time_series_active():
    file = {'file': open("test/time_series_test.csv")}
    response = requests.post(BASE + "time_series/active", files=file)
    assert response.content == b'Success'
    file['file'].close()


def test_upload_time_series_recovered():
    file = {'file': open("test/time_series_test.csv")}
    response = requests.post(BASE + "time_series/recovered", files=file)
    assert response.content == b'Success'
    file['file'].close()


def test_upload_daily_report():
    file = {'file': open("test/daily_report_test.csv")}
    response = requests.post(BASE + "daily_reports/2020-03-25", files=file)
    assert response.content == b'Success'
    file['file'].close()


def test_upload_error():
    response = requests.post(BASE + "daily_reports/2020")
    assert response.content == b'no file part'


def test_query_multi_types_multi_date_json():
    req = BASE + 'cases?data_type=death&data_type=confirmed&locations=%7B%0A%20%20%22country%22%3A%20%22US%22%2C%0A%20%20%22state%22%3A%20%22Kentucky%22%2C%0A%20%20%22combined%22%3A%20%22%22%0A%7D&locations=%7B%0A%20%20%22country%22%3A%20%22Canada%22%2C%0A%20%20%22state%22%3A%20%22British%20Columbia%22%2C%0A%20%20%22combined%22%3A%20%22%22%0A%7D&start_time=2020-01-23&end_time=2020-01-31'
    response = requests.get(req, headers={'accept': 'application/json'})
    assert response.json() == [{'country_region': 'US', 'state_province': 'Kentucky', 'combined_key': '', 'date': '2020-01-23', 'cases': 2, 'type': 'death'}, {'country_region': 'US', 'state_province': 'Kentucky', 'combined_key': '', 'date': '2020-01-24', 'cases': 3, 'type': 'death'}, {'country_region': 'US', 'state_province': 'Kentucky', 'combined_key': '', 'date': '2020-01-25', 'cases': 122, 'type': 'death'}, {'country_region': 'US', 'state_province': 'Kentucky', 'combined_key': '', 'date': '2020-01-26', 'cases': 3, 'type': 'death'}, {'country_region': 'US', 'state_province': 'Kentucky', 'combined_key': '', 'date': '2020-01-23', 'cases': 2, 'type': 'confirmed'}, {'country_region': 'US', 'state_province': 'Kentucky', 'combined_key': '', 'date': '2020-01-24', 'cases': 3, 'type': 'confirmed'}, {'country_region': 'US', 'state_province': 'Kentucky', 'combined_key': '', 'date': '2020-01-25', 'cases': 122, 'type': 'confirmed'}, {'country_region': 'US', 'state_province': 'Kentucky', 'combined_key': '', 'date': '2020-01-26', 'cases': 3, 'type': 'confirmed'}, {'country_region': 'Canada', 'state_province': 'British Columbia', 'combined_key': '', 'date': '2020-01-23', 'cases': 2, 'type': 'death'}, {'country_region': 'Canada', 'state_province': 'British Columbia', 'combined_key': '', 'date': '2020-01-24', 'cases': 4, 'type': 'death'}, {'country_region': 'Canada', 'state_province': 'British Columbia', 'combined_key': '', 'date': '2020-01-26', 'cases': 5, 'type': 'death'}, {'country_region': 'Canada', 'state_province': 'British Columbia', 'combined_key': '', 'date': '2020-01-23', 'cases': 2, 'type': 'confirmed'}, {'country_region': 'Canada', 'state_province': 'British Columbia', 'combined_key': '', 'date': '2020-01-24', 'cases': 4, 'type': 'confirmed'}, {'country_region': 'Canada', 'state_province': 'British Columbia', 'combined_key': '', 'date': '2020-01-26', 'cases': 5, 'type': 'confirmed'}]


def test_query_single_type_multi_date_csv():
    req = BASE + 'cases?data_type=active&locations=%7B%0A%20%20%22country%22%3A%20%22Canada%22%2C%0A%20%20%22state%22%3A%20%22British%20Columbia%22%2C%0A%20%20%22combined%22%3A%20%22%22%0A%7D&start_time=2020-01-23&end_time=2020-01-31'
    response = requests.get(req, headers={'accept': 'text/csv'})
    assert response.content == b'index,country_region,state_province,combined_key,date,cases,type\n0,Canada,British Columbia,,2020-01-23,2,active\n1,Canada,British Columbia,,2020-01-24,4,active\n2,Canada,British Columbia,,2020-01-26,5,active\n'


def test_query_multi_type_single_date_csv():
    req = BASE + 'cases?data_type=active&data_type=recovered&locations=%7B%0A%20%20%22country%22%3A%20%22Canada%22%2C%0A%20%20%22state%22%3A%20%22British%20Columbia%22%2C%0A%20%20%22combined%22%3A%20%22%22%0A%7D&start_time=2020-01-23'
    response = requests.get(req, headers={'accept': 'text/csv'})
    assert response.content == b'index,country_region,state_province,combined_key,date,cases,type\n0,Canada,British Columbia,,2020-01-23,2,active\n1,Canada,British Columbia,,2020-01-23,2,recovered\n'


def test_query_single_type_single_date_json():
    req = BASE + 'cases?data_type=active&locations=%7B%0A%20%20%22country%22%3A%20%22Canada%22%2C%0A%20%20%22state%22%3A%20%22British%20Columbia%22%2C%0A%20%20%22combined%22%3A%20%22%22%0A%7D&start_time=2020-01-23'
    response = requests.get(req, headers={'accept': 'application/json'})
    assert response.json() == [{'country_region': 'Canada', 'state_province': 'British Columbia', 'combined_key': '', 'date': '2020-01-23', 'cases': 2, 'type': 'active'}]



