import unittest
import time

from lr1.sync import download_all_sites


#@unittest.skip
class Test210902Sync(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()

    def test_100(self):
        self.sites = [
            "https://www.python.org",
            "https://google.com",
        ] * 50

        res = download_all_sites(self.sites)
        self.assertEqual(len(self.sites), len(res))

    def tearDown(self):
        duration = time.time() - self.start_time
        print(f"{self.id()}: Downloaded {len(self.sites)} in {duration} seconds")
