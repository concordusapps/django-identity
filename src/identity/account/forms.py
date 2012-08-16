# -*- coding: utf-8 -*-
""" \file identity/account/forms.py
\brief Provides the form definitions for the accounts module.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from . import models
from django.forms.models import ModelForm


class Profile(ModelForm):
    """TODO"""

    class Meta:
        model = models.Profile
