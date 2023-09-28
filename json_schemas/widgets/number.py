from json_schemas.widgets.base import BaseWidget


class JSONNumberWidget(BaseWidget):

    default_input_type: str = "number"
    default_input_attributes: list[str] = ["mask", "placeholder", "step"]

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = kwargs.get("input_type", self.default_input_type)
        kwargs["input_attributes"] = kwargs.get("input_attributes", self.default_input_attributes)
        super().__init__(*args, **kwargs)