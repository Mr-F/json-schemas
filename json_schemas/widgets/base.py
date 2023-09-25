import json
import logging
from typing import Any, Optional

import colander

log = logging.getLogger(__name__)

class BaseWidget:

    input_type: str = "text"
    name: str
    title: str
    readonly: bool = False
    readonly_null_value: Any = None
    disabled: bool = False

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def _get_translatable_attr(self, field, key: str) -> dict[str, str]:
        data = dict()
        value = getattr(self, key, None)
        if value is not None:
            if isinstance(value, str):
                # TODO: Add call the i18n library for the value if it's a string
                pass
            data[key] = value
        return data

    def is_required(self, field: colander.SchemaNode) -> bool:
        """
        This function determines if the input should be defined as being required.
        :param field:
        :return:
        """
        return getattr(field, True)

    def get_description(self, field) -> dict[str, str]:
        return self._get_translatable_attr(field, "description")

    def get_tooltip(self, field) -> dict[str, str]:
        return self._get_translatable_attr(field, "tooltip")

    def get_group_name(self, field) -> Optional[str]:
        value = self._get_translatable_attr(field, "group_name")
        if value in [None, ""]:
            value = getattr(field.parent.schema, "default_group_name", None)
        if isinstance(value, str):
            # TODO: Add call the i18n library for the value if it's a string
            pass
        return value

    def get_error_msg(self):
        pass

    def input_specific_data(self, field) -> dict:
        return dict()

    def core_data(self, field, cstruct: Any) -> dict:
        """
        This is the function that returns the core data, checking if keys are set and if so adding them to the base
        dictionary, or appropriate default where necessary.

        :param field:
        :param cstruct:
        :return:
        """
        pass

    def serialize(self, field, cstruct, **kwargs) -> str:
        # Determine if the serialization should be readonly by checking both the kwargs and the readonly flag set on
        # the instance.
        # Test and make sure if we are handed a colander.null that it is converted to a None value
        if cstruct is colander.null:
            if not self.readonly:
                cstruct = None
            else:
                cstruct = self.readonly_null_value

        # Setup all the required core data values which are required
        core_data = dict(
            input_type=self.input_type,
            name=self.name,
            title=self.title,
            value=cstruct,
            required=self.is_required(field),
        )

        # Adding the description data
        core_data.update(self.get_description(field))

        # Add the group name (or default group name, if defined) to the dictionary
        core_data.update(self.get_group_name(field))

        # Add the tooltip value (if needed) to the dictionary
        core_data.update(self.get_tooltip(field))

        # Next add in the optional keys which will require i18n support
        optional_keys = [ "error_msg"]
        for key in optional_keys:
            value = getattr(field.schema, key, None)
            if value is not None:
                if isinstance(value, str):
                    # TODO: Add call the i18n library for the value if it's a string
                    pass
                core_data[key] = value

        # Add in other optional keys which are defined by the widget
        for key in optional_keys:
            value = getattr(self, key, None)
            # If the value is anything other than None or False then add to the data, otherwise skip
            if value not in [None, False]:
                core_data[key] = value

        # Add the input specific values
        core_data.update(self.input_specific_data(field))

        # Add the render options

        # "render_options",
        # "validations",
        # "conditional"

        return json.dumps(core_data)

    def deserialize(self, field, pstruct):
        pass