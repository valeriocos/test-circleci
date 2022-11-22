import os
from unittest import TestCase, mock

from ..src.app import prepare_message


class DummyTestCase(TestCase):
    @mock.patch.dict(os.environ, {"SETTINGS_MODULE": "test"}, clear=True)
    def test_prepare_message(self):
        expected_message = {"body": "Hello, CDK! You are in test"}
        self.assertDictEqual(prepare_message(), expected_message)
