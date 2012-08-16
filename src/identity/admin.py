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


site.register(models.Service)
site.register(models.Provider)
