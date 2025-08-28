from typing import Any, Optional

import flet as ft

__all__ = ["SecureStorage"]


@ft.control("SecureStorage")
class SecureStorage(ft.Service):
    """
    Create an instance of FlutterSecureStorage in Flet
    https://pub.dev/packages/flutter_secure_storage
    https://github.com/juliansteenbakker/flutter_secure_storage

    The functions used are to mirror the client_storage calls
    https://flet.dev/docs/cookbook/client-storage/
    """

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
        assert value is not None
        return await self._invoke_method("set", {"key": key, "value": value})

    async def get(self, key: str) -> Optional[str]:
        """
        Retrieves a value from secure storage.
        From flutter_secure_storage: storage.read

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            Optional[str]: The value associated with the key as a string, or None if not found.
        """
        return await self._invoke_method("get", {"key": key})

    async def contains_key(self, key: str) -> bool:
        """
        Checks if a key exists in secure storage.
        From flutter_secure_storage: storage.containsKey

        Args:
            key (str): The key to check for existence.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return await self._invoke_method("contains_key", {"key": key})

    async def remove(self, key: str) -> bool:
        """
        Deletes a key from the secure storage.
        From flutter_secure_storage: storage.delete

        Args:
            key (str): The key to delete.

        Returns:
            bool: True if the key was deleted successfully, False otherwise.
        """
        return await self._invoke_method("remove", {"key": key})

    async def get_keys(self, key_prefix: Optional[str]) -> list[str]:
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
        key_prefix = key_prefix or ""
        response: dict[str, str] = await self._invoke_method("get_keys")

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
        return await self._invoke_method("clear")
