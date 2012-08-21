# -*- coding: utf-8 -*-
""" \file identity/saml/urls.py
\brief Defines the urls for the saml component of django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.conf.urls import patterns, url


# URL configuration
urlpatterns = patterns('',
    # Metadata
    #url(r'^providers/(?P<slug>[^/]*?)$', name='metadata'),
    #url(r'^resources/(?P<slug>[^/]*?)$', name='metadata'),

    # Services
    url(r'^providers/(?P<slug>[^/]*?)$', name='sso'),
    #url(r'^resources/(?P<slug>[^/]*?)$', name='slo'),
    #url(r'^resources/(?P<slug>[^/]*?)$', name='slo'),
    #url(r'^resources/(?P<slug>[^/]*?)$', name='acs'),
)
