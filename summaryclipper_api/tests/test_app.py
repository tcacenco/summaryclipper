import unittest
import os
import sys

# setting path to the root directory to import the modules
sys.path.append(__file__ + "/../..")
sys.path.append(__file__ + "/..")
os.chdir(os.path.dirname(os.path.dirname(__file__)))


class TestApp(unittest.TestCase):
    """
    # test the endpoints from app.py application
    """

    def setUp(self) -> None:
        """
        # Set up the test environment
        """

    def tearDown(self) -> None:
        """
        # Stop the patchers after each method runs
        """

    def test_health(self) -> None:
        """
        # test the health endpoint
        """

        from service import app

        app.testing = True
        app_tester = app.application.test_client()

        response = app_tester.get("/health")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
