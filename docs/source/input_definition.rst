.. include:: descriptions.rst

Input Definition
================

In the JSON form scheme each input is defined by an object.  These objects define the different attributes for the
specific input, and can be groupped into top level keys which the consumer must support, followed by second level
details, which are helpful, but completely optional for the consumer to support.

Most of the top level parameters are common across all inputs types and include items such as type, name, title, value,
etc, but some input types do have additional parameters that can be defined e.g. select inputs have top level key that
defines the options that should be including in the select tag.  In addition to these top level parameters, there are
also optional secondary parameters that provide additional information that can be useful, including rendering hints,
submission data type, validation rules etc.

Top level parameters
--------------------

Below as a basic example of a what a text input could look like.

.. code-block:: json

    {
        "type": "text",
        "name": "user_name",
        "title": "Please enter your name",
        "value": null,
        "required": true,
    }

The above definition defines a text input which when the value is submitted should be associated with the key
"user_name".  The title/label associated with the input should display "Please enter your name" and the field is
required.

The table below outine the common top level parameters that consumers of the JSON schema should implement support for.

.. csv-table::
    :header: Key, Required, Type, Description
    :widths: 2, 1, 2, 5

    type, Yes, String, |type_description|
    name, Yes, String, |name_description|
    title, Yes, String, |title_description|
    value, Yes, String or null, The current value that should appear in the input on load.
    required, Yes, Boolean, |required_description|
    description, No, String, |description_description|
    readonly, No, Boolean, |readonly_description|
    disabled, No, Boolean, |disabled_description|
    group_name, No, String, |group_name_description|
    error_msg, No, String, |error_msg_description|

The text input widget also has additional top level parameter

.. csv-table::
    :header: Key, Required, Type, Description
    :widths: 2, 1, 2, 5

    mask, No, String, |mask_description|
    placeholder, No, String, |placeholder_description|

Secondary Optional Parameters
-----------------------------

Each of the secondary parameters are defined as an object.  The following are the currently supported secondary
optional parameters, which are common across all input types.

Key: rules
**********

.. csv-table::
    :header: Key, Required, Type, Description
    :widths: 2, 1, 2, 5

    type, Yes, String,
    multiple, No, Boolean,
    render_option, No, String
    custom_support, No, ?,
    copy_from, No, String,
    locked, No, Boolean,
    derived_value, No, List,
    derived_options, No, Object,
    display_format, No, ?,
    derived_lookup, No, String,
    derived_form_lookup, No, String,

Key: validation
***************

The validation object contains information about generic validations that will be applied to the data being submitted.
Obviously not all validations are possible to express in this manner, however, were possible information will be
included to allow the consumer of the JSON schema to perform client side validation before submitting to the server.
This will allow you to provide a better experience for the user if you so choose to support it.

Below is a simple example of a min, max validation rules

.. code-block::

    "validation": {
        "min": 1,
        "max": 10,
    }

For more information about validation rules and how they are expressed in the validaiton block please see TODO: LINK


Key: conditional
****************

.. code-block::

    "conditional": {
        "conditions": {
            "field_name": [value_1, value_2]
        },
        "conditional_required": true
    }

.. note::

    Check the logic for the conditional, as I believe we added the ability to OR values as well at somet point.

.. csv-table::
    :header: Key, Required, Type, Description
    :widths: 2, 1, 2, 5

    conditions, Yes, Object, "An object that contains a list of keys which maps to other field names in the same form, and the values that is the input matches should be considered as meeting. If there are multiple field names in this object the results of each test should be ANDed together."
    conditional_required, No, Boolean, "If the condition are meet whether the input should be considered as being a required input before submitting."

