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
from django.shortcuts import redirect
from urllib import urlencode


class Binding(object):
    """TODO"""
    @classmethod
    def receive(cls, request, kind):
        name = 'SAML{}'.format(kind.title())
        if name in request.GET:
            message = Redirect.decode(request.GET[name])
            return message, request.GET.get('RelayState')
        else:
            raise ValueError("Couldn't detect binding.")

    @classmethod
    @abc.abstractmethod
    def send(cls, message, state, kind):
        """TODO"""
        pass

    @staticmethod
    @abc.abstractmethod
    def decode(message):
        """TODO"""
        pass

    @staticmethod
    @abc.abstractmethod
    def encode(message):
        """TODO"""
        pass


class Redirect(Binding):
    """TODO"""
    @classmethod
    def send(cls, destination, message, state, kind):
        """TODO"""
        params = {'SAML{}'.format(kind.title()): cls.encode(message)}
        if state is not None:
            params['RelayState'] = state

        return redirect('{}?{}'.format(destination, urlencode(params)))

    @staticmethod
    def decode(message):
        """TODO"""
        return zlib.decompress(base64.b64decode(message), -15)

    @staticmethod
    def encode(message):
        """TODO"""
        return base64.b64encode(zlib.compress(message)[2:-4])
