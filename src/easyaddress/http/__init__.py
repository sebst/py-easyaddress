from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

import urllib3, json

http = urllib3.PoolManager()

@dataclass
class Response():
    status_code : int
    data : object
    headers : dict


def default_parse(status, data, headers):
    print(data)
    data = json.loads(data)
    return data, headers


def post(url, headers, auth, data, parse=default_parse) -> Response:
    encoded_data = json.dumps(data)
    if auth:
        auth = urllib3.make_headers(basic_auth=auth)
        headers = {**headers, **auth}
    r = http.request('POST',
                     url,
                     body=encoded_data,
                     headers=headers)
    # print(r.status)
    # print(r.data)
    # data = json.loads(r.data)
    data, headers = parse(r.status, r.data, r.headers)
    return Response(r.status, data, {})


def get(url, headers, auth, data, parse=default_parse) -> Response:
    # encoded_data = json.dumps(data) TODO
    if auth:
        auth = urllib3.make_headers(basic_auth=auth)
        headers = {**headers, **auth}
    r = http.request('GET',
                     url,
                    #  body=encoded_data,
                     headers=headers)
    data, headers = parse(r.status, r.data, r.headers)
    return Response(r.status, data, {})