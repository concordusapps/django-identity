# -*- coding: utf-8 -*-
""" \file identity/scim/views.py
\brief Defines views for scim to provide interfaces for

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright © 2012 Concordus Applications, Inc.
           \n \n
           Permission is hereby granted, free of charge, to any person
           obtaining a copy of this software and associated documentation
           files (the "Software"), to deal in the Software without restriction,
           including without limitation the rights to use, copy, modify, merge,
           publish, distribute, sublicense, and/or sell copies of the Software,
           and to permit persons to whom the Software is furnished to do so,
           subject to the following conditions:
           \n \n
           The above copyright notice and this permission notice shall be
           included in all copies or substantial portions of the Software.
           \n \n
           THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
           EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
           MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
           NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
           BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
           ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
           CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
           SOFTWARE.
"""
from tastypie.resources import Resource
from tastypie.bundle import Bundle
from tastypie.utils import trailing_slash
from django.conf.urls.defaults import url


class Endpoint(Resource):
    """Generic endpoint for making a tastypie resource more scim-like
    This is copied verbatem from tastypie's source code as of
    https://github.com/toastdriven/django-tastypie/blob/5397dec04fe83092a56ba14a843731f2aa08184d/tastypie/resources.py#L288
    """

    def base_urls(self):
        """Scim only responds to an endpoint with an optional user after it
        """
        return [url(r"^(?P<resource_name>%s)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('dispatch_list'), name="api_dispatch_list"),]


class User(Endpoint):
    """Endpoint for user objects
    """

    #def get