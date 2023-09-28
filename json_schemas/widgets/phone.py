from json_schemas.widgets.base import BaseWidget


class JSONPhoneWidget(BaseWidget):

    default_input_type: str = "phone"
    default_input_attributes: list[str] = ["placeholder"]
