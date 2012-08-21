# -*- coding: utf-8 -*-
""" \file identity/account/models.py
\brief Implements the account models for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db import models
from ..models import Consumer

class People(models.Model):
    uid = models.CharField(256)
    given_name = models.CharField(32768)
    surname = models.CharField(32768)
    middle_name = models.CharField(32768)
    common_name = models.CharField(32768)
    display_name = models.CharField(32768)
    salutation = models.CharField(32768)
    generational_qualifier = models.CharField(32768)
    title = models.CharField(32768)
    preferred_language = models.CharField(128)
    time_zone = models.CharField(32768)
    is_active = models.BooleanField()
    is_away = models.BooleanField()
    password = models.CharField(128)
    
class PeopleEmail(models.model):
    people = models.ForeignKey(People)
    email = models.CharField(32768)
    
class PeoplePhone(models.model):
    people = models.ForeignKey(People)
    phone = models.CharField(32768)
    
class PeopleInstantMessage(models.model):
    people = models.ForeignKey(People)
    instant_message = models.CharField(32768)
    
class PeoplePhoto(models.model):
    people = models.ForeignKey(People)
    photo = models.ImageField()
    
class PeopleSocialNetwork(models.model):
    people = models.ForeignKey(People)
    social_network = models.CharField(32768)
    
class PeopleManager(models.Model):
    people = models.ForeignKey(People)
    manager = models.ForeignKey(People)
    
class PeopleOrganization(models.Model):
    people = models.ForeignKey(People)
    organization = models.ForeignKey(Organization)
    
class Client(models.model):
    client_name = models.CharField(32768)
    display_name = models.CharField(32768)
    time_zone = models.CharField(32768)
    is_active = models.BooleanField()
    
class ClientPhone(models.model):
    people = models.ForeignKey(People)
    phone = models.CharField(32768)
    
class ClientEmail(models.model):
    people = models.ForeignKey(People)
    email = models.CharField(32768)
    
class ClientSocialNetwork(models.model):
    people = models.ForeignKey(People)
    social_network = models.CharField(32768)
    
class ClientPhoto(models.model):
    people = models.ForeignKey(People)
    photo = models.ImageField()
    
class ClientOwner(models.Model):
    client = models.ForeignKey(Client)
    owner = models.ForeignKey(People)

class Location(models.model):
    location_name = models.CharField(32768)
    address = models.CharField(32768)
    city = models.CharField(32768)
    state = models.CharField(32768)
    Country = models.CharField(32768)
    zip_code = models.CharField()
    area_number = models.CharField(32768)
    
class OrganizationalUnit(models.model):
    organizational_unit_name = models.CharField(32768)
    description = models.CharField(32768)

class OrganizationalUnitAdministrator(models.model):
    organizational_unit = models.ForeignKey(OrganizationalUnit)
    administrator = models.ForeignKey(People)

class Application(models.model):
    application_name = models.CharField(32768)
    subscription_id = models.CharField(32768)
    
class Group(models.model):
    group_name = models.CharField(32768)
    description = models.CharField(32768)
    
class GroupMember(models.model):
    group = models.ForeignKey(Group)
    member = models.ForeignKey(People)