# -*- coding: utf-8 -*-
""" \file identity/models.py
\brief Implements the core models for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models
from django.contrib.contenttypes.models import ContentType
from .common.models import InheritanceAware, Timestamp, Host


class Resource(InheritanceAware, Timestamp):
    """An identified resource in the identity system."""

    ## The shorthand name used to access the resource.
    slug = models.CharField(max_length=64)

    ## The descriptive name of the resource.
    name = models.CharField(max_length=1024)

    ## Identiifes the host on which the resource resides.
    host = models.ForeignKey(Host)

class Provider(Resource):
    """
    A resource capable of authentication, authorization, and provisioning
    using SAML, SCIM, and XACML (forthcoming).
    """

class Service(Resource):
    """A resource capable of a service; or, represented as a product.
    """
