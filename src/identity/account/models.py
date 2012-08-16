# -*- coding: utf-8 -*-
""" \file identity/account/models.py
\brief Provides the model definitions for the accounts module.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models
from django.contrib.auth.models import User
from identity.models import Entitlement, Role


class Profile(models.Model):
    """TODO
    """

    ## TODO
    user = models.OneToOneField(User, editable=False)

    ## TODO
    given_name = models.CharField(max_length=512, null=True, blank=True)

    ## TODO
    family_name = models.CharField(max_length=512, null=True, blank=True)

    ## Roles that the user is defined to have in services.
    roles = models.ManyToManyField(Role)

    ## Entitlements that the user is defined to have in services.
    entitlements = models.ManyToManyField(Entitlement)

    def __unicode__(self):
        """Returns a textual representation of this."""
        return unicode(self.user)
