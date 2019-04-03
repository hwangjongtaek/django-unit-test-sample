from django.test import TestCase


class CrawlerTests(TestCase):

    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertEqual(3, 3)

    def test_3(self):
        self.assertEqual(4, 4)


class ConverterTests(TestCase):

    def test_1(self):
        self.assertEqual(1, 1)

    def test_2(self):
        self.assertEqual(3, 3)

    def test_3(self):
        self.assertEqual(4, 4)
