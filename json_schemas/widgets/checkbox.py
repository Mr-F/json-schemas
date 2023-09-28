from json_schemas.widgets.base import BaseWidget


class JSONCheckboxWidget(BaseWidget):

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = "checkbox"
        kwargs["input_attributes"] = ["checked"]
        super().__init__(*args, **kwargs)