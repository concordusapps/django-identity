# -*- coding: utf-8 -*-
""" \file identity/wsgi.py
\brief WSGI configuration file.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 Concordus Applications, Inc.
           All Rights Reserved.
"""
import os
from django.core.wsgi import get_wsgi_application
from .settings import PROJECT_NAME

# FIXME: This and manage.py are the SAME... figure something out where they
#        aren't

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{}.settings".format(PROJECT_NAME))

application = get_wsgi_application()
