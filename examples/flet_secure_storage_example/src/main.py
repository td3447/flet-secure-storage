import flet as ft

import flet_secure_storage as fss


def main(page: ft.Page):

    secure_storage = fss.SecureStorage()
    page.services.append(secure_storage)

    async def _set(_e: ft.Event[ft.Button]):
        # Sets the value in secure storage, Returns bool
        if await secure_storage.set(key_field.value, value_field.value):
            message.value = (
                f"Set pair key:'{key_field.value}' with value:'{value_field.value}'"
            )
        else:
            message.value = "Set Failed!"

    async def _get(_e: ft.Event[ft.Button]):
        # Gets the value based on the 'key', returns str
        value = await secure_storage.get(key_field.value)
        message.value = f"Retrieved value for '{key_field.value}' is : {value}"

    async def _contains_key(_e: ft.Event[ft.Button]):
        # Checks if the key exists in secure storage, returns bool
        exists = await secure_storage.contains_key(key_field.value)
        message.value = f"Key '{key_field.value}' exists: {exists}"

    async def _remove(_e: ft.Event[ft.Button]):
        # Removes the key-value pair from secure storage, returns bool
        if await secure_storage.remove(key_field.value):
            message.value = f"Removed pair with key:'{key_field.value}'"
        else:
            message.value = "Remove Failed!"

    async def _get_keys(_e: ft.Event[ft.Button]):
        # Retrieves all keys from secure storage, returns list[str]
        output.controls.clear()
        pairs = await secure_storage.get_keys(key_field.value)
        message.value = f"Keys with prefix '{key_field.value}' are:"
        output.controls.extend(
            [
                ft.Text(f"{pair.split(':', 1)[0]}: {pair.split(':', 1)[1]}")
                for pair in pairs
            ]
        )

    async def _clear(_e: ft.Event[ft.Button]):
        # Clears all key-value pairs from secure storage, returns bool
        if await secure_storage.clear():
            message.value = "Cleared all key-value pairs"
        else:
            message.value = "Clear Failed!"

    page.add(
        ft.Text("Secure Storage Example"),
        ft.ResponsiveRow(
            controls=[
                ft.Column(
                    controls=[
                        key_field := ft.TextField(label="Key"),
                        value_field := ft.TextField(label="Value"),
                        message := ft.Text(""),
                    ],
                    expand=1,
                ),
                ft.Column(
                    controls=[output := ft.Column()],
                    expand=1,
                ),
            ]
        ),
        ft.ResponsiveRow(
            controls=[
                ft.Button(content="Set Value", width=150, on_click=_set),
                ft.Button("Get Value", on_click=_get),
                ft.Button("Contains Key", on_click=_contains_key),
                ft.Button("Remove Value", on_click=_remove),
                ft.Button("Get Keys by Prefix", on_click=_get_keys),
                ft.Button("Clear Values", on_click=_clear),
            ],
        ),
    )


ft.run(main)
