from unittest.mock import MagicMock

import pytest

from json_schemas.widgets.text import JSONTextWidget

class TestInputSpecificData:

    def test_no_values(self):
        mock_field = MagicMock(schema=MagicMock(spec=[]))
        assert JSONTextWidget().input_specific_data(mock_field) == dict()

    def test_mask_value_set(self):
        mock_field = MagicMock(schema=MagicMock(spec=["mask"], mask="Mask Value"))
        assert JSONTextWidget().input_specific_data(mock_field) == dict(mask="Mask Value")

    def test_placeholder_value_set(self):
        mock_field = MagicMock(schema=MagicMock(spec=["placeholder"], placeholder="Placeholder Value"))
        assert JSONTextWidget().input_specific_data(mock_field) == dict(placeholder="Placeholder Value")

    def test_all_values_set(self):
        mock_field = MagicMock(
            schema=MagicMock(
                spec=["mask", "placeholder"],
                placeholder="Placeholder Value",
                mask="Mask Value"
            )
        )
        expected_result = dict(mask="Mask Value", placeholder="Placeholder Value")
        assert JSONTextWidget().input_specific_data(mock_field) == expected_result