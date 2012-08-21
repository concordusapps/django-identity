# -*- coding: utf-8 -*-
""" \file identity/account/forms.py
\brief Implements the account forms for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django import forms
from django.contrib import auth
from django.core.exceptions import ValidationError


class Login(forms.Form):
    """TODO"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        """TODO"""
        # Attempt to authenticate
        u = auth.authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        # Raise validation error if failed
        if u is None:
            raise ValidationError(
                'Access denied; username or password is incorrect.')

        # Return 'cleaned' data
        return super(Login, self).clean()

    def login(self, request):
        """TODO"""
        # Grab the user object again
        u = auth.authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        # Log the user into the system
        auth.login(request, u)
