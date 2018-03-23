#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from django_filters.filterset import FilterSet
from .models import Notification


class NotificationFilter(FilterSet):
    class Meta:
        model = Notification
        fields = {
            'project_id': ['in', 'exact'],
            'type': ['exact'],
        }
