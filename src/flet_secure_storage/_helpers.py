from datetime import datetime
from enum import Enum

_TRUE_STRINGS = {"true", "t", "1", "y", "yes"}
_FALSE_STRINGS = {"false", "f", "0", "n", "no"}


def parse_str(val: str) -> str:
    """
    Helper method to parse input string values,
        and return their stripped string representation.

    Args:
        val (str): The string value.

    Raises:
        TypeError: If val is not a `str`
    """
    if isinstance(val, str):
        return val.strip()
    raise TypeError(f"Input 'val' must be str, got type: {type(val).__name__} instead.")


def parse_bool(val: bool | str | None) -> bool | None:
    """
    Helper method to parse input boolean values as a bool or str,
        and return their boolean representation.

    Args:
        val (bool | str | None): The boolean value or its string representation.
            None if not provided.

    Raises:
        ValueError: If `val` is a string but not a valid boolean representation
        TypeError: If `val` is neither a bool nor a valid string representation

    Returns:
        bool | None: The boolean representation of the input value. None if input is not provided.
    """
    if val is None:
        return None

    if isinstance(val, bool):
        return val

    if isinstance(val, str):
        val_lower = val.lower().strip()
        if val_lower in _TRUE_STRINGS:
            return True
        elif val_lower in _FALSE_STRINGS:
            return False
        else:
            allowed = ", ".join(
                sorted([f"'{s}'" for s in _TRUE_STRINGS | _FALSE_STRINGS])
            )
            raise ValueError(
                f"Invalid string for boolean: {val!r}. "
                f"Expected one of: {allowed}. "
                "Or use a boolean value directly. (preferred)"
            )

    raise TypeError(
        f"Input 'val' must be bool or str, got type: {type(val).__name__} instead."
    )


def parse_enum(enum_val: Enum | str, enum_type: type[Enum]) -> str:
    """
    Helper method to parse input enum values as a string or Enum,
        and return their string Enum.name.

    Args:
        enum_val (Enum | str): The enum value or its string representation.
        enum_type (type[Enum]): The Enum type to validate against.

    Raises:
        TypeError: If `enum_type` is not an Enum type
        ValueError: If `enum_val` is a string but not a valid representation of `enum_type`
        TypeError: If `enum_val` is neither an instance of `enum_type` nor
            a valid string representation

    Returns:
        str: The string representation of the enum value.
    """
    if not (isinstance(enum_type, type) and issubclass(enum_type, Enum)):
        raise TypeError("enum_type must be an Enum type.")

    if isinstance(enum_val, enum_type):
        return enum_val.name

    if isinstance(enum_val, str):
        try:
            return enum_type[enum_val].name
        except KeyError as exc:
            raise ValueError(
                f"Invalid string for {enum_type.__name__}: {enum_val!r}"
            ) from exc

    raise TypeError(
        f"`enum_val` must be {enum_type.__name__}, got {type(enum_val).__name__}"
    )


def parse_dt(val: datetime | str | None) -> str | None:
    """
    Checks for datetime or string input as ISO 8601 format, and returns the value as a string.

    Args:
        val (datetime | str | None): The datetime value or its string representation.
            None if not provided.

    Raises:
        ValueError: If `val` is a string but not in ISO 8601 format
        TypeError: If `val` is neither a datetime nor a valid string representation

    Returns:
        str | None: The ISO 8601 string representation of the datetime value. None if not provided.
    """
    if val is None or val == "":
        return None

    if isinstance(val, datetime):
        return val.isoformat()

    if isinstance(val, str):
        try:
            return datetime.fromisoformat(val).isoformat()
        except ValueError as exc:
            raise ValueError(
                "Datetime string must be ISO 8601 (e.g. '2024-01-01T12:00:00+00:00')."
            ) from exc

    raise TypeError(
        f"Input 'val' must be datetime, str, or None, got {type(val).__name__}."
    )


def parse_int(val: int | str | None) -> int | None:
    """
    Helper method to parse input integer values as an int or str,
        and return their integer representation.

    Args:
        val (int | str | None): The integer value or its string representation.
            None if not provided.

    Raises:
        ValueError: If `val` is a string but cannot be converted to an integer
        TypeError: If `val` is neither an int nor a valid string representation

    Returns:

        int | None: The integer representation of the input value. None if input is not provided.
    """
    if val is None or val == "":
        return None

    if isinstance(val, int):
        return val

    if isinstance(val, str):
        try:
            return int(val.strip())
        except ValueError as exc:
            raise ValueError(f"Invalid string for integer: {val!r}") from exc

    raise TypeError(
        f"Input 'val' must be int or str, got type: {type(val).__name__} instead."
    )


def add_prefix(prefix: str, separator: str, key: str) -> str:
    """
    Adds a prefix to the given key with the specified separator.

    Args:
        prefix (str): The prefix to add.
        separator (str): The separator to use between the prefix and key.
        key (str): The original key.

    Returns:
        str: The new key with the prefix added.
    """
    if prefix is None or prefix == "":
        return key
    return f"{prefix}{separator}{key}"
