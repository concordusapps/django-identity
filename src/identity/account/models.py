# -*- coding: utf-8 -*-
""" \file identity/account/models.py
\brief Implements the account models for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models
from ..common.models import Timestamp
from ..models import Consumer


class Role(Timestamp):
    """TODO"""

    ## The service of which the role is defined in.
    service = models.ForeignKey(Consumer)

    ## TODO
    description = models.CharField(max_length=1024)

    ## TODO
    value = models.CharField(max_length=128)

    def __unicode__(self):
        """Returns a textual representation of this."""
        return '{}: {}'.format(self.service.slug, self.description)


class Entitlement(Timestamp):
    """TODO"""

    ## The service of which the entitlement is defined in.
    service = models.ForeignKey(Consumer)

    ## TODO
    description = models.CharField(max_length=1024)

    ## TODO
    value = models.CharField(max_length=128)

    def __unicode__(self):
        """Returns a textual representation of this."""
        return '{}: {}'.format(self.service.slug, self.description)
