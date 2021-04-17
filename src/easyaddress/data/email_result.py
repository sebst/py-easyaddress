from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

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