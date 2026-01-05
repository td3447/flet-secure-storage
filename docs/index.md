# Introduction

A [Flet](https://flet.dev/) extension using [flutter_secure_storage](https://pub.dev/packages/flutter_secure_storage).

## Installation
    
Install with pip:
```bash
pip install flet-secure-storage
```

or with uv:
```bash
uv add flet-secure-storage
```

## Quick Start

### Initialize
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

### Initialize with Options
- Add secure_storage to the page services.

```python
import flet as ft
from flet_secure_storage import SecureStorage, AndroidOptions

async def main(page: ft.Page):
    secure_storage = SecureStorage(
        a_options=AndroidOptions(
            shared_preferences_name="my_project",
            preferences_key_prefix="com.project"
        )
    ) # Create an instance of secure_storage
    page.services.append(secure_storage) # Add secure_storage to services

    # Code

ft.run(main)
```

## API Reference

:::flet_secure_storage.SecureStorage
