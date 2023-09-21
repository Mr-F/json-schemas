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
   :widths: 2, 1, 2, 10

    type, Yes, String, This will be "text". |type_description|
    name, Yes, String, |name_description|
    title, Yes, String, |title_description|
    value, Yes, String or null, ""
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

To generate