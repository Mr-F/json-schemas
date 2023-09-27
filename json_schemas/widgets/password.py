from json_schemas.widgets.base import BaseWidget


class JSONPasswordWidget(BaseWidget):

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = "password"
        super().__init__(*args, **kwargs)
        self.input_attributes = ["placeholder", "inputmode"]
