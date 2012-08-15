# -*- coding: utf-8 -*-
""" \file identity/account/urls.py
\brief Defines the account URL configuration.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.conf.urls import patterns, url
from django.contrib.auth.views import (
    login,
    logout,
    password_change,
    password_change_done,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete)


# URL configuration
urlpatterns = patterns('',
    url(r'^login',
        login,
        name='login'
    ),

    url(r'^logout$',
        logout,
        name='logout'
    ),

    url(r'^password/change$',
        password_change
    ),

    url(r'^password/change/done$',
        password_change_done
    ),

    url(r'^password/reset$',
        password_reset
    ),

    url(r'^password/reset/done$',
        password_reset_done
    ),

    url(r'^password/reset/complete$',
        password_reset_complete
    ),

    url(r'^password/reset/confirm/(?P<uidb36>.+)/(?P<token>[\d\w-]+)$',
        password_reset_confirm
    ),
)
