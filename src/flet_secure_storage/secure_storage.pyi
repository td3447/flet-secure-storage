from typing import Any

import flet as ft

from .options import (
    AndroidOptions,
    IOSOptions,
    LinuxOptions,
    MacOsOptions,
    WebOptions,
    WindowsOptions,
)

class SecureStorageKeyError(ValueError): ...

class SecureStorage(ft.Service):
    prefix: str | None
    prefix_separator: str | None
    i_options: IOSOptions | None
    a_options: AndroidOptions | None
    l_options: LinuxOptions | None
    w_options: WindowsOptions | None
    web_options: WebOptions | None
    m_options: MacOsOptions | None
    def __init__(
        self,
        prefix: str | None = None,
        prefix_separator: str | None = ".",
        i_options: IOSOptions | None = None,
        a_options: AndroidOptions | None = None,
        l_options: LinuxOptions | None = None,
        w_options: WindowsOptions | None = None,
        web_options: WebOptions | None = None,
        m_options: MacOsOptions | None = None,
    ) -> None: ...
    async def set(self, key: str, value: Any) -> bool: ...
    async def get(self, key: str) -> str | None: ...
    async def contains_key(self, key: str) -> bool: ...
    async def remove(self, key: str) -> bool: ...
    async def get_keys(self, key_prefix: str = ...) -> list[str]: ...
    async def clear(self) -> bool: ...
