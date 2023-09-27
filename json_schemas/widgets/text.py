from typing import Any

from json_schemas.widgets.base import BaseWidget

class JSONTextWidget(BaseWidget):

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = "text"
        super().__init__(*args, **kwargs)

    def input_specific_data(self, field) -> dict[str, Any]:
        data = dict()
        input_attributes = ["mask", "placeholder"]
        for input_attrib in input_attributes:
            value = getattr(field.schema, input_attrib, None)
            if value is not None:
                data[input_attrib] = value
        return data