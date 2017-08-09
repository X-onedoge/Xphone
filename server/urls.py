#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Author:Xonedoge

from django.conf.urls import include, url
from django.contrib import admin

from server.views import *

urlpatterns = [
    url(r'^server/$', server,name='server'),
]