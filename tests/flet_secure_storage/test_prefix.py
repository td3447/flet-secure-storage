import pytest

from flet_secure_storage import SecureStorage


@pytest.mark.asyncio
@pytest.mark.smoke
class TestPrefixAndSeparator:
    """Test prefix and prefix_separator behavior"""

    async def test_empty_prefix_ignores_separator(self):
        """When prefix is empty, separator should not be appended"""
        svc = SecureStorage(prefix="", prefix_separator=".")

        storage: dict[str, str] = {}

        async def fake_invoke(name, args=None):
            if name == "set":
                storage[args["key"]] = args["value"]
                return True
            if name == "get":
                return storage.get(args["key"])
            raise AssertionError(f"unexpected method: {name}")

        svc._invoke_method = fake_invoke

        # Should store as "key" not ".key"
        await svc.set("key", "value")
        assert "key" in storage
        assert ".key" not in storage

        # Should retrieve correctly
        result = await svc.get("key")
        assert result == "value"

    async def test_none_prefix_ignores_separator(self):
        """When prefix is None, separator should not be appended"""
        svc = SecureStorage(prefix=None, prefix_separator=".")

        storage: dict[str, str] = {}

        async def fake_invoke(name, args=None):
            if name == "set":
                storage[args["key"]] = args["value"]
                return True
            raise AssertionError(f"unexpected method: {name}")

        svc._invoke_method = fake_invoke

        await svc.set("key", "value")
        assert "key" in storage
        assert ".key" not in storage

    async def test_whitespace_prefix_ignores_separator(self):
        """When prefix is whitespace only, separator should not be appended"""
        svc = SecureStorage(prefix="   ", prefix_separator=".")

        storage: dict[str, str] = {}

        async def fake_invoke(name, args=None):
            if name == "set":
                storage[args["key"]] = args["value"]
                return True
            raise AssertionError(f"unexpected method: {name}")

        svc._invoke_method = fake_invoke

        await svc.set("key", "value")
        assert "key" in storage
        assert ".key" not in storage

    async def test_valid_prefix_with_separator(self):
        """When prefix is valid, separator should be used"""
        svc = SecureStorage(prefix="app", prefix_separator=".")

        storage: dict[str, str] = {}

        async def fake_invoke(name, args=None):
            if name == "set":
                storage[args["key"]] = args["value"]
                return True
            if name == "get":
                return storage.get(args["key"])
            raise AssertionError(f"unexpected method: {name}")

        svc._invoke_method = fake_invoke

        await svc.set("key", "value")
        assert "app.key" in storage
        assert "key" not in storage

        result = await svc.get("key")
        assert result == "value"

    async def test_valid_prefix_no_separator(self):
        """When prefix is valid but separator is empty"""
        svc = SecureStorage(prefix="app", prefix_separator="")

        storage: dict[str, str] = {}

        async def fake_invoke(name, args=None):
            if name == "set":
                storage[args["key"]] = args["value"]
                return True
            raise AssertionError(f"unexpected method: {name}")

        svc._invoke_method = fake_invoke

        await svc.set("key", "value")
        assert "appkey" in storage

    async def test_custom_separator(self):
        """Test custom separator character"""
        svc = SecureStorage(prefix="myapp", prefix_separator="_")

        storage: dict[str, str] = {}

        async def fake_invoke(name, args=None):
            if name == "set":
                storage[args["key"]] = args["value"]
                return True
            raise AssertionError(f"unexpected method: {name}")

        svc._invoke_method = fake_invoke

        await svc.set("key", "value")
        assert "myapp_key" in storage
