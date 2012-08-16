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
from identity.common.views import Protected
from django.conf import settings
from django.views.generic.edit import FormView, UpdateView
from . import forms
import ldap


class Profile(Protected, UpdateView):
    """TODO"""
    template_name = 'identity/account/profile.html'
    form_class = forms.Profile
    success_url = '/accounts/profile'  # FIXME: Make this dynamic

    def get_object(self):
        """TODO"""
        return self.request.user.get_profile()

    def form_valid(self, form):
        """TODO"""
        # Save the user model
        response = super(Profile, self).form_valid(form)

        # Hook in here to save to LDAP
        # FIXME: This can be abstracted
        # Construct the DN
        dn = "uid={},ou=people,{}".format(
            self.request.session['user'],
            settings.LDAP['DN']
        )

        # Initialize the LDAP connection
        connection = ldap.open(settings.LDAP['HOST'])
        connection.protocol_version = getattr(
            ldap, 'VERSION{}'.format(settings.LDAP['VERSION']))

        try:
            # Attempt to authenticate with the given credentials
            connection.simple_bind_s(dn, self.request.session['pass'])

            # Update LDAP attributes
            data = form.cleaned_data
            connection.modify_s(dn, [
                (ldap.MOD_REPLACE, 'givenName', [str(data['given_name'])]),
                (ldap.MOD_REPLACE, 'sn', [str(data['family_name'])]),
            ])

        except:
            # Something went wrong; we have no auth
            #
            raise

        finally:
            # Ensure we close our connection
            connection.unbind_s()

        # Return the response
        return response


def login(request, *args, **kwargs):
    """TODO"""
    if request.method == 'POST':
        # Store the username and password for later re-auth using LDAP
        request.session['user'] = request.POST['username']
        request.session['pass'] = request.POST['password']

    return views.login(request, *args, **kwargs)
