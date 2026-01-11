from collections.abc import Mapping
from dataclasses import is_dataclass
from typing import Any, Optional, Protocol, cast, runtime_checkable

import flet as ft

from ._helpers import add_prefix
from .options import (
    AndroidOptions,
    IOSOptions,
    LinuxOptions,
    MacOsOptions,
    WebOptions,
    WindowsOptions,
)
from .options.android_options import KeyCipherAlgorithm, StorageCipherAlgorithm

__all__ = [
    "SecureStorage",
    "IOSOptions",
    "AndroidOptions",
    "LinuxOptions",
    "WindowsOptions",
    "WebOptions",
    "MacOsOptions",
    "KeyCipherAlgorithm",
    "StorageCipherAlgorithm",
]


class SecureStorageKeyError(ValueError):
    """
    Raised when an invalid key is provided to SecureStorage methods.
    """


@runtime_checkable
class HasOptions(Protocol):
    def options(self) -> Mapping[str, object]: ...


@ft.control("SecureStorage")  # type: ignore[arg-type]
class SecureStorage(ft.Service):
    """
    Create an instance of FlutterSecureStorage in Flet
    [FlutterSecureStorage - pub.dev](https://pub.dev/packages/flutter_secure_storage)
    [FlutterSecureStorage - GitHub](https://github.com/juliansteenbakker/flutter_secure_storage)

    The functions used are to mirror the Flet [client_storage](https://docs.flet.dev/cookbook/client-storage/) calls
    """

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
    ):
        # Normalize and validate prefix
        if prefix is None:
            # treat None as empty string
            self.prefix = ""
        elif not isinstance(prefix, str):
            raise TypeError(f"Prefix must be a string. Got {type(prefix)} instead.")
        else:
            self.prefix = prefix.strip()

        # Normalize and validate prefix_separator
        # If prefix is empty, separator should be empty regardless of input
        if self.prefix == "":
            self.prefix_separator = ""
        elif prefix_separator is None or prefix_separator == "":
            # treat None as empty string
            self.prefix_separator = ""
        elif not isinstance(prefix_separator, str):
            raise TypeError("prefix_separator must be a string or None.")
        else:
            self.prefix_separator = prefix_separator

        self.i_options = i_options if i_options is not None else IOSOptions()
        self.a_options = a_options if a_options is not None else AndroidOptions()
        self.l_options = l_options if l_options is not None else LinuxOptions()
        self.w_options = w_options if w_options is not None else WindowsOptions()
        self.web_options = web_options if web_options is not None else WebOptions()
        self.m_options = m_options if m_options is not None else MacOsOptions()

        super().__init__()

    def before_update(self) -> None:
        """
        Overrides the parent method. This is where we ensure the option
        dictionaries are correctly formatted for the client.

        Sets each platform options attribute to a dictionary, or raises TypeError
        if the attribute is not a dataclass with an options() method.
        """
        # super().before_update is not typed in flet; silence mypy for this call
        super().before_update()  # type: ignore[no-untyped-call]
        for platform_options in (
            "i_options",
            "a_options",
            "l_options",
            "w_options",
            "web_options",
            "m_options",
        ):
            opt = getattr(self, platform_options, None)
            if opt is None or isinstance(opt, Mapping):
                continue

            if not is_dataclass(opt) or isinstance(opt, type):
                raise SecureStorageKeyError(
                    f"{platform_options!r} must be a dataclass instance with an options() method."
                )

            if not isinstance(opt, HasOptions):
                raise SecureStorageKeyError(
                    f"{platform_options!r} must implement options() -> Mapping."
                )

            options_dict = opt.options()

            if not isinstance(options_dict, Mapping):
                raise SecureStorageKeyError(
                    f"{platform_options!r}.options() must return a dictionary-like object."
                )

            setattr(self, platform_options, options_dict)

    def _validate_key(self, key: str) -> None:
        if not isinstance(key, str):
            raise ValueError(f"Key must be a string. Got {type(key)} instead.")
        if key.strip() == "":
            raise ValueError("Key cannot be empty or whitespace.")

    async def set(self, key: str, value: Any) -> bool:
        """
        Sets a value in secure storage.
        From flutter_secure_storage: storage.write

        Args:
            key (str): key name, used to retrieve the value
            value (Any): value to store

        Returns:
            bool: True if the value was stored successfully, False otherwise
        """
        self._validate_key(key)
        key = add_prefix(self.prefix, self.prefix_separator, key)
        return cast(
            bool, await self._invoke_method("set", {"key": key, "value": value})
        )

    async def get(self, key: str) -> Optional[str]:
        """
        Retrieves a value from secure storage.
        From flutter_secure_storage: storage.read

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            Optional[str]: The value associated with the key as a string, or None if not found.
        """
        self._validate_key(key)
        key = add_prefix(self.prefix, self.prefix_separator, key)
        return cast(Optional[str], await self._invoke_method("get", {"key": key}))

    async def contains_key(self, key: str) -> bool:
        """
        Checks if a key exists in secure storage.
        From flutter_secure_storage: storage.containsKey

        Args:
            key (str): The key to check for existence.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        self._validate_key(key)
        key = add_prefix(self.prefix, self.prefix_separator, key)
        return cast(bool, await self._invoke_method("contains_key", {"key": key}))

    async def remove(self, key: str) -> bool:
        """
        Deletes a key from the secure storage.
        From flutter_secure_storage: storage.delete

        Args:
            key (str): The key to delete.

        Returns:
            bool: True if the key was deleted successfully, False otherwise.
        """
        self._validate_key(key)
        key = add_prefix(self.prefix, self.prefix_separator, key)
        return cast(bool, await self._invoke_method("remove", {"key": key}))

    async def get_keys(self, key_prefix: str = "") -> list[str]:
        """
        Retrieves all keys from secure storage.
        From flutter_secure_storage: storage.readAll

        Args:
            key_prefix (str): The prefix to filter keys by.

        Returns:
            list[str]: Returns a list of keys [<key_prefix>:<value>] of the values
                       that match the key_prefix or all keys if the user enters and
                       empty string or None
        """
        if key_prefix is None or key_prefix.strip() == "":
            key_prefix = self.prefix
        elif (
            key_prefix == self.prefix
            or key_prefix == f"{self.prefix}{self.prefix_separator}"
        ):
            key_prefix = self.prefix
        else:
            key_prefix = add_prefix(self.prefix, self.prefix_separator, key_prefix)

        response: dict[str, str] = cast(
            dict[str, str], await self._invoke_method("get_keys")
        )

        return [
            f"{key}:{value}"
            for key, value in response.items()
            if key.startswith(key_prefix)
        ]

    async def clear(self) -> bool:
        """
        Clears all data from secure storage.
        From flutter_secure_storage: storage.deleteAll

        Returns:
            bool: True if the storage was cleared successfully, False otherwise.
        """
        return cast(bool, await self._invoke_method("clear"))
