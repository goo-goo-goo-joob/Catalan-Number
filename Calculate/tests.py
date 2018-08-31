from django.test import TestCase
from Polygon import polygon
import platform
import subprocess


class PolygonTestCase(TestCase):

    def test_40_len_without_num(self):
        self.assertEqual(polygon('()' * 40, 'test.jpg', False), 0, "Can't create img for 40 len without num")

    def test_40_len_with_num(self):
        self.assertEqual(polygon('()' * 40, 'test.jpg', True), 0, "Can't create img for 40 len with num")

    def test_40_multi_len_without_num(self):
        self.assertEqual(polygon('(' * 20 + ')' * 20, 'test.jpg', False), 0, "Can't create img for 40 multi len without num")

    def test_40_multi_len_with_num(self):
        self.assertEqual(polygon('(' * 20 + ')' * 20, 'test.jpg', True), 0, "Can't create img for 40 multi len with num")


class BinaryTestCase(TestCase):

    def test_40_len_without_num(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Br_Tr.o', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len without num")
        else:
            self.assertEqual(subprocess.call(['./Cat_Br_Tr.exe', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len without num")

    def test_40_len_with_num(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Br_Tr_Num.o', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len with num")
        else:
            self.assertEqual(subprocess.call(['./Cat_Br_Tr_Num.exe', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len with num")

    def test_40_multi_len_without_num(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Br_Tr.o', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 len without num")
        else:
            self.assertEqual(subprocess.call(['./Cat_Br_Tr.exe', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 len without num")

    def test_40_multi_len_with_num(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Br_Tr_Num.o', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 multi len without num")
        else:
            self.assertEqual(subprocess.call(['./Cat_Br_Tr_Num.exe', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 multi len with num")


class RootedTestCase(TestCase):

    def test_40_len_without_num(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Tree_Win.o', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len without num")
        else:
            self.assertEqual(subprocess.call(['./Cat_Tree_Win.exe', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len without num")

    def test_40_len_with_num(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Tree_Win_Num.o', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len with num")
        else:
            self.assertEqual(subprocess.call(['./Cat_Tree_Win_Num.exe', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len with num")

    def test_40_multi_len_without_num(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Tree_Win.o', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 len without num")
        else:
            self.assertEqual(subprocess.call(['./Cat_Tree_Win.exe', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 len without num")

    def test_40_multi_len_with_num(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Tree_Win_Num.o', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 multi len without num")
        else:
            self.assertEqual(subprocess.call(['./Cat_Tree_Win_Num.exe', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 multi len with num")


class TableTestCase(TestCase):

    def test_40_len(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Jung.o', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len")
        else:
            self.assertEqual(subprocess.call(['./Cat_Jung.exe', '()' * 40, 'test.jpg']), 0, "Can't create img for 40 len")

    def test_40_multi_len(self):
        if platform.system() == 'Linux':
            self.assertEqual(subprocess.call(['./Cat_Jung.o', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 len")
        else:
            self.assertEqual(subprocess.call(['./Cat_Jung.exe', '(' * 20 + ')' * 20, 'test.jpg']), 0, "Can't create img for 40 len")
