from enum import Enum

import pytest

from flet_secure_storage._helpers import parse_bool, parse_enum, parse_str


@pytest.mark.smoke
def test_parse_str():
    assert parse_str("  hello ") == "hello"
    assert parse_str("world") == "world"
    assert parse_str("TEST ") == "TEST"
    assert parse_str(" TEsT2 ") == "TEsT2"
    with pytest.raises(TypeError):
        parse_str(123)  # type: ignore
    with pytest.raises(TypeError):
        parse_str(True)  # type: ignore


@pytest.mark.smoke
def test_parse_bool():
    assert parse_bool(True) is True
    assert parse_bool(False) is False
    assert parse_bool(" true ") is True
    assert parse_bool("FALSE") is False
    assert parse_bool("1") is True
    assert parse_bool("0") is False
    assert parse_bool("yes") is True
    assert parse_bool("0") is False
    with pytest.raises(ValueError):
        parse_bool("ye")
    with pytest.raises(ValueError):
        parse_bool("3")
    with pytest.raises(TypeError):
        parse_bool(123)  # type: ignore


@pytest.mark.smoke
def test_parse_enum():
    class Shape(Enum):
        CIRCLE = "circle"
        SQUARE = "square"
        TRIANGLE = "triangle"

    class Color(Enum):
        RED = "red"
        GREEN = "green"
        BLUE = "blue"

    assert parse_enum(Color.RED, Color) == "RED"
    assert parse_enum("GREEN", Color) == "GREEN"
    with pytest.raises(ValueError):
        parse_enum("YELLOW", Color)
    with pytest.raises(TypeError):
        parse_enum(123, Color)  # type: ignore
    with pytest.raises(TypeError):
        parse_enum(Color.RED, Shape)
