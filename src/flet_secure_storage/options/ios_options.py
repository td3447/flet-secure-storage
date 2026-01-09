from dataclasses import dataclass

from .apple_options import AppleOptions


@dataclass
class IOSOptions(AppleOptions):
    """
    Creates Apple-specific iOS options for secure storage.
    [Reference - ios_options.dart](https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/ios_options.dart) # noqa: E501

    Attributes:
        None: Still under development.
    """

    # Configurable options and their default values
    # TODO: Add iOS-specific options.

    def options(self) -> dict[str, str]:
        return {}
