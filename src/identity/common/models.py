# -*- coding: utf-8 -*-
""" \file identity/common/models.py
\brief Implements the common models for django-identity.

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


class Protocol(Timestamp):
    """Identifies the transport protocol used to access the host."""

    ## Identifies both the name of the protocol and the scheme used to access
    ## it (ex. http, ssh, ftp, etc).
    name = models.CharField(max_length=255)

    ## Identifies the default port for this protocol.
    port = models.IntegerField()

    def __unicode__(self):
        """Returns a textual representation of this."""
        return self.name


class Host(Timestamp):
    """Identifies a host resident at a server listening at a port.
    """

    ## The transport protocol used to access the host.
    protocol = models.ForeignKey(Protocol)

    ## The domain name of the server.
    server = models.CharField(max_length=255, blank=True)

    ## The port that the host is listening on.
    port = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        """Returns a textual representation of this."""
        return self.get_absolute_url()

    def get_absolute_url(self):
        """Returns a useable URL from this."""
        port = ''
        if not (self.port or self.protocol.port) == self.protocol.port:
            port = ':{}'.format(self.port)

        return '{}://{}{}'.format(
            self.protocol,
            self.server or 'localhost',
            port)
