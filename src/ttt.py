from easyaddress import API, set_api_key,set_api_secret, validate_email, validate
from easyaddress.easyaddress_ship import API as ShipAPI

# print(API().validate_email("hi@seb.st"))
# set_api_key("ABC")
# api = API()
# print("api.key", api.api_key)

# set_api_key("ABC")
# api = API()
# print("api.key", api.api_key)


# print(validate_email("sebastian.steins@gmail.de"))


# r = validate_email("sebastian.steins@gmail.com")
# print(r.mx[0])
# print(type(r.mx[0]))

# test:8wvc4txWtUGBEMbJZFbDDcjS
# test:$apr1$KGk0tqvE$D6QZObBNWIlaGh74yKmX61

set_api_key('test')
set_api_secret("8wvc4txWtUGBEMbJZFbDDcjS")
api = API()
from easyaddress.data.address import ValidatableAddress


"""
320 Fowler Street, Lynbrook, New York

31 Spooner Street, Quahog, Rhode Island

1882 Gerard Street, San Francisco, California

129 West 81st Street, New York, New York

1407 Graymalkin Lane, Salem Center, New York

"""

address = ValidatableAddress(
    street_number="320",
    street="Fowler Street",
    city="Lynbrook",
    zipcode="0",
    province="NY",
    country="US",
    reference=None
)
address = ValidatableAddress(
    street_number="64",
    street="Haaler Str",
    city="Würselen",
    zipcode="52146",
    province="NW",
    country="DE",
    reference=None
)

r = api.validate(address)
print(r)



# print(API().validate_email("hi@seb.st"))
# set_api_key("ABC")
api = ShipAPI()
print("api.key", api.api_key, api, type(api))


from easyaddress.data.ship import Address, Parcel

de_id = "00000000-0000-0000-0000-032000000000"
# de = Country(id=de_id)

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
    environment="0178e63d-af4a-37bc-5d61-b750514998bd"
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
    environment="0178e63d-af4a-37bc-5d61-b750514998bd"
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


parcel_created = api.create_parcel(parcel)
print(parcel_created.id, "created.")

# api.order_parcel(parcel_created, carrier_product="0178e658-58f1-8d47-02f2-3566b3ed3842")
#0178e9d9-6842-d1f0-c637-68e9eb028b22
res = api.order_parcel(parcel_created, carrier_product="0178e9d9-6842-d1f0-c637-68e9eb028b22")
print(res)


api.get_parcel_label_pdf_bytes(res)