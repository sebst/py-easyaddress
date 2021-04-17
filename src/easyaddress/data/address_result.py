from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class ValidatedAddress():
    validated_street_number : str
    validated_street        : str
    validated_city          : str
    validated_zipcode       : str
    # validated_province      : Optional[Region]
    # validated_country       : Optional[Country]
