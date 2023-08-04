import unittest
import os
import sys

# Setting path to the root directory to import the modules
# --------------------------------------------------------------------
# Get the absolute path to the directory containing this script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to sys.path (to import modules from there)
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

# Change the working directory to the parent directory
os.chdir(parent_directory)
# --------------------------------------------------------------------


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
