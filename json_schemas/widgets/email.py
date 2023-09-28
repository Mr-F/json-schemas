from json_schemas.widgets.base import BaseWidget


class JSONEmailWidget(BaseWidget):

    default_input_type: str = "email"
    default_input_attributes: list[str] = ["multiple", "placeholder"]
