"""Simple openaq to only depend on json, math, and requests (no dfs/plots)."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import math


class ApiError(Exception):
    pass
