from unittest import TestCase
from swf.datapackage import load


class TestLoad(TestCase):

    def test_load(self):
        descriptor = 'http://datahub.io/quidproquo/2016-survey-of-consumer-finances-summary-extract/datapackage.json'
        df = load(descriptor)

        self.assertIsNotNone(df)

        print(df)
