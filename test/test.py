import requests
import unittest

BASE = "http://127.0.0.1:5000/"


class TestWebApi(unittest.TestCase):

    def test_upload(self):
        file = {'file': open("time_series_test.csv")}
        response = requests.post(BASE + "time_series/death", files=file)
        assert response.content == b'Success'
        file['file'].close()


if __name__ == '__main__':
    unittest.main()
