#!/usr/bin/env python3

import json
import jsonschema
import platform
import hashlib
from datetime import datetime
from pathlib import Path

from typing import Union, Self

# --------------------------------------------------------------------------
# Schemas (for now, since loading json from package is trixy)
# --------------------------------------------------------------------------
_config_schema = {
  "type": "object",
  "properties" : {
    "client_key": {
      "type": "string"
    },
    "client_secret": {
      "type": "string"
    }
  },
  "required": [
    "client_key",
    "client_secret"
  ]
}


# --------------------------------------------------------------------------
# Classes
# --------------------------------------------------------------------------

class InvalidCredentialStore(RuntimeError):
    pass


class InvalidCredentialFileError(RuntimeError):
    pass


class Token:
    def __init__(self, token_key:str, token_value:str, expires:Union[None, datetime] = None):
        super().__init__()
        self.token_key = token_key
        self.file_name = hashlib.sha256(token_key.encode()).hexdigest()
        self.token_value = token_value
        self.expires = expires


class CredentialManager:

    def __init__(self, store: Union[None, Path] = None) -> Self:
        super().__init__()
        # Set up location for credential store
        self.store = store if store is not None else (Path.home() / '.credmgr')
        if not self.store.exists():
            self.store.mkdir(parents = True, exist_ok = True)
        elif not self.store.is_dir():
            raise InvalidCredentialStore(self.store)
        # Credential store management paths
        self.lockfile = self.store / '.lock'
        # Load config if exists
        try:
            with (self.store / '.config').open('r') as cf:
                self.config = json.load(cf)
                jsonschema.validate(self.config, _config_schema)
        except json.JSONDecodeError as exc:
            raise InvalidCredentialFileError('Failed to read .config file.') from exc
        except jsonschema.ValidationError as exc:
            raise InvalidCredentialFileError('Invalid config file.') from exc
        except FileNotFoundError:
            pass

    def get_token(self, token_key:str) -> Union[None, Token]:

    @staticmethod
    def _get_windows_machine_id() -> Union[None, str]:
        try:
            import winreg
            registry = winreg.HKEY_LOCAL_MACHINE
            address = r'SOFTWARE\Microsoft\Cryptography'
            key_args = winreg.KEY_READ | winreg.KEY_WOW64_64KEY
            key = winreg.OpenKey(registry, address, key_args)
            try:
                value = winreg.QueryValueEx(key, 'MachineGuid')
            finally:
                winreg.CloseKey(key)
            if value is not None:
                return value[0]
            return None
        except (ImportError, ModuleNotFoundError):
            return None

    @staticmethod
    def _get_unix_machine_id() -> Union[None, str]:
        try:
            with open('/var/lib/dbus/machine-id', 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    @staticmethod
    def get_machine_id() -> Union[None, str]:
        match platform.system().lower():
            case 'windows':
                return CredentialManager._get_windows_machine_id()
            case ['darwin', 'linux']:
                return CredentialManager._get_unix_machine_id()
            case _:
                return None


cm = CredentialManager()