# -*- coding: utf-8 -*-
""" \file identity/account/singals.py
\brief Implements the neccessary singals for the accounts module.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
