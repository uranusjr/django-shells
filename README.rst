=============================
django-shells
=============================

Better shells for your `manage.py`.

Documentation
-------------

The full documentation is at https://django-shells.readthedocs.org.

Quickstart
----------

Install django-shells::

    pip install django-shells

Then add ``'shells'`` to your ``INSTALLED_APPS``.

Features
--------

`django-shells` overrides two built-in Django management commands: `shell` and `dbshell`.

Two extra shell options are added to `shell`:

* `ptpython`
* `ptipython`

The former is picked up automatically if you have ptpython intsalled. The latter is picked up if you have both ptpython and IPython installed.

Two extra database client options are added to `dbshell`:

* `pgcli` for PostgreSQL.
* `mycli` for MySQL.

Both are picked up automatically when you have the Python package of the same name installed.

You can also specify a client manually via the ``--interface`` (shorthanded ``-i``) option, similar to the built-in option of the same name provided by the `shell` command.


Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/pydanny/cookiecutter-djangopackage
