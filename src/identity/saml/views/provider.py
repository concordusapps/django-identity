# -*- coding: utf-8 -*-
""" \file identity/saml/views/provider.py
\brief Implements the SAML endpoints for providers.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from .. import models


def sso(request, *args, **kwargs):
    """Single sign on (SSO)"""
    print(request.body)
    pass


def slo(request, *args, **kwargs):
    """Single log on (SLO)"""
    pass
