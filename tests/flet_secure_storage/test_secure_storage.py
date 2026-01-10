import pytest

from flet_secure_storage import SecureStorage
from flet_secure_storage.options import (
    AndroidOptions,
    IOSOptions,
    KeyCipherAlgorithm,
    StorageCipherAlgorithm,
)


@pytest.fixture
def secure_storage():
    svc = SecureStorage()

    storage: dict[str, str] = {}

    async def fake_invoke(name, args=None):
        if name == "set":
            assert args is not None
            storage[args["key"]] = args["value"]
            return True
        if name == "get":
            return storage.get(args["key"])
        if name == "contains_key":
            return args["key"] in storage
        if name == "remove":
            storage.pop(args["key"], None)
            return True
        if name == "get_keys":
            return storage.copy()
        if name == "clear":
            storage.clear()
            return True
        raise AssertionError(f"unexpected method: {name}")

    svc._invoke_method = fake_invoke
    return svc


@pytest.mark.asyncio
@pytest.mark.smoke
class TestSecureStorageErrorHandling:
    async def test_invalid_key_set(self, secure_storage):
        with pytest.raises(ValueError):
            await secure_storage.set("", "value")
        with pytest.raises(ValueError):
            await secure_storage.set(123, "value")

    async def test_invalid_key_get(self, secure_storage):
        with pytest.raises(ValueError):
            await secure_storage.get("")
        with pytest.raises(ValueError):
            await secure_storage.get(123)

    async def test_invalid_key_contains(self, secure_storage):
        with pytest.raises(ValueError):
            await secure_storage.contains_key("")
        with pytest.raises(ValueError):
            await secure_storage.contains_key(123)

    async def test_invalid_key_remove(self, secure_storage):
        with pytest.raises(ValueError):
            await secure_storage.remove("")
        with pytest.raises(ValueError):
            await secure_storage.remove(123)

    async def test_set_with_invalid_key_type(self, secure_storage):
        with pytest.raises(ValueError, match="Key must be a string"):
            await secure_storage.set(123, "value")  # type: ignore

    async def test_set_with_empty_key(self, secure_storage):
        with pytest.raises(ValueError, match="Key cannot be empty"):
            await secure_storage.set("", "value")

    async def test_set_with_whitespace_key(self, secure_storage):
        with pytest.raises(ValueError, match="Key cannot be empty"):
            await secure_storage.set("   ", "value")

    async def test_get_with_invalid_key(self, secure_storage):
        with pytest.raises(ValueError, match="Key must be a string"):
            await secure_storage.get(None)  # type: ignore


@pytest.mark.asyncio
@pytest.mark.smoke
class TestSecureStorage:
    #
    # set method tests
    #
    async def test_set(self, secure_storage):
        assert await secure_storage.set("key1", "value1") is True
        assert await secure_storage.set("key2 ", "value2") is True
        assert await secure_storage.set("  key3", "value3    ") is True
        assert await secure_storage.set("key4", " value4 ") is True

    #
    # get method tests
    #
    async def test_get(self, secure_storage):
        assert await secure_storage.set("key1", "value1") is True

        assert await secure_storage.get("key1") == "value1"

    #
    # contains_key method tests
    #
    async def test_contains(self, secure_storage):
        assert await secure_storage.set("key1", "value1") is True

        assert await secure_storage.contains_key("key1") is True

    #
    # remove method tests
    #
    async def test_remove(self, secure_storage):
        # Adding values to check
        assert await secure_storage.set("key1", "value1") is True

        # Removing values
        assert await secure_storage.remove("key1") is True

    #
    # get_keys method tests
    #
    async def test_get_keys(self, secure_storage):
        assert await secure_storage.set("key1", "value1") is True

        prefix = "key"

        assert await secure_storage.get_keys(prefix) == ["key1:value1"]

    #
    # clear method tests
    #
    async def test_clear(self, secure_storage):
        assert await secure_storage.set("key1", "value1") is True

        assert await secure_storage.clear() is True
        assert await secure_storage.contains_key("key") is False


# Options Tests
@pytest.mark.smoke
def test_android_options_defaults():
    opts = AndroidOptions()
    result = opts.options()

    assert result["resetOnError"] is True
    assert result["migrateOnAlgorithmChange"] is True
    assert result["enforceBiometrics"] is False


@pytest.mark.smoke
def test_android_options_custom():
    opts = AndroidOptions(
        reset_on_error=False,
        shared_preferences_name="my_app",
        key_cipher_algorithm=KeyCipherAlgorithm.RSA_ECB_PKCS1Padding,
    )
    result = opts.options()

    assert result["resetOnError"] is False
    assert result["sharedPreferencesName"] == "my_app"


@pytest.mark.smoke
def test_ios_options_defaults():
    opts = IOSOptions()
    result = opts.options()

    assert result["accountName"] == "flet_secure_storage_service"
    assert result["synchronizable"] is False
