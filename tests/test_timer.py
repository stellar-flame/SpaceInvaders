import time
from unittest import TestCase


class TestTimer(TestCase):
    def test_is_stopped(self):
        timer = Timer(2)
        timer.start()
        self.assertFalse(timer.is_stopped())

        time.sleep(2)
        self.assertTrue(timer.is_stopped())
