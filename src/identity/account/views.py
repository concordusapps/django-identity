# -*- coding: utf-8 -*-
""" \file identity/account/views.py
\brief Implements the account views for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.views.generic.edit import FormView
from . import forms
from django.core.urlresolvers import reverse
from urllib import urlencode


class Login(FormView):
    """TODO"""
    template_name = 'identity/account/login.html'
    form_class = forms.Login

    def form_valid(self, form):
        # Grab the provider slug using the identifier in the url
        identifier = self.request.GET['id']
        slug = self.request.session['{}:saml:provider'.format(identifier)]

        # Ensure the success_url is set appropriately
        self.success_url = '{}?{}'.format(reverse('sso', kwargs={
                'slug': slug
            }), urlencode({
                'id': self.request.GET['id'],
                '': self
            })
        )

        # Login
        form.login(self.request)

        # Return back up the chain
        return super(Login, self).form_valid(form)
