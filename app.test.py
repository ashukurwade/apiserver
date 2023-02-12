import unittest
from app import app
class BasicTestCase(unittest.TestCase):
    def test_home(self):
            tester = app.test_client(self)
            response = tester.get('/', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Hello World')

    def test_banklist(self):
        tester = app.test_client(self)
        response = tester.get('/banklist', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '_main_':
    unittest.main()