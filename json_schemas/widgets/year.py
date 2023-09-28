from json_schemas.widgets.date import JSONDateWidget


class JSONYearWidget(JSONDateWidget):

    default_render_option: str = "year"