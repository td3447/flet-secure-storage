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

```python
import flet as ft

import flet_secure_storage as fss


def main(page: ft.Page):

    secure_storage = fss.SecureStorage() # Create an instance of secure_storage
    page.services.append(secure_storage) # Add secure_storage to services

    # API Calls here

    page.add(
        ft.Text("Quick Start")
    )

ft.run(main)
```

## API Reference


### Classes

#### **SecureStorage**

    ```python
    import flet_secure_storage as fss


    secure_storage = fss.SecureStorage() # Create an instance of secure_storage
    page.services.append(secure_storage) # Add secure_storage to services
    ```


### Functions

#### **set**

```python
await secure_storage.set("key", "value")
```

- Input: 
    * key   -> String
    * value -> String
- Output:
    * bool

---
#### **get**

```python
await secure_storage.get("key")
```

- Input: 
    * key   -> String
- Output:
    * value -> String

---
#### **contains_key**

```python
await secure_storage.set("key")
```

- Input: 
    * key   -> String
- Output:
    * bool

---
#### **remove**

```python
await secure_storage.remove("key")
```

- Input: 
    * key   -> String
- Output:
    * bool

---
#### **get_keys**

```python
await secure_storage.get_keys("key")
```

- Input: 
    * key   -> String or None
- Output:
    * list  -> String

---
#### **clear**

```python
await secure_storage.remove("key")
```

- Input: 
    * key   -> String
- Output:
    * bool

---