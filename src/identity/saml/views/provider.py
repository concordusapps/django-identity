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
from ..client import binding

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

    # Determine if we are from the login form or not
    from_login = request.method == 'GET' and len(request.GET) == 1

    if not from_login:
        # Generate request identifier to namespace variables stored in session
        # storage
        identifier = uuid4().hex
    else:
        # Grab the identifier from the GET paramter passed back from the login
        # form
        identifier = request.GET['id']

    # Template to pull namespaced items out of the session storage
    storage = '{}:saml:{{}}'.format(identifier)

    if not from_login:
        # Decode and deserialize the message
        message, state = binding.Binding.receive(request, 'request')
        xml = etree.XML(message)
        obj = schema.samlp.AuthenticationRequest.deserialize(xml)

        # Verify that the issuing consumer is known to identity
        consumer = get_object_or_404(Consumer, name=obj.issuer.text)
    else:
        # Get the consumer from the identifier passed from the login form
        consumer = get_object_or_404(
            Consumer,
            slug=request.session[storage.format('consumer')]
        )

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

    if not from_login:
        # TODO: Perform validation of message
        pass

    # Store items in namespaced session storage
    request.session[storage.format('provider')] = provider.slug
    request.session[storage.format('consumer')] = consumer.slug
    request.session[storage.format('message:id')] = obj.id
    request.session[storage.format('state')] = state

    if not request.user.is_authenticated():
        # Send user off to get authenticated;
        # redirect to login page
        return redirect('{}?{}'.format(
            reverse('login'),
            urlencode({'id': identifier})
        ))
    else:
        # Assign subject id to user if not already assigned
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
            assertion=schema.saml.Assertion(
                issuer=schema.saml.Issuer(provider.name),
                subject=schema.saml.Subject(
                    id=schema.saml.NameID(request.session['saml:subject']),
                    confirm=schema.saml.SubjectConfirmation(
                        data=schema.saml.SubjectConfirmationData(
                            in_response_to=consumer.name
                        )
                    )
                ),
                statements=[
                    schema.saml.AuthenticationStatement(
                        context=schema.saml.AuthenticationContext(
                            reference=schema.saml.AuthenticationContext.
                                Reference.PREVIOUS_SESSION
                        )
                    ),
                    schema.saml.AttributeStatement(
                        attributes=[
                            schema.saml.Attribute(
                                name='uid',
                                values=request.user.username
                            ),
                        ]
                    ),
                ]
            )
        )

        # Serialize message to a string
        message = etree.tostring(schema.samlp.Response.serialize(obj))
        print(message)

        # Send off
        return binding.Redirect.send(
            service.get_absolute_url(),
            message,
            request.session[storage.format('state')],
            'response'
        )


def slo(request, *args, **kwargs):
    """Single log on (SLO)"""
    pass
