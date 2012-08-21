# -*- coding: utf-8 -*-
""" \file identity/saml/admin.py
\brief Registers the saml models for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.contrib.admin import site
from django.contrib.admin.options import ModelAdmin
from . import models


site.register(models.Profile)
site.register(models.Binding)

class ServiceAdmin(ModelAdmin):
    list_filter = ('resource', 'profile', 'binding',)
    list_display = ('resource', 'profile', 'binding',)
    list_display_links = ('profile',)
    list_editable = ('binding',)


site.register(models.Service, ServiceAdmin)
