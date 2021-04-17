py-easyaddress
==============

*py-easyaddress by [easyaddress.io](https://easyaddress.io/)*


Installation
------------

.. code-block:: bash

    $ pip install easyaddress


Get an API Key
--------------




Usage
-----

.. code-block:: python

    >>> from easyaddress import API
    >>> api = easyaddress.API("<API_KEY>", "<API_SECRET>")
    >>> api.validate_email("example@example.org")


.. code-block:: bash

    $ export EASYADDRESS_API_KEY=<API_KEY>
    $ export EASYADDRESS_API_SECRET=<API_SECRET>

.. code-block:: python

    >>> from easyaddress import validate_email
    >>> validate_email("example@example.org")


.. code-block:: python

    >>> from easyaddress import API
    >>> api = easyaddress.API("<API_KEY>", "<API_SECRET>")
    >>> api.validate(Address(street_number='2630', street='Hegal Place', zipcode='23242', city='Alexandria', country=Country.US, province=USRegion.VA))


Running Tests
-------------

.. code-block:: bash

    $ python -m unittest discover


________________________________________________

Licence: MIT
© 2021 [easyaddress.io](https://easyaddress.io/)
