from dataclasses import dataclass

from .apple_options import AppleOptions


@dataclass
class IOSOptions(AppleOptions):
    """
    Creates Apple-specific iOS options for secure storage.
    [Reference - ios_options.dart](https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/ios_options.dart) # noqa: E501

    Attributes:
        None: Currently there are no specific ios options available, but only shared
            options from apple options.
    """

    # Inherits all options from AppleOptions

    def options(
        self,
    ) -> dict[str, str | bool | int | list[str] | None]:
        opts = super().options()
        opts.update(
            {
                # No iOS-specific options yet
            }
        )
        return opts
