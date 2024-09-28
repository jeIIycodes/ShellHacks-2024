import unittest
from app import create_app


api_server = create_app()

class BaseTestCase(unittest.TestCase):
    pass

class TestMultiplyFunction(unittest.TestCase):

    def test_multiplication(self):
        with api_server.test_client() as client:
            response = client.get('/testing/multiply/69/420')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), '28980')

    def test_missing_variable(self):
        with api_server.test_client() as client:
            response = client.get('/testing/multiply/420/')
            self.assertEqual(response.status_code, 404)

    def test_invalid_variable(self):
        with api_server.test_client() as client:
            response = client.get('/testing/multiply/69/fishies')
            self.assertEqual(response.status_code, 404)

