========
Usage
========

To use django-shells, add ``'shells'`` in your ``INSTALLED_APPS``. This replaces the ``shell`` and ``dbshell`` management commands with a customised version.


The ``shell`` Command
======================

The new ``shell`` command adds two choices as your Python shell: ``ptpython`` and ``ptipython``. Both requires you to install Jonathan Slender's ptpython_, and the latter also requires IPython.

The interpreter is chosen automatically based on what your environment has. All command line options are identical to the built-in ``shell`` command, except that the ``--interface`` (and the ``-i`` shorthand) supports two additional values ``ptpython`` and ``ptipython``.


The ``dbshell`` Command
========================

Two additional database clients are added: ``pgcli`` for PostgreSQL, and ``mycli`` for MySQL. Both require you to install `a Python package with the same name <https://github.com/dbcli>`_.

The client is chosen automatically based on your database settings, and what your environment provides. You can also use the ``--plain`` and ``--interface`` (shorthanded ``-i``) options to specify one explicitly.


.. _ptpython: https://github.com/jonathanslenders/ptpython/
