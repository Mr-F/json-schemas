Text Type
=========

.. csv-table::
   :widths: 2, 4

   **Type**, text
   **HTML equivalence**, Yes
   **HTML example**, <input type="text" name="example" />


Description
-----------



JSON Example
------------

Simple example

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
   :widths: 2, 1, 2, 10

   type, Yes, enum, |type_description|
   name, Yes, string, |name_description|
   title, Yes, string, |title_description|
   value, Yes, null or string, ""
   placeholder, No, string, |placeholder_description|
   mask, No, string, |mask_description|
   readonly, No, boolean, |readonly_description|
   disabled, No, boolean, |disabled_description|
   group_name, No, string, |group_name_description|
   error_msg, No, string, |error_msg_description|
   conditional, No, object, ""
   conditional_required, No, boolean, ""