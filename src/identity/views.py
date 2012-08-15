# -*- coding: utf-8 -*-
""" \file identity/views.py
\brief Implements the core views for django-identity.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Protected(object):
    """TODO
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """TODO"""
        return super(Protected, self).dispatch(*args, **kwargs)
