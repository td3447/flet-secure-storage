# flet-secure-storage

[![pypi](https://img.shields.io/pypi/v/flet-secure-storage.svg)](https://pypi.python.org/pypi/flet-secure-storage)
[![downloads](https://static.pepy.tech/badge/flet-secure-storage/month)](https://pepy.tech/project/flet-secure-storage)
[![license](https://img.shields.io/github/license/td3447/flet-secure-storage.svg)](https://github.com/td3447/flet-secure-storage/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flet-secure-storage)](https://pypi.python.org/pypi/flet-secure-storage)

[![Requires Flet >=0.70.0.dev0](https://img.shields.io/badge/Flet-%3E%3D0.70.0.dev0-blue)](https://pypi.org/project/flet/#history)


An encrypted storage options for [Flet](https://flet.dev) that stores data securely, based on the platform, it is designed to be similiar to the SharedPreferences (previously ClientStorage) class in Flet v1.

It utilizes the [flutter_secure_storage](https://pub.dev/packages/flutter_secure_storage) Flutter package

## Documentation

[Link to documentation](https://github.com/td3447/flet-secure-storage/)

## Platform Support
<!-- https://emojipedia.org/ -->
| Platform   | Supported      |
|------------|:-------------:|
| Windows    | ✅            |
| macOS      | 🚧            |
| Linux      | 🚧            |
| Android    | 🚧            |
| iOS        | 🚧            |
| Web        | 🚧            |

## Flet Compatibility

| Version       | Supported   |
|---------------|:-----------:|
| > 0.70.0.dev0 | ✅         |
| < 0.28.3      | ❌         |

## Usage

### Installation

To install the `flet-permission-handler` package and add it to your project dependencies:

- Using `uv`:
    ```bash
    uv add flet-permission-handler
    ```

- Using `pip`:
    ```bash
    pip install flet-permission-handler
    ```
    After this, you will have to manually add this package to your `requirements.txt` or `pyproject.toml`.

    ```toml
    [project]
    dependencies = [
        "flet-secure-storage",
        "flet>=0.28.3",
    ]
    ```

### Examples

To see how to use the example go [here](examples/flet_secure_storage_example/README.md)
