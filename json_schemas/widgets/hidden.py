from json_schemas.widgets.base import BaseWidget


class JSONHiddenWidget(BaseWidget):

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = "hidden"
        kwargs["input_attributes"] = []
        super().__init__(*args, **kwargs)