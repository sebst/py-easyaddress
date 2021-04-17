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


def post(url, headers, auth, data) -> Response:
    encoded_data = json.dumps(data)
    # headers = urllib3.make_headers(basic_auth='abc:xyz', **headers)
    # headers = urllib3.make_headers(**headers)
    r = http.request('POST',
                     url,
                     body=encoded_data,
                     headers=headers)
    print(r)
    try:
        data = json.loads(r.data)
    except:
        data = r.data
    return Response(r.status, data, {})