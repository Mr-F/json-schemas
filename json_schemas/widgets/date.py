from json_schemas.widgets.base import BaseWidget


class JSONDateWidget(BaseWidget):

    default_input_type: str = "date"
    default_input_attributes: list[str] = []
    default_render_option: str = "day"

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = kwargs.get("input_type", self.default_input_type)
        kwargs["input_attributes"] = kwargs.get("input_attributes", self.default_input_attributes)
        kwargs["render_option"] = kwargs.get("render_option", self.default_render_option)
        super().__init__(*args, **kwargs)
