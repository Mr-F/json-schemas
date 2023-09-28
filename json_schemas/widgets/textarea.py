from json_schemas.widgets.base import BaseWidget


class JSONTextAreWidget(BaseWidget):

    default_input_type: str = "textarea"
    default_input_attributes: list[str] = ["rows", "cols"]