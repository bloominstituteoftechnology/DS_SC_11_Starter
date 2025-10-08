"""Simple openaq to only depend on json, math, and requests (no dfs/plots)."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import math


class ApiError(Exception):
    pass


class API:
    """Generic API wrapper object."""

    def __init__(self, **kwargs):
        self._key = kwargs.pop('key', '')
        self._pswd = kwargs.pop('pswd', '')
        self._version = kwargs.pop('version', None)
        self._baseurl = kwargs.pop('baseurl', None)
        self._headers = {'content-type': 'application/json'}
        # Add API key to headers if provided
        if self._key:
            self._headers['X-API-Key'] = self._key

    def _make_url(self, endpoint, **kwargs):
        """Internal method to create a url from an endpoint.
        :param endpoint: Endpoint for an API call
        :type endpoint: string
        :returns: url
        """
        endpoint = "{}/{}/{}".format(self._baseurl, self._version, endpoint)

        extra = []
        for key, value in kwargs.items():
            if isinstance(value, list) or isinstance(value, tuple):
                # value = ','.join(value)
                for v in value:
                    extra.append("{}={}".format(key, v))
            else:
                extra.append("{}={}".format(key, value))

        if len(extra) > 0:
            endpoint = '?'.join([endpoint, '&'.join(extra)])

        return endpoint
