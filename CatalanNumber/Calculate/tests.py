from django.test import TestCase
from .scripts import callPolygon, callBinTree, callRootTree, callTableJung
import platform
import subprocess


class PolygonTestCase(TestCase):

    def test_40_len_without_num(self):
        self.assertEqual(callPolygon('()' * 40, 'test.jpg', False), 0, "Can't create img for 40 len without num")

    def test_40_len_with_num(self):
        self.assertEqual(callPolygon('()' * 40, 'test.jpg', True), 0, "Can't create img for 40 len with num")

    def test_40_multi_len_without_num(self):
        self.assertEqual(callPolygon('(' * 20 + ')' * 20, 'test.jpg', False), 0, "Can't create img for 40 multi len without num")

    def test_40_multi_len_with_num(self):
        self.assertEqual(callPolygon('(' * 20 + ')' * 20, 'test.jpg', True), 0, "Can't create img for 40 multi len with num")


class BinaryTestCase(TestCase):

    def test_40_len_without_num(self):
        self.assertEqual(callBinTree('()' * 40, 'test.jpg', False), 0, "Can't create img for 40 len without num")

    def test_40_len_with_num(self):
        self.assertEqual(callBinTree('()' * 40, 'test.jpg', True), 0, "Can't create img for 40 len with num")

    def test_40_multi_len_without_num(self):
        self.assertEqual(callBinTree('(' * 20 + ')' * 20, 'test.jpg', False), 0, "Can't create img for 40 multilen without num")

    def test_40_multi_len_with_num(self):
        self.assertEqual(callBinTree('(' * 20 + ')' * 20, 'test.jpg', True), 0, "Can't create img for 40 multilen with num")


class RootedTestCase(TestCase):

    def test_40_len_without_num(self):
        self.assertEqual(callRootTree('()' * 40, 'test.jpg', False), 0, "Can't create img for 40 len without num")

    def test_40_len_with_num(self):
        self.assertEqual(callRootTree('()' * 40, 'test.jpg', True), 0, "Can't create img for 40 len with num")

    def test_40_multi_len_without_num(self):
        self.assertEqual(callRootTree('(' * 20 + ')' * 20, 'test.jpg', False), 0, "Can't create img for 40 multi len without num")

    def test_40_multi_len_with_num(self):
        self.assertEqual(callRootTree('(' * 20 + ')' * 20, 'test.jpg', True), 0, "Can't create img for 40 multi len with num")


class TableTestCase(TestCase):

    def test_40_len(self):
        self.assertEqual(callTableJung('()' * 40, 'test.jpg'), 0, "Can't create img for 40 len")

    def test_40_multi_len(self):
        self.assertEqual(callTableJung('(' * 20 + ')' * 20, 'test.jpg'), 0, "Can't create img for 40 multi len")
