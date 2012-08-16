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
    """
    Backend for the django-identity server to authenticate users against
    LDAP locally.
    """

    ## TODO
    create_unknown_user = False

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

    def authenticate(self, **credentials):
        """
        Attempts to authenticate the user by searching and verifying
        creditionals against LDAP.
        """
        # Construct the DN
        dn = "uid={},ou=people,{}".format(
            credentials['username'],
            settings.LDAP['DN']
        )

        # Initialize the LDAP connection
        connection = ldap.open(settings.LDAP['HOST'])
        connection.protocol_version = getattr(
            ldap, 'VERSION{}'.format(settings.LDAP['VERSION']))

        try:
            # Attempt to authenticate with the given credentials
            connection.simple_bind_s(dn, credentials['password'])

            # Hash the DN and get the first 30 characters to store as their
            # django username
            username = hashlib.sha256(dn).hexdigest()[:30]

            # Has this LDAP user been locally cached ?
            user, new = User.objects.get_or_create(username=username)
            if new:
                # No; initialize user
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

            # Yeah; off we go
            return user

        except:
            # Something went wrong; we have no auth
            return None

        finally:
            # Ensure we close our connection
            connection.unbind_s()


class IdentityBackend(RemoteUserBackend):
    """
    Authentication backend for django-identity clients so they can authenticate
    remotely against a django-identity server (or some other SAML and SCIM
    compliant IDM).
    """
