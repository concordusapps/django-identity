# -*- coding: utf-8 -*-
""" \file identity/account/urls.py
\brief Defines the urls for the account component of django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.conf.urls import patterns, url
from django.conf import settings
from . import views

# URL configuration
urlpatterns = patterns('',
    url('^login', views.Login.as_view(), name='login'),
    #url('^logout$', views.Logout.as_view(), name='logout'),
)
