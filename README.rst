django-rf-candv-choices
=======================

|pypi_package| |pypi_downloads| |python_versions| |license|


Use `django-candv-choices`_ with `django-rest-framework`_.


**Table of contents**

.. contents::
    :local:
    :depth: 2
    :backlinks: none


Installation
------------

Install from `PyPI <https://pypi.python.org/pypi/django-rf-candv-choices>`_:

.. code-block:: bash

  $ pip install django-rf-candv-choices


Usage
-----

Serializing choices
~~~~~~~~~~~~~~~~~~~

For example, you have some model which uses
``candv_x.django.choices.ChoiceField`` to store one of allowed values. This
might be a ``User`` model, which has ``user_role`` field, where values for
``user_role`` are defined by ``USER_ROLES`` constants container.

Use ``candv_x.rest_framework.choices.ChoiceField`` for ``user_role``
serialization:

.. code-block:: python

  from rest_framework import serializers
  from candv_x.rest_framework.choices import ChoiceField

  from .constants import USER_ROLES
  from .models import User


  class UserSerializer(serializers.ModelSerializer):
      user_role = ChoiceField(USER_ROLES)

      class Meta:
          model = User
          fields = ('id', 'name', 'user_role', )



Exposing choices to the outer world
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to expose list of possible choices for your field, then you can
use a ``ChoicesList`` base view to get a class-based view:

.. code-block:: python

  from candv_x.rest_framework.choices import ChoicesList

  from .constants import USER_ROLES


  class UserRoleList(ChoicesList):
      choices = USER_ROLES

The only thing you need to do is to define ``choices`` attribute.

There is a faster way also: you can use a ``coalitions_list`` view factory to
get a function-based view:


.. code-block:: python

  from candv_x.rest_framework.choices import simple_choices_list

  from .constants import USER_ROLES


  user_role_list = simple_choices_list(USER_ROLES)


Changelog
---------

*You can click a version name to see a diff with the previous one.*

* `1.0.0`_ (Aug 1, 2015)

  Initial version


.. |pypi_package| image:: http://img.shields.io/pypi/v/django-rf-candv-choices.svg?style=flat
   :target: http://badge.fury.io/py/django-rf-candv-choices/
   :alt: Version of PyPI package

.. |pypi_downloads| image:: http://img.shields.io/pypi/dm/django-rf-candv-choices.svg?style=flat
   :target: https://crate.io/packages/django-rf-candv-choices/
   :alt: Number of downloads of PyPI package

.. |python_versions| image:: https://img.shields.io/badge/Python-2.7,3.4-brightgreen.svg?style=flat
   :alt: Supported versions of Python

.. |license| image:: https://img.shields.io/badge/license-LGPLv3-blue.svg?style=flat
   :target: https://github.com/oblalex/django-rf-candv-choices/blob/master/LICENSE
   :alt: Package license


.. _django-candv-choices: https://github.com/oblalex/django-candv-choices
.. _django-rest-framework: http://www.django-rest-framework.org

.. _1.0.0: https://github.com/oblalex/django-rf-candv-choices/releases/tag/v1.0.0
