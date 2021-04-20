#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = []

import os

_SDK_VERSION             = "0.0.1"
_SDK_API_KEY_VAR         = "EASYADDRESS_API_KEY"
_SDK_API_SECRET_VAR      = "EASYADDRESS_API_SECRET"
_SDK_API_HOST_VAR        = "EASYADDRESS_API_HOST"
_SDK_API_ENVIRONMENT_VAR = "EASYADDRESS_API_ENVIRONMENT"

_API_VERSION             = "v1"
_API_KEY_DEFAULT         = None
_API_SECRET_DEFAULT      = None
_API_SCHEME              = "https"
_API_HOST_DEFAULT        = "api.easyaddress.io"
_API_ENVIRONMENT_DEFAULT = None
_API_KEY                 = lambda: os.environ.get(_SDK_API_KEY_VAR,         _API_KEY_DEFAULT)
_API_SECRET              = lambda: os.environ.get(_SDK_API_SECRET_VAR,      _API_SECRET_DEFAULT)
_API_HOST                = lambda: os.environ.get(_SDK_API_HOST_VAR,        _API_HOST_DEFAULT)
_API_ENVIRONMENT         = lambda: os.environ.get(_SDK_API_ENVIRONMENT_VAR, _API_ENVIRONMENT_DEFAULT)
_API_JSON_TYPE           = "application/json" # "application/vnd.api+json"

_USER_AGENT               = f"pypi-easyaddress/{_SDK_VERSION} ({_API_VERSION} compat.)"


_API_ENDPOINTS = {
    'email.validate'       : f"{_API_SCHEME}://%s/{_API_VERSION}/emails/",
    'address.validate'     : f"{_API_SCHEME}://%s/{_API_VERSION}/addresses/",
    'parcel.create'        : f"{_API_SCHEME}://%s/{_API_VERSION}/environments/%s/parcels/",
    'parcel.validate'      : f"{_API_SCHEME}://%s/{_API_VERSION}/environments/%s/parcels/{{parcel_id}}/",
    'parcel.order'         : f"{_API_SCHEME}://%s/{_API_VERSION}/environments/%s/parcels/{{parcel_id}}/orders/",
    'parcel_order.label'   : f"{_API_SCHEME}://%s/{_API_VERSION}/environments/%s/parcels/{{parcel_id}}/orders/{{parcel_order_id}}/label/",
    # 'parcel_order.cancel'  : f"{_API_SCHEME}://%s/{_API_VERSION}/environments/%s/parcels/{{parcel_id}}/orders/{{parcel_order_id}}/",
}