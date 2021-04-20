import os, json
from dataclasses import asdict
from .http import get, post

from .easyaddress import BaseAPI
from .data.ship import Parcel, ParcelOrder

class API(BaseAPI):
    def create_parcel(self, parcel: Parcel) -> Parcel:
        if not isinstance(parcel, Parcel):
            raise TypeError("`parcel` needs to be `Parcel`.")
        response = post(self._build_url('parcel.create'),
                        headers=self._build_headers(),
                        auth=self._build_auth(),
                        data=asdict(parcel))
        if response.status_code != 201:
            raise RuntimeError("Error.")
        # return response.data # TODO
        data = response.data
        data = Parcel(**data)
        return data

    def validate_parcel(self, parcel):
        if not isinstance(parcel, Parcel):
            raise TypeError("`parcel` needs to be `Parcel`.")
        if parcel.id is None:
            raise RuntimeError("`parcel` object needs to have an `id` property. Please create the parcel first.")
        # parcel_id
        response = post(self._build_url('parcel.validate').replace('{parcel_id}', parcel.id),
                        headers=self._build_headers(),
                        auth=self._build_auth(),
                        data={})
        print(response)

    def order_parcel(self, parcel, carrier_product):
        if not isinstance(parcel, Parcel):
            raise TypeError("`parcel` needs to be `Parcel`.")
        if parcel.id is None:
            raise RuntimeError("`parcel` object needs to have an `id` property. Please create the parcel first.")
        # TODO: Check if validated.
        response = post(self._build_url('parcel.order').replace('{parcel_id}', parcel.id),
                        headers=self._build_headers(),
                        auth=self._build_auth(),
                        data={'carrier_product': carrier_product})
        print(response.status_code, response.data)
        print("Parcel", response.data["parcel"])
        print("CarrierProduct", response.data["carrier_product"])
        print("Id", response.data["id"])
        parcel_order = ParcelOrder(parcel=response.data["parcel"], carrier_product=response.data["carrier_product"], id=response.data["id"]) # TODO!
        return parcel_order
        print(response)

    def get_parcel_label_pdf_bytes(self, parcel_order):
        print("get_parcel_label_pdf_bytes", parcel_order)
        # return
        response = get(url := self._build_url('parcel_order.label')
                            .replace('{parcel_id}', parcel_order.parcel) # TODO: .id
                            .replace('{parcel_order_id}', parcel_order.id),
                       headers=self._build_headers(),
                       auth=self._build_auth(),
                       data=None,
                       parse=lambda x,y,z:(y,None))
        print("URL"*88, url)
        print(response.status_code, response.data[:100])
        print()
        print()
        print(url)

    def cancel_parcel_order(self, parcel_order):
        pass
