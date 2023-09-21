Input Types
===========

Input types are a concept to allow the form designer to suggest what sort of input type might be appropriate for the
rendering client to use when using HTML.  This does not mean that the consumer will use these items, for example where
the schema is being rendered outside of a web page.  As such input types typically map to a HTML input type or HTML tag.
There are some input types values which don't map directly to a HTML equivalent type or tag.


Type: checkbox
--------------



Type: content
-------------

This type isn't technically an input but a way for more rich content to be delivered from the server to the the
consumer.  As such no responses will ever be expected from a content type definition, and it is purely for rendering
information.

**HTML equivalence**

.. code-block::

    None

Type: date
-----------

This is used where date information needs to be collected.  Using the specific HTML equivalence tag will allow the
consumer to render the most appropriate input method for the device being used.

**HTML equivalance**

.. code-block::

    <input type="date" />

Type: email
-----------

**HTML equivalance:**

.. code-block::

    <input type="email" />

Type: file
----------

The file type allows for files to be uploaded via the form.

**HTML equivalence**

.. code-block::

    <input type="file" />

Type: hidden
------------

The hidden input type allows to the form to define elements which should be hidden and not rendered to the user.

**HTML equivalence**

.. code-block::

    <input type="hidden" />

Type: number
------------

The number input type allows for better support when collecting numerical data form the user.

**HTML equivalence**

.. code-block::

    <input type="number" />

Type: password
--------------

The password input type allows for the user to enter a password, and for the values to automatically be hidden from view
using the default mask.

**HTML equivalence**

.. code-block::

    <input type="password" />

Type: range
-----------


Type: select
------------

Type: table
-----------

Type: tel
---------

Type: text
----------

Type: textarea
--------------

Type: time
----------



.. toctree::

   checkbox
   content
   date
   email
   file
   hidden
   number
   password
   range
   select
   table
   tel
   text
   textarea
   time