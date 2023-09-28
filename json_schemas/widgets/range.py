from json_schemas.widgets.number import JSONNumberWidget


class JSONRangeWidget(JSONNumberWidget):

    default_input_type: str = "range"
