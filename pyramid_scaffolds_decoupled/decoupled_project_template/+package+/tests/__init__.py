import unittest
from pyramid import testing

class TestView(unittest.TestCase):
    def setUp(self):
        testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_it(self):
        from {{package}}.views import my_view
        request = testing.DummyRequest()
        response = my_view(request)
        self.assertEqual(response['hello'], 'world')
