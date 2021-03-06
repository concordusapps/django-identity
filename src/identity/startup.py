# -*- coding: utf-8 -*-
""" \file identity/startup.py
\brief Defines code that is executed once upon django server startup.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.contrib import admin
from django import template
from django.contrib.auth.models import User, Group


# Discover administration modules
admin.autodiscover()

# Remove auth models (as they are 'unused')
admin.site.unregister(User)
admin.site.unregister(Group)

# Project-wide template tags
template.add_to_builtins('django.templatetags.future')
template.add_to_builtins('django.contrib.staticfiles.templatetags.staticfiles')
