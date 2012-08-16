# -*- coding: utf-8 -*-
""" \file identity/admin.py
\brief Registers the core models for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.contrib.admin import site
from . import models
from django.contrib.admin.options import ModelAdmin


site.register(models.Service)
site.register(models.Provider)


class RoleEntitlementAdmin(ModelAdmin):
    list_filter = ('service',)
    list_display = ('service', 'value', 'description',)
    list_editable = ('value',)
    list_display_links = ('description',)


site.register(models.Entitlement, RoleEntitlementAdmin)
site.register(models.Role, RoleEntitlementAdmin)
