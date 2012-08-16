# -*- coding: utf-8 -*-
""" \file identity/db/ldap/models.py
\brief Implements the models neccessary to map to LDAP.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models
from identity.common.models import Host
from identity.db.models import Store


class Directory(Store):
    """Represents a LDAP directory.
    """

    class Meta:
        verbose_name_plural = 'directories'

    ## The host on which the LDAP directory resides.
    host = models.ForeignKey(
        Host,
        help_text="The host on which the LDAP directory resides.")

    ## The base distinguished name.
    base_dn = models.CharField(
        verbose_name="base distinguished name",
        max_length=1024,
        blank=True,
        help_text="""
            The base distinguished name that is prepended to every query
            against LDAP.
        """,
    )

    def __unicode__(self):
        """Returns a textual representation of this."""
        return unicode(self.host)
