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
from scim import user
from tastypie import bundle
#from identity.account.models import Profile
from django.conf.urls.defaults import url


class Endpoint(Resource):
    """Generic endpoint for making a tastypie resource more scim-like
    """

    def base_urls(self):
        """Scim only responds to an endpoint with an optional user after it
        This is copied verbatem from tastypie's source code as of
        https://github.com/toastdriven/django-tastypie/blob/v0.9.11/tastypie/resources.py#L274
        """
        return [
            url(r"^(?P<resource_name>%s)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('dispatch_list'), name="api_dispatch_list"),
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]

    def alter_list_data_to_serialize(self, request, data):
        """Remove HATEOAS stuff and reformat list queries"""

        # format stuff in a scim compliant manner
        data['totalResults'] = data['meta']['total_count']

        # Note the arbitrary capitalization of Resources here.
        # Taken from http://www.simplecloud.info/specs/draft-scim-api-00.html#query-resources
        data['Resources'] = data['objects']

        # Remove default tastypie stuff
        del data['meta']
        del data['objects']

        return super(Endpoint, self).alter_list_data_to_serialize(request, data)


class User(Endpoint):
    """Endpoint for user objects
    """

    class Meta:
        object_class = Profile
        resource_name = 'Users'

        # Methods allowed for an individual user
        detail_allowed_methods = ['GET', 'PUT', 'PATCH', 'DELETE']

        # Methods allowed for a users endpoint
        list_allowed_methods = ['POST']

#    def get_object_list(self, request):
#        """TODO:
#        This function needs to return a list of scim objects representing all
#        the users
#        """
#        return super(User, self).get_object_list(request)
#
#    def obj_get_list(self, request=None, **kwargs):
#        """TODO:
#        This function is in charge of filtering the object list
#        """
#        return super(User, self).obj_get_list(request, **kwargs)
#
#    def obj_get(self, request=None, **kwargs):
#        """TODO:
#        This function returns the scim user object representing a single user
#        Raise NotFound() exception on 404
#        """
#        return super(User, self).obj_get(request, **kwargs)
#
#    def obj_create(self, bundle, request=None, **kwargs):
#        """TODO:
#        This function creates a scim object (and should also create a user)
#        based on the request
#        """
#        return super(User, self).obj_creat(request, **kwargs)
#
#    def obj_update(self, bundle, request=None, **kwargs):
#        """TODO:
#        This function updates a scim object in place.
#        Raise NotFound() exception on 404
#        """
#        return super(User, self).obj_update(request, **kwargs)
#
#    def obj_delete_list(self, request=None, **kwargs):
#        """TODO:
#        This function deletes a range of objects
#        """
#        return super(User, self).obj_delete_list(request, **kwargs)
#
#    def obj_delete(self, request=None, **kwargs):
#        """TODO:
#        This function deletes a single object
#        Raise NotFound() exception on 404
#        """
#        return super(User, self).obj_delete(request, **kwargs)
#
#    def rollback(self, bundles):
#        """TODO:
#        Delete the objects associated with list of bundles given
#        Will need to delete the User objects, or set them to inactive
#        """
#        return super(User, self).rollback(bundles)
