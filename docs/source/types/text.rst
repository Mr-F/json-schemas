.. include:: key_descriptions

.. |title_description| Title description todo

Text Type
=========

.. csv-table::
   :widths: 35, 100

   **Type**, text
   **HTML equivalence**, Yes
   **HTML example**, <input type="text" name="example" />


Description
-----------

TODO

JSON Example
------------

.. code-block:: json

   {
       "type": "text",
       "name": "input_name",
       "title": "Input A",
       "value": null,
       "render_option": "default"
   }


.. csv-table::
   :header: Key, Required, Type, Description

   type, Yes, enum, |type_description|
   name, Yes, string, ""
   title, Yes, string, |title_description|
   value, Yes, null or string, ""
   placeholder, No, string, ""
   mask, No, string, ""
   readonly, No, boolean, ""
   disabled, No, boolean, ""
   group_name, No, string, ""
   error_msg, No, string, ""
   conditional, No, object, ""
   conditional_required, No, boolean, ""