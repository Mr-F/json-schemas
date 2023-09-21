.. include:: key_descriptions


Email Widget
============

This widget models an email input.  Using this specific input type allows the consumer to tigger custom UX elements
which might be more appropriate for this type of input e.g. mobile modified keyboard which includes the '@' symbol by
default.

Example
-------

A simple text input example would look like this.

.. code-block:: python

    colander.SchemaNode(
        colander.String(),
        name="email",
        title="Your email address",
        widget=JSONEmailWidget()
    )

This would generate the following JSON output.

.. code-block:: json

    {
        "type": "email",
        "name": "email",
        "title": "Your email address",
        "value": null,
        "required": true
    }

Parameters
----------

.. csv-table::
   :header: Version, Date, Description
   :widths: 15, 20, 50

.. csv-table::
   :header: Key, Required, Type, Description
   :widths: 2, 1, 2, 5

    type, Yes, String, "| This will be 'email'.
    |type_description|"
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