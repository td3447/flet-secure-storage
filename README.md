# flet-secure-storage
<!--intro-start-->
[![pypi](https://img.shields.io/pypi/v/flet-secure-storage.svg)](https://pypi.python.org/pypi/flet-secure-storage)
[![license](https://img.shields.io/github/license/td3447/flet-secure-storage.svg)](https://github.com/td3447/flet-secure-storage/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flet-secure-storage)](https://pypi.python.org/pypi/flet-secure-storage)

[![Requires Flet >=0.80.0.dev0](https://img.shields.io/badge/Flet-%3E%3D0.80.0-blue)](https://pypi.org/project/flet/0.80.0/)


An encrypted storage option for [Flet](https://flet.dev) that stores data securely, based on the platform, it is designed to be similiar to the SharedPreferences (previously ClientStorage) class in Flet v1.

It utilizes the [flutter_secure_storage](https://pub.dev/packages/flutter_secure_storage) Flutter package
<!--intro-end-->
## Documentation

[Link to documentation](https://td3447.github.io/flet-secure-storage/)
<!--docs-start-->
## Platform Support
<!-- https://emojipedia.org/ ✅⚠️🚧❌-->
| Platform   | Supported |
|------------|:---------:|
| Windows    | ✅       |
| Android    | ✅       |
| Web        | ✅       |
| Linux      | ✅       |
| macOS      | 🚧       |
| iOS        | 🚧       |

ℹ️ **Note:** Currently unable to verify on macOS or iOS.

## Flet Compatibility

| Version     | Supported |
|-------------|:---------:|
| >= 0.80.0   | ✅       |
| < 0.28.3    | ❌       |

## Usage

### Installation

To install the `flet-secure-storage` package and add it to your project dependencies:

- Using `uv`:
    ```bash
    uv add flet-secure-storage
    ```

- Using `pip`:
    ```bash
    pip install flet-secure-storage
    ```
    After this, you will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

    ```toml
    [project]
    dependencies = [
        "flet-secure-storage",
        "flet>=0.80.0",
    ]
    ```

### Basic Usage

#### Initialize
- Add secure_storage to the page services.

    ```python
    import flet as ft
    from flet_secure_storage import SecureStorage

    async def main(page: ft.Page):
        secure_storage = SecureStorage() # Create an instance of secure_storage
        page.services.append(secure_storage) # Add secure_storage to services

        # Code

    ft.run(main)
    ```

#### Initialize with Options
- Add secure_storage to the page services.

    ```python
    import flet as ft
    from flet_secure_storage import SecureStorage, AndroidOptions

    async def main(page: ft.Page):
        secure_storage = SecureStorage(
            prefix="com.example", # `.` is added automatically between prefix and key
            prefix_separator=".", # Default
            a_options=AndroidOptions(
                shared_preferences_name="my_project",
                preferences_key_prefix="com.project"
            )
            # Add other platform options
        ) # Create an instance of secure_storage
        page.services.append(secure_storage) # Add secure_storage to services

        # Code

    ft.run(main)
    ```

#### Functions

- **set** - Set a value by key in storage

    ```python
    await secure_storage.set("key", "value")

    return bool
    ```

- **get** - Retrieve a value from storage by it's key

    ```python
    value = await secure_storage.get("key")

    return value: str
    ```

- **contains_key** - Check if a key exists in storage by it's key

    ```python
    await secure_storage.contains_key("key"):
        
    return bool
    ```

- **remove** - Removes the key, value pair from storage

    ```python
    await secure_storage.remove("key")

    return bool
    ```

- **get_keys** - Gets all keys that startwith the entered key. Returns all keys if blank.

    ```python
    values = await secure_storage.get_keys("key": str = "")
    # No entry or an entry of '' will produce keys starting with the `prefix=` option.

    return values: list[str]

    # input key = "key"
    # return ['key1:value1', 'key2:value2']
    ```

- **clear** - Clears **all** keys from storage.

    ```python
    await secure_storage.remove("key")
    ```
<!--docs-end-->

### Documentation

To get a more through explanation, check out the [documentation](https://td3447.github.io/flet-secure-storage/).
