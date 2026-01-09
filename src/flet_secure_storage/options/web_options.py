from dataclasses import dataclass


@dataclass
class WebOptions:
    """
    Creates Web-specific options for secure storage.

    [Reference - web_options.dart](https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/web_options.dart) # noqa: E501

    Attributes:
        db_name: The name of the database used for secure storage.
        public_key: The public key used for encryption.
        wrap_key: The key used to wrap the encryption key.
        wrap_key_iv: The initialization vector (IV) used for the wrap key.
        use_session_storage: Whether to use session storage instead of local storage.
    """

    # Configurable options and their default values
    db_name: str = "FletEncryptedStorage"
    public_key: str = "FletSecureStorage"
    wrap_key: str = ""
    wrap_key_iv: str = ""
    use_session_storage: bool = False

    def options(self) -> dict[str, str | bool]:
        """
        Serialize WebOptions for Flutter Secure Storage.

        Returns:
            Mapping of option names expected by the Flutter Secure Storage plugin.
        """
        return {
            "dbName": self.db_name,
            "publicKey": self.public_key,
            "wrapKey": self.wrap_key,
            "wrapKeyIv": self.wrap_key_iv,
            "useSessionStorage": self.use_session_storage,
        }
