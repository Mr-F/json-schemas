.. include:: descriptions.rst

Input Definition
================

Each form input is defined as a JSON object, that contains a number of different attributes.  A number of attributes
are "core" and will be defined regardless of the input type, whilst others are specific to an type.  In addition, some
of the attributes are required for a valid definition, whilst others are completely optional.

The table below outlines the top level attributes that are currently supported.

.. csv-table::
    :header: Key, Core/Input Specific, Required, Data Type, Description
    :widths: 1, 1, 1, 2, 5

    type, Core, Yes, String, |type_description|
    name, Core, Yes, String, |name_description|
    title, Core, Yes, String, |title_description|
    value, Core, Yes, String or null, The current value that should appear in the input on load.
    required, Core, Yes, Boolean, |required_description|
    description, Core, No, String, |description_description|
    readonly, Core, No, Boolean, |readonly_description|
    disabled, Core, No, Boolean, |disabled_description|
    group_name, Core, No, String, |group_name_description|
    error_msg, Core, No, String, |error_msg_description|
    render_options, Core, No, Object,
    validation, Core, No, Object,
    conditional, Core, No, Object,

    placeholder, Input Specific, No, String,
    mask, Input Specific, No, String,
    options, Input Specific, No, List,
    multiple, Input Specific, No, Boolean,
    checked, Input Specific, No, Boolean,
    option_description, Input Specific, No, ?,
    display_format, Input Specific, No,
    rows, Input Specific, No, Integer,
    cols, Input Specific, No, Integer,

"render_options" Attribute
--------------------------

.. csv-table::
    :header: Key, Required, Type, Description
    :widths: 2, 1, 2, 5

    type, Yes, String,
    render_option, No, String
    copy_from, No, String,
    locked, No, Boolean,

    custom_support, No, ?,
    derived_value, No, List,
    derived_options, No, Object,
    derived_lookup, No, String,
    derived_form_lookup, No, String,



"validation" Attribute
----------------------
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


"conditional" Attribute
-----------------------
The conditional attribute, allows us to specify conditional logic on when and how specific fields should be displayed
and if they are required to be answered.  For example, a previous input might ask the user to select a reason, with the
final option being "other".  In these situation, the form designer might want to present a followup question to allow
for a free text entry from the user.  However, for people that select one of the predefined values they would not need
to answer this question.  This is what the conditional attributes defines.

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




In this JSON scheme for form inputs, each input is defined as an object.  These objects define the different attributes for the
specific input, and can be groupped into top level keys which the consumer must support, followed by second level
details, which are helpful, but completely optional for the consumer to support.

Most of the top level parameters are common across all inputs types and include items such as type, name, title, value,
etc, but some input types do have additional parameters that can be defined e.g. select inputs have top level key that
defines the options that should be including in the select tag.  In addition to these top level parameters, there are
also optional secondary parameters that provide additional information that can be useful, including rendering hints,
submission data type, validation rules etc.
