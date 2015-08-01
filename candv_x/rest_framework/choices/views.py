# -*- coding: utf-8 -*-

import abc

from django.utils import six
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class ChoicesList(six.with_metaclass(abc.ABCMeta, APIView)):

    @abc.abstractproperty
    def choices(self):
        pass

    def get(self, request, format=None):
        return Response(self.choices.to_primitive())


def simple_choices_list(choices):

    @api_view(['GET', ])
    def view(request, format=None):
        return Response(choices.to_primitive())

    return view
