.. include:: key_descriptions

Text Widget
===========

This widget models a basic text input type.  This is the normally the default mapping for Colander type Str or String.

Example
-------

A simple text input example would look like this.

.. code-block:: python

    colander.SchemaNode(
        colander.String(),
        name="input_name",
        title="Input title",
        widget=JSONTextInputWidget()
    )

This would generate the following JSON output.

.. code-block:: json

    {
        "type": "text",
        "name": "input_name",
        "title": "Input title",
        "value": null,
        "required": true
    }

Parameters
----------

.. csv-table::
   :header: Key, Required, Type, Description
   :widths: 2, 1, 2, 5

    type, Yes, String, This will be "text". |type_description|
    name, Yes, String, |name_description|
    title, Yes, String, |title_description|
    value, Yes, String or null, ""
    required, Yes, Boolean, |required_description|
    description, No, String, |description_description|
    placeholder, No, String, |placeholder_description|
    mask, No, String, |mask_description|
    readonly, No, Boolean, |readonly_description|
    disabled, No, Boolean, |disabled_description|
    group_name, No, String, |group_name_description|
    error_msg, No, String, |error_msg_description|
    conditional, No, Object, ""
    conditional_required, No, boolean, ""



JSON Schema
-----------

.. code-block:: json

    {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$id": "http://example.com/example.json",
        "type": "object",
        "default": {},
        "title": "Root Schema",
        "required": [
            "type",
            "name",
            "title",
            "value",
            "required"
        ],
        "properties": {
            "type": {
                "type": "string",
                "default": "",
                "title": "The type Schema",
                "examples": [
                    "text"
                ]
            },
            "name": {
                "type": "string",
                "default": "",
                "title": "The name Schema",
                "examples": [
                    "input_name"
                ]
            },
            "title": {
                "type": "string",
                "default": "",
                "title": "The title Schema",
                "examples": [
                    "Input title"
                ]
            },
            "value": {
                "type": "null",
                "default": null,
                "title": "The value Schema",
                "examples": [
                    null
                ]
            },
            "required": {
                "type": "boolean",
                "default": false,
                "title": "The required Schema",
                "examples": [
                    true
                ]
            }
        },
        "examples": [{
            "type": "text",
            "name": "input_name",
            "title": "Input title",
            "value": null,
            "required": true
        }]
    }