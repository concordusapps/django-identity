# -*- coding: utf-8 -*-
""" \file identity/account/admin.py
\brief Registers the model definitions of the accounts module.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.contrib.admin import site
from . import models


site.register(models.Profile)
