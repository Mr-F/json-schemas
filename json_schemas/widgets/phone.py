from json_schemas.widgets.base import BaseWidget


class JSONPhoneWidget(BaseWidget):

    default_input_type: str = "tel"
    default_input_attributes: list[str] = ["placeholder"]
