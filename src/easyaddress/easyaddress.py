import os
from dataclasses import asdict
from .config import _API_KEY, _API_SECRET, _API_HOST, _SDK_API_KEY_VAR, _SDK_API_SECRET_VAR, _API_ENDPOINTS, _USER_AGENT, _API_JSON_TYPE, _API_ENVIRONMENT
from .http import post
from .data.email import ValidatableEmail
from .data.address import ValidatableAddress
from .data.email_result import ValidatedEmail


class BaseAPI:
    def __init__(self,
                 api_key=None,
                 api_secret=None,
                 api_host=None,
                 environment=None):
        """
        """
        if api_key is None:
            api_key = _API_KEY()
        if api_secret is None:
            api_secret = _API_SECRET()
        if api_host is None:
            api_host = _API_HOST()
        if environment is None:
            environment = _API_ENVIRONMENT()
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_host = api_host
        self.environment = environment
        # if any(c is None for c in [self.api_key, self.api_secret, self.api_host]):
            # raise RuntimeError("easyaddress.io API not set up properly. Please provide KEY and SECRET.")

    def _build_url(self, endpoint_name):
        """
        """
        try: # TODO
            return _API_ENDPOINTS[endpoint_name]%(self.api_host)
        except:
            return _API_ENDPOINTS[endpoint_name]%(self.api_host, self.environment)

    def _build_headers(self):
        """
        """
        return {
            'User-Agent': _USER_AGENT,
            'Accept': _API_JSON_TYPE,
            'Content-Type': _API_JSON_TYPE,
        }
    
    def _build_auth(self):
        """
        """
        if self.api_key is not None and self.api_secret is not None:
            return f"{self.api_key}:{self.api_secret}"


class API(BaseAPI):
    """
    """

    def validate_email(self,
                       email,
                       test_mx=False) -> ValidatedEmail:
        """
        """
        if isinstance(email, str):
            email = ValidatableEmail(email)
        if not isinstance(email, ValidatableEmail):
            raise TypeError("`email` needs to be `str` or `ValidatebleEmail`.")
        response = post(self._build_url('email.validate'),
                        headers=self._build_headers(),
                        auth=self._build_auth(),
                        data=asdict(email))
        if response.status_code != 201:
            raise RuntimeError("Error.")
        data = ValidatedEmail(**response.data)
        return data

    def validate_address(self,
                         address):
        """
        """
        if not isinstance(address, ValidatableAddress):
            raise TypeError("`address` needs to be `ValidatableAddress`.")
        response = post(self._build_url('address.validate'),
                        headers=self._build_headers(),
                        auth=self._build_auth(),
                        data=asdict(address))
        print(response)

    def validate(self, validation_object, *args, **kwargs):
        """
        """
        if isinstance(validation_object, ValidatableEmail):
            return self.validate_email(validation_object, *args, **kwargs)
        elif isinstance(validation_object, ValidatableAddress):
            return self.validate_address(validation_object, *args, **kwargs)
        else:
            raise TypeError("`validation_object` needs to be `ValidatableAddress` or `ValidatebleEmail`.")
    
    def __str__(self):
        return f"easyaddress.io API client @ {self.api_host}"


def validate_email(email, *args, **kwargs):
    """Shortcut method to validate an email. See API.validate_email."""
    return API().validate_email(email, *args, **kwargs)

def validate_address(address, *args, **kwargs):
    """Shortcut method to validate an address. See API.validate_address."""
    return API().validate_address(address, *args, **kwargs)

def validate(validation_object, *args, **kwargs):
    """Shortcut method to validate an object. See API.validate."""
    return API().validate(validation_object, *args, **kwargs)

def set_api_key(api_key):
    """
    """
    os.environ[_SDK_API_KEY_VAR] = str(api_key)

def set_api_secret(api_secret):
    """
    """
    os.environ[_SDK_API_SECRET_VAR] = str(api_secret)