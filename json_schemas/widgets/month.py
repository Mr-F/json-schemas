from json_schemas.widgets.date import JSONDateWidget


class JSONMonthWidget(JSONDateWidget):

    # Currently this isn't supported in Safari or Firefox, so using a custom rendering option for the moment
    # default_input_type: str = "month"
    default_render_option: str = "month"
