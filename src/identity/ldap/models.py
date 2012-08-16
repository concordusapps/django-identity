# -*- coding: utf-8 -*-
""" \file identity/db/models.py
\brief Implements the models neccessary to abstract user data stores.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models
from identity.common.models import InheritanceAware, Timestamp
from identity.models import Provider

class Store(Timestamp, InheritanceAware):
    """Represents a generic data store.
    """

    ## The provider that this data store is behind.
    provider = models.ForeignKey(Provider)
