from dataclasses import dataclass


@dataclass
class WindowsOptions:
    """
    Creates Windows-specific options for secure storage.

    [Reference - windows_options.dart](https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/windows_options.dart) # noqa: E501

    Attributes:
        use_backward_compatibility: Determines whether to use backward
            compatibility mode to read values from a previous version's storage.
    """

    # Configurable options and their default values
    use_backward_compatibility: bool = False

    def options(self) -> dict[str, bool]:
        """
        Serialize WindowsOptions for Flutter Secure Storage.

        Returns:
            Mapping of option names expected by the Flutter Secure Storage plugin.
        """
        return {
            "useBackwardCompatibility": self.use_backward_compatibility,
        }
