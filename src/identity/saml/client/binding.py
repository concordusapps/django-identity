# -*- coding: utf-8 -*-
""" \file identity/saml/client/binding.py
\brief Implements the SAML standard for bindings.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
import abc
import base64
import zlib


class Binding(object):
    """TODO"""
    @classmethod
    def receive(cls, request, kind):
        name = 'SAML{}'.format(kind.title())
        if name in request.GET:
            return Redirect.decode(request.GET[name])
        else:
            raise ValueError("Couldn't detect binding.")

    @abc.abstractmethod
    @staticmethod
    def decode(message):
        """TODO"""
        pass

    @abc.abstractmethod
    @staticmethod
    def encode(message):
        """TODO"""
        pass


class Redirect(Binding):
    """TODO"""
    @staticmethod
    def decode(message):
        """TODO"""
        return zlib.decompress(base64.b64decode(message), -15)

    @staticmethod
    def encode(message):
        """TODO"""
        return base64.b64encode(zlib.compress(message)[2:-4])