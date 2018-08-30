from django.test import TestCase
from Polygon import polygon


class PolygonTestCase(TestCase):

    def test_40_len_without_num(self):
        self.assertEqual(polygon('()' * 40, 'test.jpg', False), 0, "Can't create img for 40 len without num")

    def test_40_len_with_num(self):
        self.assertEqual(polygon('()' * 40, 'test.jpg', True), 0, "Can't create img for 40 len with num")

    def test_40_multi_len_without_num(self):
        self.assertEqual(polygon('(' * 20 + ')' * 20, 'test.jpg', False), 0, "Can't create img for 40 multi len without num")

    def test_40_multi_len_with_num(self):
        self.assertEqual(polygon('(' * 20 + ')' * 20, 'test.jpg', True), 0, "Can't create img for 40 multi len with num")
