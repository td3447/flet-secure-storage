import warnings
from dataclasses import dataclass
from enum import Enum, unique

from flet_secure_storage._helpers import parse_bool, parse_enum, parse_str

__all__ = ["AndroidOptions", "KeyCipherAlgorithm", "StorageCipherAlgorithm"]


# Enums
@unique
class KeyCipherAlgorithm(Enum):
    """
    Algorithm used to encrypt the secret key. By default RSA/ECB/OAEPWithSHA-256AndMGF1Padding
        is used (API 23+). Legacy RSA/ECB/PKCS1Padding is available for backwards compatibility.

    Attributes:
        RSA_ECB_PKCS1Padding:Legacy RSA/ECB/PKCS1Padding for backwards compatibility.

        RSA_ECB_OAEPwithSHA_256andMGF1Padding: RSA/ECB/OAEPWithSHA-256AndMGF1Padding
            (default, API 23+).

        AES_GCM_NoPadding: AES/GCM/NoPadding for KeyStore-based key wrapping (supports biometrics).
    """

    RSA_ECB_PKCS1Padding = "RSA_ECB_PKCS1Padding"
    RSA_ECB_OAEPwithSHA_256andMGF1Padding = "RSA_ECB_OAEPwithSHA_256andMGF1Padding"
    AES_GCM_NoPadding = "AES_GCM_NoPadding"


@unique
class StorageCipherAlgorithm(Enum):
    """
    Algorithm used to encrypt stored data. By default AES/GCM/NoPadding is used (API 23+).
        Legacy AES/CBC/PKCS7Padding is available for backwards compatibility.

    Attributes:
        AES_CBC_PKCS7Padding: Legacy AES/CBC/PKCS7Padding for backwards compatibility.
        AES_GCM_NoPadding: AES/GCM/NoPadding (default, API 23+).
    """

    AES_CBC_PKCS7Padding = "AES_CBC_PKCS7Padding"
    AES_GCM_NoPadding = "AES_GCM_NoPadding"


@dataclass
class AndroidOptions:
    """
    Creates Android-specific options for secure storage.
    [Reference - android_options.dart](https://github.com/juliansteenbakker/flutter_secure_storage/blob/05b1c4be30a1c7142dfba6db41b32aa8e6a38c58/flutter_secure_storage/lib/options/android_options.dart)

    Attributes:
        encrypted_shared_preferences: EncryptedSharedPrefences
            are only available on API 23 and greater

        reset_on_error: When an error is detected, automatically reset all data.

            WARNING: This will prevent fatal errors regarding an unknown key however keep in
            mind that it will `PERMANENTLY` erase the data when an error occurs.

            Defaults to `True`.

        migrate_on_algorithm_change: When the encryption algorithm changes, automatically
            migrate existing data to the new algorithm. This preserves data across
            algorithm upgrades.

            `Note:` If false, data will be lost when algorithm changes unless
            `reset_on_error` is true.

            Defaults to `True`.

        enforce_biometrics: Whether to enforce biometric/PIN authentication.

            When `True`, the plugin will throw an exception if the device
            has no PIN, pattern, password, or biometric enrolled. The key will
            be generated with setUserAuthenticationRequired(true).

            When `False` (default), the plugin will gracefully degrade
            to storing data without biometric protection if unavailable.
            The key will be generated with setUserAuthenticationRequired(false).

            Security Note: Set to `True` for highly sensitive data that must
            never be stored without authentication.

            Defaults to `False`.

        key_cipher_algorithm: Algorithm used to encrypt the secret key.
            By default RSA/ECB/OAEPWithSHA-256AndMGF1Padding is used (API 23+).
            Legacy RSA/ECB/PKCS1Padding is available for backwards compatibility.

        storage_cipher_algorithm: Algorithm used to encrypt stored data.

            By default AES/GCM/NoPadding is used (API 23+).

            Legacy AES/CBC/PKCS7Padding is available for backwards compatibility.

        shared_preferences_name: The name of the sharedPreference database to use.
            You can select your own name if you want. A default name will
            be used if nothing is provided here.

            `WARNING:`If you change this you can't retrieve already saved preferences.

        preferences_key_prefix: The prefix for a shared preference key. The prefix is used to make
            sure the key is unique to your application. An underscore (_) is added to the
            end of the prefix automatically. If not provided, a default prefix will
            be used.

            Example: preferencesKeyPrefix: "my_app" will result in a key like
            "my_app_key1".

            `WARNING:` If you change this you can't retrieve already saved preferences.

        biometric_prompt_title: The title shown in the biometric authentication prompt.

        biometric_prompt_subtitle: The subtitle shown in the biometric authentication prompt.
    """

    # Configurable options and their default values
    encrypted_shared_preferences: bool | None = None
    reset_on_error: bool = True
    migrate_on_algorithm_change: bool = True
    enforce_biometrics: bool = False
    key_cipher_algorithm: KeyCipherAlgorithm = (
        KeyCipherAlgorithm.RSA_ECB_OAEPwithSHA_256andMGF1Padding
    )
    storage_cipher_algorithm: StorageCipherAlgorithm = (
        StorageCipherAlgorithm.AES_GCM_NoPadding
    )
    shared_preferences_name: str = ""
    preferences_key_prefix: str = ""
    biometric_prompt_title: str = "Authenticate to access"
    biometric_prompt_subtitle: str = "Use biometrics or device credentials"

    def __post_init__(self):
        # Deprecation warning for encrypted_shared_preferences
        if self.encrypted_shared_preferences is None:
            self.encrypted_shared_preferences = False
        else:
            warnings.warn(
                "encrypted_shared_preferences is deprecated and will be removed in v11. "
                "The Jetpack Security library is deprecated by Google. "
                "Remove this parameter — it will be ignored.",
                category=DeprecationWarning,
                stacklevel=3,
            )

    def biometric(self):
        # TODO: implement biometric options
        pass

    def options(
        self,
    ) -> dict[str, str | bool]:
        """
        Serialize AndroidOptions for Flutter Secure Storage.

        Returns:
            Mapping of option names expected by the Flutter Secure Storage plugin.
        """
        if self.encrypted_shared_preferences is None:
            self.encrypted_shared_preferences = False
        return {
            "encryptedSharedPreferences": parse_bool(self.encrypted_shared_preferences),
            "resetOnError": parse_bool(self.reset_on_error),
            "migrateOnAlgorithmChange": parse_bool(self.migrate_on_algorithm_change),
            "enforceBiometrics": parse_bool(self.enforce_biometrics),
            "keyCipherAlgorithm": parse_enum(
                self.key_cipher_algorithm, KeyCipherAlgorithm
            ),
            "storageCipherAlgorithm": parse_enum(
                self.storage_cipher_algorithm, StorageCipherAlgorithm
            ),
            "sharedPreferencesName": parse_str(self.shared_preferences_name),
            "preferencesKeyPrefix": parse_str(self.preferences_key_prefix),
            "biometricPromptTitle": parse_str(self.biometric_prompt_title),
            "biometricPromptSubtitle": parse_str(self.biometric_prompt_subtitle),
        }
