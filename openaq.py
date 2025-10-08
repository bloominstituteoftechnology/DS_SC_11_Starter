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

    def _send(self, endpoint, method='GET', **kwargs):
        """Make an API call of any method

        :param endpoint: API endpoint
        :param method: API call type. Options are PUT, POST, GET, DELETE

        :type endpoint: string
        :type method: string

        :returns: (status_code, json_response)

        :raises ApiError: raises an exception
        """
        # For OpenAQ API v3, use API key in headers instead of basic auth
        auth = (self._key, self._pswd) if self._pswd else None
        url = self._make_url(endpoint, **kwargs)

        if method == 'GET':
            resp = requests.get(url, auth=auth, headers=self._headers)
        else:
            raise ApiError("Invalid Method")

        if resp.status_code != 200:
            raise ApiError("A bad request was made: {}".format(resp.status_code))

        res = resp.json()

        # Add a 'pages' attribute to the meta data
        try:
            res['meta']['pages'] = math.ceil(res['meta']['found'] / res['meta']['limit'])
        except:
            pass

        return resp.status_code, res

    def _get(self, url, **kwargs):
        return self._send(url, 'GET', **kwargs)


class OpenAQ(API):
    """Create an instance of the OpenAQ API

    """

    def __init__(self, version='v3', **kwargs):
        """Initialize the OpenAQ instance.

        :param version: API version.
        :param kwargs: API options.

        :type version: string
        :type kwargs: dictionary

        """
        self._baseurl = 'https://api.openaq.org'

        super(OpenAQ, self).__init__(version=version, baseurl=self._baseurl, **kwargs)

    def cities(self, **kwargs):
        """Returns a listing of cities within the platform.

        :param country: limit results by a certain country
        :param limit: limit results in the query. Default is 100. Max is 10000.
        :param page: paginate through the results. Default is 1.
        :param order_by: order by one or more fields (ex. order_by=['country', 'locations']). Default value is 'country'
        :param sort: define the sort order for one or more fields (ex. sort='desc')

        :return: dictionary containing the *city*, *country*, *count*, and number of *locations*

        :type country: 2-digit ISO code
        :type limit: number
        :type order_by: string or list of strings
        :type sort: string
        :type page: number
        :type country: string or array of strings
        :type df: bool
        :type index: string

        :Example:

        >>> import openaq
        >>> api = openaq.OpenAQ()
        >>> status, resp = api.cities()
        >>> resp['results']
        [
            {
                "city": "Amsterdam",
                "country": "NL",
                "count": 21301,
                "locations": 14
            },
            {
                "city": "Badhoevedorp",
                "country": "NL",
                "count": 2326,
                "locations": 1
            },
            ...
        ]
        """
        return self._get('cities', **kwargs)
