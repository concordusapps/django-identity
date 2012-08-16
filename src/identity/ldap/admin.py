# -*- coding: utf-8 -*-
""" \file identity/ldap/admin.py
\brief Registers the LDAP data store models.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.contrib.admin import site
from . import models
from django.contrib.admin.options import ModelAdmin


site.register(models.Directory)


class ObjectAdmin(ModelAdmin):
    list_display = ('directory', 'parent', 'description',)
    list_display_links = ('description',)
    list_filter = ('directory', 'parent')


site.register(models.Object, ObjectAdmin)
