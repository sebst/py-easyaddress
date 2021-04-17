#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = []


"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from easyaddress_countries.models import Country, Region


__all__ = ['ValidatableAddress', 'ValidatedAddress', 'ValidationResult', 'ValidatedEmail', 'MXResult', 'ValidatableEmail']


@dataclass
class ValidatableEmail():
    email                   : str

@dataclass
class MXResult():
    priority                : int
    server                  : str

@dataclass
class ValidatedEmail():
    email                   : str

    validated_email         : str
    validation_success      : bool
    is_freemail             : bool
    is_disposable           : bool
    smtp_validation         : str
    did_you_mean            : str
    mx                      : list[MXResult]



@dataclass
class ValidatableAddress():
    street_number           : str
    street                  : str
    city                    : str
    zipcode                 : str
    province                : str
    country                 : str
    reference               : Optional[str]




@dataclass
class ValidatedAddress():
    validated_street_number : str
    validated_street        : str
    validated_city          : str
    validated_zipcode       : str
    validated_province      : Optional[Region]
    validated_country       : Optional[Country]


@dataclass
class ValidationResult(ValidatableAddress, ValidatedAddress):
    validation_success      : bool

    def to_oneline(self):
        raise NotImplementedError()




"""