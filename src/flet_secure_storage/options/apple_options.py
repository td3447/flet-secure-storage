from dataclasses import dataclass


@dataclass
class AppleOptions:
    """
    Creates Apple-specific options for secure storage.
    https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/apple_options.dart
    """

    # Configurable options and their default values
    # use_backwards_compatibility: bool = False

    def options(self) -> dict[str, str]:
        return {
            # "useBackwardsCompatibility": self.use_backwards_compatibility,
        }
