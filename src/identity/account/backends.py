# -*- coding: utf-8 -*-
""" \file identity/account/backends.py
\brief Authenticate users against LDAP.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.models import User
import ldap
from django.conf import settings
import hashlib
from . import models

class LDAPBackend(RemoteUserBackend):
    """TODO"""

    ## TODO
    create_unknown_user = False

    ## TODO
    base_dn = 'ou=people,dc=concordusapps,dc=com'

    def populate_profile(self, user, attributes):
        """
        Populate the user profile according to information stored in their
        LDAP attributes.
        """
        # Construct the profile object if needed
        profile = models.Profile.objects.get_or_create(user=user)[0]

        if 'givenName' in attributes:
            # Grab first gn to use as the primary givenName
            profile.given_name = attributes['givenName'][0]

            # TODO: Additional gn's go to nickName

        # Simple attributes
        if 'sn' in attributes:
            profile.family_name = attributes['sn'][0]

        # Save the profile
        profile.save()

    def clean_username(self, username):
        """
        Performs any cleaning on the username (e.g. stripping LDAP DN
        information) prior to using it to get or create a User object.
        """
        raise Exception

    def configure_user(self, user):
        """
        Configures a newly created user. This method is called immediately
        after a new user is created, and can be used to perform custom setup
        actions, such as setting the user's groups based on attributes in an
        LDAP directory.
        """
        raise Exception

#    def get_user(self, user_id):
#        """Retreives a user object from the passed identifier.
#        """
#
#        # user = somehow_create_an_instance_of (MyUser, user_id)
#        # return user

    def authenticate(self, **credentials):
        """
        Attempts to authenticate the user by searching and verifying
        creditionals against LDAP.
        """
        # Construct the DN
        dn = "uid={},{}".format(credentials['username'], LDAPBackend.base_dn)

        # Initialize the LDAP connection
        connection = ldap.open('spock')
        connection.protocol_version = ldap.VERSION3

        try:
            # Attempt to authenticate with the given credentials
            connection.simple_bind_s(dn, credentials['password'])

            # We now have an authenticated LDAP connection; let's play
            try:
                # Hash the DN and get the first 30 characters
                hash = hashlib.sha256(dn).hexdigest()[:30]

                # Has this LDAP user been locally cached ?
                user, new = User.objects.get_or_create(username=hash)
                if new:
                    # Initialize user
                    user.set_unusable_password()

                    # FIXME: REMOVE this and actually check for permissions
                    user.is_staff = True
                    user.is_superuser = True

                    # Save the user to the DB
                    user.save()

                # Get attributes
                attributes = connection.search_s(
                    dn,
                    ldap.SCOPE_SUBTREE,
                    '(objectclass=*)',
                    None
                )

                # Populate profile
                self.populate_profile(user, attributes[0][1])

                #self.populate_profile(user.get_profile(), connection)

                # Yeah; off we go
                return user

            except User.DoesNotExist:
                # Nope; die
                print("Does not exist.")
                return None

        except BaseException as x:
            # Something went wrong; we have no auth
            print(x)
            print("Not authenticated.")
            return None

        finally:
            # Ensure we close our connection
            connection.unbind_s()
