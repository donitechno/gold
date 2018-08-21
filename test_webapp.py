import unittest
import main
# from webapp import app
# from webapp import home


class HomeViewTest(unittest.TestCase):

    def setUp(self):
    	self.app = main.app.test_client()
    	self.app.testing = True

    def test_home_page(self):
        home = self.app.get('/')
        self.assertIn('Home Page', str(home.data))


if __name__ == "__main__":
    unittest.main()
