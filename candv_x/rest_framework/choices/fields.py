# -*- coding: utf-8 -*-

from candv.base import Constant, ConstantsContainer
from django.utils.translation import ugettext_lazy as _
from rest_framework.fields import Field


class ChoiceField(Field):
    default_error_messages = {
        'invalid_choice': _("'{input}' is not a valid choice."),
        'missing_constant_name': _("Constant name is missing."),
    }

    def __init__(self, choices, **kwargs):
        assert issubclass(choices, ConstantsContainer)
        assert issubclass(choices.constant_class, Constant)

        self.choices = choices
        super(ChoiceField, self).__init__(**kwargs)

    def to_internal_value(self, data):
        try:
            return self.choices[data]
        except KeyError:
            self.fail('invalid_choice', input=data)

    def to_representation(self, value):
        return value.name
