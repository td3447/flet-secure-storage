from dataclasses import dataclass
from enum import Enum, unique

@unique
class KeyCipherAlgorithm(Enum):
    RSA_ECB_PKCS1Padding = "RSA_ECB_PKCS1Padding"
    RSA_ECB_OAEPwithSHA_256andMGF1Padding = "RSA_ECB_OAEPwithSHA_256andMGF1Padding"
    AES_GCM_NoPadding = "AES_GCM_NoPadding"

@unique
class StorageCipherAlgorithm(Enum):
    AES_CBC_PKCS7Padding = "AES_CBC_PKCS7Padding"
    AES_GCM_NoPadding = "AES_GCM_NoPadding"

@dataclass
class AndroidOptions:
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

    @classmethod
    def biometric(
        cls,
        encrypted_shared_preferences: bool = False,
        reset_on_error: bool = True,
        migrate_on_algorithm_change: bool = True,
        enforce_biometrics: bool = False,
        shared_preferences_name: str = "",
        preferences_key_prefix: str = "",
        biometric_prompt_title: str = "Authenticate to access",
        biometric_prompt_subtitle: str = "Use biometrics or device credentials",
    ) -> "AndroidOptions": ...
