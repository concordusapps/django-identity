# -*- coding: utf-8 -*-
""" \file identity/saml/models.py
\brief Implements the saml models for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models
from ..models import Provider
from ..common.models import Timestamp


class Binding(Timestamp):
    """
    Represents a binding a provider may use to connect to another providers'
    service.
    """

    ## Name of the binding.
    name = models.CharField(max_length=10, unique=True)

    def __unicode__(self):
        """Returns a representation of this instance as a string."""
        return self.name


class Profile(models.Model):
    """
    Represents the profile the service is fulfilling for a provider.

    Available profiles include:
        - Assertion consumer service [ACS]
        - Single Logout service [SLS]
        - Single sign on [SSO]
        - Single log out [SLO]
        - Artifact resolution service [ARS]
        - Name identifier management service [MNI]
        - Name identifier mapping service [NIM]
        - Assertion query / request [AQR]
    """

    ## Symbolic name of the profile for use in queries.
    slug = models.CharField(max_length=3, unique=True)

    ## Friendly name of the profile.
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        """Returns a representation of this instance as a string."""
        return '{} [{}]'.format(self.name, self.slug)


class Service(Timestamp):
    """Represents a SAML service (ex. sso, acs, slo, etc).
    """

    ## The provider for whom the service is for.
    provider = models.ForeignKey(Provider)

    ## Path on the provider as to where the service resides.
    path = models.CharField(max_length=1024)

    ## Bindings this service will respond to.
    binding = models.ForeignKey(Binding)

    ## Profile the service is fulfilling
    profile = models.ForeignKey(Profile)

    def __unicode__(self):
        """Returns a representation of this instance as a string."""
        return '{}: {} <{}>'.format(
            self.provider,
            self.profile,
            self.binding
        )

