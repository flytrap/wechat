#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from django.conf.urls import url
from .views import TaigaUserView

urlpatterns = [
    url('^user', TaigaUserView.as_view({'post': 'create'}), ),
    url('^logout', TaigaUserView.as_view({'put': 'update'}), ),
]
