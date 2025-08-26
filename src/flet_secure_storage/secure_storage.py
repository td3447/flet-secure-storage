from typing import Any, Optional

from flet.controls.base_control import control
from flet.controls.services.service import Service

__all__ = ["SecureStorage"]


@control("SecureStorage")
class SecureStorage(Service):
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

    # TODO: shared_preferences -> storage.getKeys
    # async def get_keys(self, key_prefix: str) -> list[str]:
    #     """_summary_

    #     Args:
    #         key_prefix (str): _description_

    #     Returns:
    #         list[str]: _description_
    #     """
    #     return await self._invoke_method("get_keys", {"key_prefix": key_prefix})

    async def clear(self) -> bool:
        """
        Clears all data from secure storage.
        From flutter_secure_storage: storage.deleteAll

        Returns:
            bool: True if the storage was cleared successfully, False otherwise.
        """
        return await self._invoke_method("clear")
