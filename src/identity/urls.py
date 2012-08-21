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
#from scim import api


# One-time startup code goes here:
from . import startup

# URL templates
component = '{}.{{}}.urls'.format(settings.PROJECT_NAME)

# URL configuration
urlpatterns = patterns('',
    # Administration
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Components
    #url(r'^accounts/', include('{}.account.urls'.format(settings.PROJECT_NAME))),
    url(r'^saml/', include(component.format('saml'))),
    #url(r'^scim/', include(api.v1_api.urls)),
)
