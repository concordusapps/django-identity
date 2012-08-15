# -*- coding: utf-8 -*-
""" \file identity/account/views.py
\brief Provides the views definitions for the accounts module.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import views
from identity.views import Protected
from django.views.generic.edit import FormView
from . import forms


class Profile(Protected, FormView):
    """TODO"""
    template_name = 'identity/account/profile.html'
    form_class = forms.Profile


def login(request, *args, **kwargs):
    """TODO"""
    if request.method == 'POST':
        # Store the username and password for later re-auth using LDAP
        request.session['user'] = request.POST['username']
        request.session['pass'] = request.POST['password']

    return views.login(request, *args, **kwargs)
