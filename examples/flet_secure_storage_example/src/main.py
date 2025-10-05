import flet as ft

import flet_secure_storage as fss


async def main(page: ft.Page):

    secure_storage = fss.SecureStorage()
    page.services.append(secure_storage)

    page.window.width = 400
    page.window.height = 600

    async def _set(_e: ft.Event[ft.Button]):
        # Sets the value in secure storage, Returns bool
        _clear_messages()
        if await secure_storage.set(key_field.value, value_field.value):
            message.value = (
                f"Set pair key:'{key_field.value}' with value:'{value_field.value}'"
            )
            _clear_fields()
        else:
            message.value = "Set Failed!"

    async def _get(_e: ft.Event[ft.Button]):
        # Gets the value based on the 'key', returns str
        _clear_messages()
        value_field.value = ""

        value = await secure_storage.get(key_field.value)
        message.value = f"Retrieved value for '{key_field.value}' is : {value}"

    async def _contains_key(_e: ft.Event[ft.Button]):
        # Checks if the key exists in secure storage, returns bool
        _clear_messages()
        value_field.value = ""

        exists = await secure_storage.contains_key(key_field.value)
        message.value = f"Key '{key_field.value}' exists: {exists}"

    async def _remove(_e: ft.Event[ft.Button]):
        # Removes the key-value pair from secure storage, returns bool
        _clear_messages()
        value_field.value = ""

        if await secure_storage.remove(key_field.value):
            message.value = f"Removed pair with key:'{key_field.value}'"
        else:
            message.value = "Remove Failed!"

        _clear_fields()

    async def _get_keys(_e: ft.Event[ft.Button]):
        # Retrieves all keys from secure storage, returns list[str]
        _clear_messages()
        pairs = await secure_storage.get_keys(key_field.value)
        message.value = f"Keys with prefix '{key_field.value}' are:"
        output_field.controls.extend(
            [
                ft.Text(f"{pair.split(':', 1)[0]}: {pair.split(':', 1)[1]}")
                for pair in pairs
            ]
        )

    async def _clear(_e: ft.Event[ft.Button]):
        # Clears all key-value pairs from secure storage, returns bool
        _clear_messages()
        if await secure_storage.clear():
            message.value = "Cleared all key-value pairs"
        else:
            message.value = "Clear Failed!"

    def _clear_messages():
        message.value = ""
        output_field.controls.clear()

    def _clear_fields():
        key_field.value = ""
        value_field.value = ""

    page.add(
        ft.Text("Secure Storage Example"),
        key_field := ft.TextField(label="Key", autofocus=True),
        value_field := ft.TextField(label="Value"),
        message := ft.Text(""),
        ft.Divider(),
        output_field := ft.Column(),
        ft.Button(content="Set Value", on_click=_set),
        ft.Button(content="Get Value", on_click=_get),
        ft.Button(content="Contains Key", on_click=_contains_key),
        ft.Button(content="Remove Value", on_click=_remove),
        ft.Button(content="Get Keys by Prefix", on_click=_get_keys),
        ft.Button(content="Clear Values", on_click=_clear),
    )


ft.run(main)
