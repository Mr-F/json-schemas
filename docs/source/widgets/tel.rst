.. include:: ../descriptions.rst


Telephone Widget
================

This widget models a telephone input.  Using this specific input type allows the consumer to tigger custom UX elements
such as mobile phone keypads when entering this information.

Example
-------

A simple text input example would look like this.

.. code-block:: python

    colander.SchemaNode(
        colander.String(),
        name="phone_number",
        title="Your phone number",
        widget=JSONPhoneWidget()
    )

This would generate the following JSON output.

.. code-block:: json

    {
        "type": "tel",
        "name": "phone_number",
        "title": "Your phone number",
        "value": null,
        "required": true
    }

Parameters
----------

.. csv-table::
   :header: Key, Required, Type, Description
   :widths: 2, 1, 2, 5

    type, Yes, String, This will be "tel".
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

To generate