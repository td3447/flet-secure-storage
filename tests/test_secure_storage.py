import pytest

import flet_secure_storage.secure_storage as fss


@pytest.fixture
def secure_storage():
    svc = fss.SecureStorage()

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


test_data = [
    ("sample_key_1", "sample_value_1"),
    ("sample_key_2", "sample_value_2"),
    ("sample_key_3", "sample_value_3"),
]

test_prefix = "sample_"


@pytest.mark.asyncio
@pytest.mark.smoke
class TestSecureStorage:
    #
    # set method tests
    #
    @pytest.mark.parametrize("key,value", test_data)
    async def test_set(self, secure_storage, key, value):
        assert await secure_storage.set(key, value) is True

    #
    # get method tests
    #
    @pytest.mark.parametrize("key,value", test_data)
    async def test_get(self, secure_storage, key, value):
        await secure_storage.set(key, value)
        assert await secure_storage.get(key) == value

    #
    # contains_key method tests
    #
    @pytest.mark.parametrize("key,value", test_data)
    async def test_contains(self, secure_storage, key, value):
        await secure_storage.set(key, value)
        assert await secure_storage.contains_key(key) is True

    #
    # remove method tests
    #
    @pytest.mark.parametrize("key,value", test_data)
    async def test_remove(self, secure_storage, key, value):
        await secure_storage.set(key, value)
        assert await secure_storage.remove(key) is True
        assert await secure_storage.contains_key(key) is False

    #
    # get_keys method tests
    #
    @pytest.mark.parametrize("key,value", test_data)
    async def test_get_keys(self, secure_storage, key, value, prefix=test_prefix):
        await secure_storage.set(key, value)
        assert await secure_storage.get_keys(prefix) == [f"{key}:{value}"]

    #
    # clear method tests
    #
    @pytest.mark.parametrize("key,value", test_data)
    async def test_clear(self, secure_storage, key, value):
        await secure_storage.set(key, value)
        assert await secure_storage.clear() is True
        assert await secure_storage.contains_key("") is False
