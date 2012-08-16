# -*- coding: utf-8 -*-
""" \file identity/models.py
\brief Implements the core models for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models


class Timestamp(models.Model):
    """Identifies when an inherited model has been created and last updated.
    """

    class Meta:
        abstract = True

    ## Date and time the model was created.
    created = models.DateTimeField(auto_now_add=True, editable=False)

    ## Date and time the model was last updated.
    updated = models.DateTimeField(auto_now=True, editable=False)


class Provider(Timestamp):
    """
    """
    pass
