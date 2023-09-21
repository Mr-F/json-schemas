import json

import colander

class BaseWidget:

    input_type: str = "text"
    name: str
    title: str
    readonly: bool = False
    disabled: bool = False

    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    def get_base_data(self, field, cstruct) -> dict:
        return dict(
            type=self.input_type,
            name=self.name,
            title=self.title,
            value=cstruct,
        )

    def add_conditional_data(self, field):
        pass

    def readonly_serialize(self, field, cstruct: dict) -> dict:
        if cstruct in (colander.null, None):
            cstruct = self.readonly_null_value
        data = self._base_data(cstruct, field)
        data["readonly"] = True
        return data

    def serialize(self, field, cstruct, **kwargs) -> str:
        # Determine if the serialization should be readonly by checking both the kwargs and the readonly flag set on
        # the instance.
        # TODO: Do we ever pass it in via the serailization call, if not maybe we could drop this.
        readonly = kwargs.get("readonly") | self.readonly

        if not readonly:
            data = dict()
        else:
            data = dict()

        return json.dumps(data)

    def deserialize(self, field, pstruct):
        pass