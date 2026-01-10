"""
Flet Secure Storage Example

Refactored Secure Storage Example using flet_secure_storage extension.

Using Flet 0.80.0

"""

import flet as ft

import flet_secure_storage as fss
from flet_secure_storage.options import (
    AndroidOptions,
    IOSOptions,
    KeyCipherAlgorithm,
    LinuxOptions,
    MacOsOptions,
    StorageCipherAlgorithm,
    WebOptions,
    WindowsOptions,
)


async def main(page: ft.Page):

    secure_storage = fss.SecureStorage(
        prefix="net.example",
        i_options=IOSOptions(),
        l_options=LinuxOptions(),
        m_options=MacOsOptions(),
        w_options=WindowsOptions(use_backward_compatibility=False),
        web_options=WebOptions(
            db_name="FletEncryptedStorage",
            public_key="FletSecureStorage",
            wrap_key="",
            wrap_key_iv="",
            use_session_storage=False,
        ),
        a_options=AndroidOptions(
            # encrypted_shared_preferences=False, # Deprecated
            reset_on_error=True,
            migrate_on_algorithm_change=True,
            enforce_biometrics=False,
            key_cipher_algorithm=(
                KeyCipherAlgorithm.RSA_ECB_OAEPwithSHA_256andMGF1Padding
            ),
            storage_cipher_algorithm=(StorageCipherAlgorithm.AES_GCM_NoPadding),
            shared_preferences_name="",
            preferences_key_prefix="",
            biometric_prompt_title="Authenticate to access",
            biometric_prompt_subtitle="Use biometrics or device credentials",
        ),
    )
    page.services.append(secure_storage)

    page.window.width = 400
    page.window.height = 600

    async def _set(_e: ft.Event[ft.Button]) -> None:
        # Sets the value in secure storage, Returns bool
        _clear_messages()
        if await secure_storage.set(key_field.value, value_field.value):
            message.value = (
                f"Set pair key:'{key_field.value}' with value:'{value_field.value}'"
            )
            _clear_fields()
        else:
            message.value = "Set Failed!"
        page.update()

    async def _get(_e: ft.Event[ft.Button]) -> None:
        # Gets the value based on the 'key', returns str
        _clear_messages()
        value_field.value = ""

        value = await secure_storage.get(key_field.value)
        message.value = f"Retrieved value for '{key_field.value}' is : {value}"
        page.update()

    async def _contains_key(_e: ft.Event[ft.Button]) -> None:
        # Checks if the key exists in secure storage, returns bool
        _clear_messages()
        value_field.value = ""

        exists = await secure_storage.contains_key(key_field.value)
        message.value = f"Key '{key_field.value}' exists: {exists}"
        page.update()

    async def _remove(_e: ft.Event[ft.Button]) -> None:
        # Removes the key-value pair from secure storage, returns bool
        _clear_messages()
        value_field.value = ""

        if await secure_storage.remove(key_field.value):
            message.value = f"Removed pair with key:'{key_field.value}'"
        else:
            message.value = "Remove Failed!"

        _clear_fields()
        page.update()

    async def _get_keys(_e: ft.Event[ft.Button]) -> None:
        # Retrieves all keys from secure storage, returns list[str]
        _clear_messages()
        pairs = await secure_storage.get_keys(key_field.value)
        message.value = f"Keys with prefix '{key_field.value}' are:"
        output_field.controls.extend(
            [
                ft.Text(value=f"{pair.split(':', 1)[0]}: {pair.split(':', 1)[1]}")
                for pair in pairs
            ]
        )
        page.update()

    async def _clear(_e: ft.Event[ft.Button]) -> None:
        # Clears all key-value pairs from secure storage, returns bool
        _clear_messages()
        _clear_fields()
        if await secure_storage.clear():
            message.value = "Cleared all key-value pairs"
        else:
            message.value = "Clear Failed!"
        page.update()

    def _clear_messages() -> None:
        message.value = ""
        output_field.controls.clear()

    def _clear_fields() -> None:
        key_field.value = ""
        value_field.value = ""

    page.add(
        ft.Text(value="Flet Secure Storage Example"),
        key_field := ft.TextField(label="Key", autofocus=True),
        value_field := ft.TextField(label="Value"),
        message := ft.Text(value=""),
        ft.Divider(),
        output_field := ft.Column(),
        ft.Column(
            controls=[
                ft.Button(content="Set Value", on_click=_set),
                ft.Button(content="Get Value", on_click=_get),
                ft.Button(content="Contains Key", on_click=_contains_key),
                ft.Button(content="Remove Value", on_click=_remove),
                ft.Button(content="Get Keys by Prefix", on_click=_get_keys),
                ft.Button(content="Clear Values", on_click=_clear),
            ],
        ),
    )


ft.run(main)
