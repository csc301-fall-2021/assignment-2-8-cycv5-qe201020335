import requests
import unittest

BASE = "http://127.0.0.1:5000/"


class TestWebApi(unittest.TestCase):

    def test_upload(self):
        file = {'file': open("test/time_series_test.csv", 'rb')}
        response = requests.post(BASE + "time_series/", files=file)
        assert response.json() == {'first line in the file': "b'Province/State,Country/Region,Lat,Long,1/22/20,1/23/20,1/24/20,1/25/20,1/26/20\\r\\n'"}

    def test_get(self):
        response = requests.get(BASE + "query/china/death")
        assert response.json() == {'info': 'death', 'place': 'china'}


if __name__ == '__main__':
    unittest.main()
