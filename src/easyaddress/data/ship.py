from __future__ import annotations
from typing import Optional
import uuid, json, time
from dataclasses import dataclass, asdict, field


@dataclass
class Address:
    
    first_name : str
    last_name : str
    company_name : str

    email : str
    phone : str

    street : str
    street_number : str
    # line_2 = models.CharField(null=True, blank=True) # TODO
    zipcode : str
    city : str
    province : Optional[str]
    country : str

    reference : Optional[str]

    environment : str # TODO

    


@dataclass
class Parcel:

    sender : Address
    receiver : Address

    width  : float
    length : float
    height : float
    weight : float

    unit_of_mass   : str
    unit_of_length : str
    id : Optional[str] = field(default=None, init=True)


@dataclass
class CarrierProduct:
    
    name : str
    carrier : str
    id : Optional[str] = field(default=None, init=True)


@dataclass
class ParcelOrder:
    parcel : Parcel
    carrier_product : CarrierProduct

    id : Optional[str] = field(default=None, init=True)

"""
from __future__ import annotations
from typing import Optional
import uuid, json, time
from dataclasses import dataclass, asdict
import requests

@dataclass
class Country:
    id : str #uuid.UUID


@dataclass
class Province:
    id : str #uuid.UUID


@dataclass
class Address:
    first_name : str
    last_name : str
    company_name : str

    email : str
    phone : str

    street : str
    street_number : str
    # line_2 = models.CharField(null=True, blank=True) # TODO
    zipcode : str
    city : str
    province : Optional[Province]
    country : Country

    reference : Optional[str]

    environment : str


@dataclass
class Parcel:
    sender : Address
    receiver : Address

    width  : float
    length : float
    height : float
    weight : float

    unit_of_mass   : str
    unit_of_length : str



if __name__ == "__main__":
    # print("Hello World")
    
    de_id = "00000000-0000-0000-0000-032000000000"
    de = Country(id=de_id)

    sender = Address(
        first_name="Sebastian",
        last_name="Steins",
        company_name="ectual",
        email="hi@seb.st",
        phone="+491776496013",
        street="Haaler Str",
        street_number="64",
        zipcode="52146",
        city="Würselen",
        province=None,
        country=de_id,
        reference="SEN1",
        environment="0178d6bf-b8c1-94d0-c264-020361ca13c9"
    )
    receiver = Address(
        first_name="Sebastian",
        last_name="Steins",
        company_name="ectual",
        email="hi@seb.st",
        phone="+491776496013",
        street="Haaler Str",
        street_number="64",
        zipcode="52146",
        city="Würselen",
        province=None,
        country=de_id,
        reference="REC1",
        environment="0178d6bf-b8c1-94d0-c264-020361ca13c9"
    )

    parcel = Parcel(
        sender=sender,
        receiver=receiver,
        width=10,
        height=10,
        length=10,
        weight=1,
        unit_of_length="cm",
        unit_of_mass="kg"
    )

    # print(asdict(parcel))

    url = "http://localhost:8000/v1/environments/0178d6bf-b8c1-94d0-c264-020361ca13c9/parcels/"
    # response = requests.post(url, data=asdict(parcel))
    # response = requests.post(url, data=json.dumps(asdict(parcel)))
    response = requests.post(url, json=asdict(parcel))
    # print(response)
    # print(response.text)

    
    # print(json.dumps(asdict(parcel)))

    response_json = response.json()
    parcel_id = response_json['id']

    print("Parcel", parcel_id, "created")

    url = url + parcel_id + "/orders/"
    print(url)

    for i in range(3):
        print(".")
        # time.sleep(1)
    print("Ordering the parcel now!")

    response = requests.post(url, json={'carrier_product': '0178d716-08d3-84b8-64d7-54b35bc0d1e0'})
    print(response)
    print(response.text)
"""