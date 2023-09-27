from json_schemas.widgets.base import BaseWidget


class JSONPhoneWidget(BaseWidget):

    def __init__(self, *args, **kwargs):
        kwargs["input_type"] = "text"
        super().__init__(*args, **kwargs)
        self.input_attributes = ["placeholder"]
