# -*- coding: utf-8 -*-
""" \file identity/saml/views/provider.py
\brief Implements the SAML endpoints for providers.

\author Erich Healy (cactuscommander) ErichRHealy@gmail.com
\author Ryan Leckey (mehcode) leckey.ryan@gmail.com

\copyright Copyright 2012 © Concordus Applications, Inc.
           All Rights Reserved.
"""
from .. import models
from ...models import Provider, Consumer
from ..client.binding import Binding

from lxml import etree

import saml.schema.saml
import saml.schema.samlp
from saml import schema

from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from uuid import uuid4
from urllib import urlencode
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta


def sso(request, *args, **kwargs):
    """Single sign on (SSO)."""
    # Get ACS profile instance
    acs = models.Profile.objects.get(slug='acs')

    # Verify that the provider described in the URL exists
    provider = get_object_or_404(Provider, slug=kwargs['slug'])

    # Different paths if the user is already authenticated
    if not request.user.is_authenticated():
        # Generate request identifier to namespace variables stored in session
        # storage
        identifier = uuid4().hex
    else:
        # Grab the identifier from the GET paramter passed back from the login
        # form
        identifier = request.GET['id']

    storage = '{}:saml:{{}}'.format(identifier)


    # Different paths if the user is already authenticated
    if not request.user.is_authenticated():
        # Decode and deserialize the message
        message, state = Binding.receive(request, 'request')
        xml = etree.XML(message)
        obj = schema.samlp.AuthenticationRequest.deserialize(xml)

        # Verify that the issuing consumer is known to identity
        consumer = get_object_or_404(Consumer, name=obj.issuer.text)
    elif:
        # Get the consumer from the identifier

    # Query for a list of services provided by the requester that we know
    # about; if we cannot find one for ACS, then return a 404
    # TODO: Handle the case of more than one acs
    # NOTE: This is a redundant query; it is merely a sanity check so that
    #       if the service doesn't exist the user won't get any farther
    #       in the authn process.
    service = get_object_or_404(
        models.Service,
        resource=consumer,
        profile=acs
    )

    # TODO: Perform validation of message

    # Different paths if the user is already authenticated
    if not request.user.is_authenticated():
        # Store things in session storage TEMPORARILY to transfer to the login
        # view; which, in turn, promptly deletes them.
        request.session[storage.format('provider')] = provider.slug
        request.session[storage.format('consumer')] = consumer.slug
        request.session[storage.format('message:id')] = obj.id
        request.session[storage.format('state')] = state

        # Send user off to get authenticated
        # Redirect to login page
        return redirect('{}?{}'.format(
            reverse('login'),
            urlencode({'id': identifier})
        ))
    else:
        # Query for the consumer
        consumer = get_object_or_404(
            Consumer,
            slug=request.session[storage.format('consumer')]
        )

        # Query for the provider
        provider = get_object_or_404(
            Provider,
            slug=request.session[storage.format('provider')]
        )

        # Query for a list of services provided by the requester that we know
        # about; if we cannot find one for ACS, then return a 404
        # TODO: Handle the case of more than one acs
        service = get_object_or_404(
            models.Service,
            resource=consumer,
            profile=acs
        )

        # Assign subject id to user
        if 'saml:subject' not in request.session:
            request.session['saml:subject'] = uuid4().hex

        # Construct SAML response
        # FIXME: This should go in `python-saml`, perhaps?
        obj = schema.samlp.Response(
            issuer=schema.saml.Issuer(provider.name),
            status=schema.samlp.Status(
                code=schema.samlp.StatusCode(
                    value=schema.samlp.StatusCode.Value.SUCCESS
                )
            ),
            assertion=saml.Assertion(
                issuer=schema.saml.Issuer(provider.name),
                subject=schema.saml.Subject(
                    id=schema.saml.NameID(request.session['saml:subject']),
                    confirm=schema.saml.SubjectConfirmation(
                        data=schema.saml.SubjectConfirmationData(
                            in_response_to=consumer.name,
                            not_before=datetime.utcnow(),
                            not_on_or_after=datetime.utcnow() +
                                timedelta(minutes=2)
                        )
                    )
                ),
                statements=[
                    schema.saml.AuthenticationStatement(
                        session_not_on_or_after=datetime.utcnow() +
                            timedelta(minutes=2),
                        context=schema.saml.AuthenticationContext(
                            reference=schema.saml.AuthenticationContext.
                                Reference.PREVIOUS_SESSION
                        )
                    )
                ]
            )
        )

        # DEBUG
        dob = schema.samlp.Response.serialize(obj)
        s = etree.tostring(dob, pretty_print)

        print(s)


def slo(request, *args, **kwargs):
    """Single log on (SLO)"""
    pass
