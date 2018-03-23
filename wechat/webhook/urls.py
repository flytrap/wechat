#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from django.conf.urls import url
from .views import WebHookView

urlpatterns = [
    url('^$', WebHookView.as_view({'post': 'create'}), ),
    url('^notify', WebHookView.as_view({'get': 'list'}), ),
]
