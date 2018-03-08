#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from rest_framework.viewsets import ModelViewSet
from .serializers import TaigaUserSerializer


class TaigaUserView(ModelViewSet):
    serializer_class = TaigaUserSerializer

    def create(self, request, *args, **kwargs):
        return super(TaigaUserView, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TaigaUserView, self).update(request, *args, **kwargs)
