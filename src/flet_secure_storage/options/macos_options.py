from dataclasses import dataclass

from .apple_options import AppleOptions


@dataclass
class MacOsOptions(AppleOptions):
    """
    Creates Apple-specific macOS options for secure storage.
    [Reference - macos_options.dart](https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/macos_options.dart) # noqa: E501

    Attributes:
        uses_data_protection_keychain: `kSecUseDataProtectionKeychain` (macOS only): **Shared**.
            Indicates whether the macOS data protection keychain is used.
            Not applicable on iOS.

        All other attributes are inherited from AppleOptions.
    """

    uses_data_protection_keychain: bool = True

    def options(
        self,
    ) -> dict[str, str | bool | int | list[str] | None]:
        opts = super().options()
        opts.update(
            {
                "usesDataProtectionKeychain": self.uses_data_protection_keychain,
            }
        )
        return opts
