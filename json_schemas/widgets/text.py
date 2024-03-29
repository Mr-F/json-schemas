from typing import Any

from json_schemas.widgets.base import BaseWidget


class JSONTextWidget(BaseWidget):

    default_input_type: str = "text"
    default_input_attributes: list[str] = ["mask", "placeholder"]

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = kwargs.get("input_type", self.default_input_type)
        kwargs["input_attributes"] = kwargs.get("input_attributes", self.default_input_attributes)
        super().__init__(*args, **kwargs)
