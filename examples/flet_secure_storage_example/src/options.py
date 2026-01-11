"""
options.py: Defines various platform-specific options for secure storage.

Not all options are required, the listed options are the defaults. So you can also
    just create an instance of the options class without any parameters. e.g. IOSOptions()

Returns:
    Platform-specific options instances for iOS, Android, Linux, Windows, Web, and MacOS.
"""

from flet_secure_storage import (
    AccessControlFlag,
    AndroidOptions,
    IOSOptions,
    KeychainAccessibility,
    KeyCipherAlgorithm,
    LinuxOptions,
    MacOsOptions,
    StorageCipherAlgorithm,
    WebOptions,
    WindowsOptions,
)


def i_opts() -> IOSOptions:
    return IOSOptions(
        account_name="flet_secure_storage_service",
        group_id="",
        accessibility=KeychainAccessibility.unlocked,
        synchronizable=False,
        label="",
        description="",
        comment="",
        is_invisible=None,
        is_negative=None,
        creation_date=None,
        last_modified_date=None,
        result_limit=None,
        should_return_persistent_reference=None,
        authentication_ui_behavior="",
        access_control_flags=[],
        # use_secure_enclave=False,
    )


def a_opts():
    return AndroidOptions(
        # encrypted_shared_preferences=False, # Deprecated
        reset_on_error=True,
        migrate_on_algorithm_change=True,
        enforce_biometrics=False,
        key_cipher_algorithm=KeyCipherAlgorithm.RSA_ECB_OAEPwithSHA_256andMGF1Padding,
        storage_cipher_algorithm=StorageCipherAlgorithm.AES_GCM_NoPadding,
        shared_preferences_name="",
        preferences_key_prefix="",
        biometric_prompt_title="Authenticate to access",
        biometric_prompt_subtitle="Use biometrics or device credentials",
    )


def l_opts():
    return LinuxOptions()


def w_opts():
    return WindowsOptions(use_backward_compatibility=False)


def web_opts():
    return WebOptions(
        db_name="FletEncryptedStorage",
        public_key="FletSecureStorage",
        wrap_key="",
        wrap_key_iv="",
        use_session_storage=False,
    )


def m_opts():
    return MacOsOptions(
        account_name="flet_secure_storage_service",
        group_id="",
        accessibility=KeychainAccessibility.unlocked,
        synchronizable=False,
        label="",
        description="",
        comment="",
        is_invisible=None,
        is_negative=None,
        creation_date=None,
        last_modified_date=None,
        result_limit=None,
        should_return_persistent_reference=None,
        authentication_ui_behavior="",
        access_control_flags=[],
        # use_secure_enclave=False,
        uses_data_protection_keychain=True,  # this is macOS specific
    )
