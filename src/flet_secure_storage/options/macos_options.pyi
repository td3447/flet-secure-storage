from dataclasses import dataclass

from .apple_options import AppleOptions

@dataclass
class MacOsOptions(AppleOptions):
    uses_data_protection_keychain: bool = True
