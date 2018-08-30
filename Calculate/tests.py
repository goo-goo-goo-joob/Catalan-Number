from django.test import TestCase
from Polygon import polygon


class PolygonTestCase(TestCase):

    def test_10_len_without_num(self):
        self.assertEqual(polygon('()' * 10, 'test.jpg', False), 0, "Can't create img for 10 len without num")

    def test_10_len_with_num(self):
        self.assertEqual(polygon('()' * 10, 'test.jpg', True), 0, "Can't create img for 10 len with num")

    def test_20_len_without_num(self):
        self.assertEqual(polygon('()' * 20, 'test.jpg', False), 0, "Can't create img for 20 len without num")

    def test_20_len_with_num(self):
        self.assertEqual(polygon('()' * 20, 'test.jpg', True), 0, "Can't create img for 20 len with num")

    def test_50_len_without_num(self):
        self.assertEqual(polygon('()' * 50, 'test.jpg', False), 0, "Can't create img for 50 len without num")

    def test_50_len_with_num(self):
        self.assertEqual(polygon('()' * 50, 'test.jpg', True), 0, "Can't create img for 50 len with num")

    def test_60_len_without_num(self):
        self.assertEqual(polygon('()' * 60, 'test.jpg', False), 0, "Can't create img for 60 len without num")

    def test_60_len_with_num(self):
        self.assertEqual(polygon('()' * 60, 'test.jpg', True), 0, "Can't create img for 60 len with num")

    def test_60_multi_len_without_num(self):
        self.assertEqual(polygon('(' * 30 + ')' * 30, 'test.jpg', False), 0, "Can't create img for 60 multi len without num")

    def test_60_multi_len_with_num(self):
        self.assertEqual(polygon('(' * 30 + ')' * 30, 'test.jpg', True), 0, "Can't create img for 60 multi len with num")
