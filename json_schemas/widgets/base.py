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
        self.input_attributes = []
        self.__dict__.update(kwargs)


    def _get_translatable_attr(self, field, key: str) -> dict[str, str]:
        data = dict()
        value = getattr(field.schema, key, None)
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
        return getattr(field.schema, "required", True)

    def is_readonly(self, field) -> bool:
        return self.readonly

    def is_disabled(self, field) -> bool:
        return self.disabled

    def get_description(self, field) -> dict[str, str]:
        return self._get_translatable_attr(field, "description")

    def get_tooltip(self, field) -> dict[str, str]:
        return self._get_translatable_attr(field, "tooltip")

    def get_group_name(self, field) -> dict[str, str]:
        value = self._get_translatable_attr(field, "group_name")
        if value in [None, ""]:
            value = getattr(field.parent.schema, "default_group_name", None)
        return value

    def get_error_msg(self, field) -> dict[str, str]:
        data = dict()
        error_msg = getattr(field.schema, "error_msg", None)
        if error_msg is not None:
            data["error_msg"] = error_msg
        return data

    def input_specific_data(self, field) -> dict[str, Any]:
        """
        Any widgets that have input specific values should override this function and return the values
        that they wish to set e.g.

            - Options widget: will need to set the "options", "mulitple" key-pairs
            - Checkbox widget: will need to set the "checked" key-pair
            - etc

        :param field:
        :return:
        """
        data = dict()
        for input_attrib in self.input_attributes:
            value = getattr(field.schema, input_attrib, None)
            if value is not None:
                data[input_attrib] = value
        return data

    def get_component_options_data(self, field) -> dict[str, Any]:
        data = dict()
        return data

    def get_validation_data(self, field) -> dict[str, Any]:
        data = dict()
        return data

    def get_conditional_data(self, field) -> dict[str, Any]:
        data = dict()
        return data

    def get_derived_options_data(self, field) -> dict[str, Any]:
        data = dict()
        return data

    def serialize(self, field, cstruct, **kwargs) -> str:
        # Determine if the serialization should be readonly by checking both the kwargs and the readonly flag set on
        # the instance.
        # Test and make sure if we are handed a colander.null that it is converted to a None value
        if cstruct is colander.null:
            if not self.is_readonly(field):
                cstruct = None
            else:
                cstruct = self.readonly_null_value

        # Setup all the required core data values which are required
        input_definition = dict(
            input_type=self.input_type,
            name=self.name,
            title=self.title,
            value=cstruct,
            required=self.is_required(field),
        )

        # Adding in the readonly flag, if needed
        if self.is_readonly(field):
            input_definition["readonly"] = True

        # Adding in the disabled flag, if needed
        if self.is_disabled(field):
            input_definition["disabled"] = True

        # Adding the description data
        input_definition.update(self.get_description(field))

        # Add the tooltip value (if needed) to the dictionary
        input_definition.update(self.get_tooltip(field))

        # Add the group name (or default group name, if defined) to the dictionary
        input_definition.update(self.get_group_name(field))

        # Add in the error_msg if available
        input_definition.update(self.get_error_msg(field))

        # Add the input specific values
        input_definition.update(self.input_specific_data(field))

        # component_options
        obj_data = self.get_component_options_data(field)
        if obj_data is not {}:
            input_definition["component_options"] = obj_data

        # derived_options
        if not self.is_readonly(field):
            obj_data = self.get_derived_options_data(field)
            if obj_data is not {}:
                input_definition["derived_options"] = obj_data

        # validations
        if not self.is_readonly(field):
            obj_data = self.get_validation_data(field)
            if obj_data is not {}:
                input_definition["validation"] =  obj_data

        # conditional
        obj_data = self.get_conditional_data(field)
        if obj_data is not {}:
            input_definition["conditional"] = obj_data

        return json.dumps(input_definition)

    def deserialize(self, field, pstruct):
        pass