# -*- coding: utf-8 -*-
""" \file identity/account/models.py
\brief Implements the account models for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models


class Contact(models.Model):
    """Represents a contactable entity.
    """

    class Meta:
        abstract = True

    ## The person's chosen display name.
    display_name = models.CharField(max_length=32768, blank=True, null=True)

    ## Email address for the contact.
    email = ListField(models.EmailField())

    ## Phone numbers for the contact.
    phone = ListField(models.CharField(
        max_length=32768, null=True, blank=True))

    ## Instant messaging services for the contact.
    ims = ListField(models.CharField(max_length=32768, null=True, blank=True))

    ## Photos for the contact.
    photo = ListField(models.ImageField(null=True, blank=True))

    ## Social networks for the contact.
    social = ListField(models.CharField(
        max_length=32768, null=True, blank=True))

    ## The time zone to display times in (ex. America/Los_Angeles).
    time_zone = models.CharField(max_length=32768, null=True, blank=True)

    ## Whether this person has an active account.
    is_active = models.BooleanField(null=True, blank=True)


class People(Contact):
    """Represents a person (user) that is able to authenticate with the system.
    """

    ## User identifier.
    uid = models.CharField(max_length=256, primary_key=True)

    ## First name of the person.
    first_name = ListField(models.CharField(max_length=32768))

    ## Last name of the person.
    last_name = models.CharField(max_length=32768)

    ## Middle name of the person.
    middle_name = models.CharField(max_length=32768, blank=True, null=True)

    ## Full name of the person.
    common_name = models.CharField(max_length=32768, blank=True, null=True)

    ## The person's prefix to their name.
    prefix = models.CharField(max_length=32768, blank=True, null=True)

    ## The person's suffix to their name.
    suffix = models.CharField(max_length=32768, blank=True, null=True)

    ## Title of the person.
    title = models.CharField(max_length=32768, blank=True, null=True)

    ## The perferred language of the person (ex. en-us).
    preferred_language = models.CharField(max_length=128)

    ## Whether this person is away on extended leave (for data flow).
    is_away = models.BooleanField()

    ## Managers of the person.
    manager = ListField(models.ForeignKey('self', null=True, blank=True))

    ## Clients the person is part of.
    organization = ListField(models.ForeignKey(
        'Client', null=True, blank=True))

    ## The person's hashed password.
    password = models.CharField(max_length=128)


class Client(Contact):
    """Represents a client (organization) registered with identity.
    """

    ## Name of the client.
    name = models.CharField(max_length=32768, primary_key=True)

    ## Owners of the client.
    owner = ListField(models.ForeignKey(People))


class Location(models.Model):
    location_name = models.CharField(32768)
    address = models.CharField(32768)
    city = models.CharField(32768)
    state = models.CharField(32768)
    Country = models.CharField(32768)
    zip_code = models.CharField()
    area_number = models.CharField(32768)


class OrganizationalUnit(models.Model):
    organizational_unit_name = models.CharField(32768)
    description = models.CharField(32768)


class OrganizationalUnitAdministrator(models.Model):
    organizational_unit = models.ForeignKey(OrganizationalUnit)
    administrator = models.ForeignKey(People)


class Application(models.Model):
    application_name = models.CharField(32768)
    subscription_id = models.CharField(32768)


class Group(models.Model):
    group_name = models.CharField(32768)
    description = models.CharField(32768)


class GroupMember(models.Model):
    group = models.ForeignKey(Group)
    member = models.ForeignKey(People)
