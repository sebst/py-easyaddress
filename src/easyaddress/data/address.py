from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class ValidatableAddress():
    street_number           : Optional[str]
    street                  : str
    city                    : str
    zipcode                 : str
    province                : Optional[str]
    country                 : str
    reference               : Optional[str]

