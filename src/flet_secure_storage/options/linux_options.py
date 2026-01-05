from dataclasses import dataclass


@dataclass
class LinuxOptions:
    """
    Creates Linux-specific options for secure storage.

    [Reference - linux_options.dart](https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/linux_options.dart)

    Attributes:
        None: Currently, there are no specific options available for Linux secure storage.
    """

    # Configurable options and their default values
    # Currently there are no specific linux options available.

    def options(self) -> dict[str, str]:
        """
        Serialize LinuxOptions for Flutter Secure Storage.

        Currently there are not specific linux options available,
            and will return anempty dictionary.

        Returns:
            Mapping of option names expected by the Flutter Secure Storage plugin.
        """
        return {}
