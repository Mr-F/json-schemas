from json_schemas.widgets.base import BaseWidget


class JSONEmailWidget(BaseWidget):

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = "email"
        super().__init__(*args, **kwargs)
        self.input_attributes = ["multiple", "placeholder"]