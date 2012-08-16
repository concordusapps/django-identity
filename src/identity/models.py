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


class InheritanceAware(models.Model):
    """Enables a model to be aware of its inheritance tree.
    """

    class Meta:
        abstract = True

    ## The actual type of the model.
    type = models.ForeignKey(ContentType, editable=False)

    def cast(self):
        """Returns this entity casted to its actual type."""
        return self.type.get_object_for_this_type(pk=self.pk)

    def save(self, *args, **kwargs):
        """Ensures the stored type reflects the actual type of this entity."""
        # Force the stored type to its defined content type
        self.type = ContentType.objects.get_for_model(type(self))

        # Save the subclass
        super(InheritanceAware, self).save(*args, **kwargs)


class Timestamp(models.Model):
    """Identifies when an inherited model has been created and last updated.
    """

    class Meta:
        abstract = True

    ## Date and time the model was created.
    created = models.DateTimeField(auto_now_add=True, editable=False)

    ## Date and time the model was last updated.
    updated = models.DateTimeField(auto_now=True, editable=False)


class Resource(InheritanceAware, Timestamp):
    """An identified resource in the identity system."""

class Provider(Resource):
    """
    A resource capable of authentication, authorization, and provisioning
    using SAML, SCIM, and XACML (forthcoming).
    """
    pass
