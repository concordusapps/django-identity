# -*- coding: utf-8 -*-
""" \file identity/urls.py
\brief Defines the root URL configuration.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from scim import api


# One-time startup code goes here:
from . import startup


# URL configuration
urlpatterns = patterns('',
    # Administration
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Accounts
    url(r'^accounts/', include('identity.account.urls')),

    # SCIM endpoint
    url(r'^scim/', include(api.v1_api.urls)),
)
