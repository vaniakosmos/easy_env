import os

from typing import Optional, Union


__all__ = [
    'get_int', 'get_float', 'get_bool', 'get_str', 'get_bytes', 'get_list', 'get',
]
TRUE_VALUES = set('1 y yes ok okay confirm absolutely totally yep'.split())


def process(factory, key: str, default: Optional[int], raise_error: bool):
    value = os.getenv(key, None)
    if value is None:
        if default is not None:
            value = default
        elif raise_error:
            raise KeyError('Failed to find env var {}'.format(key))
    else:
        value = factory(value)
    return value


def bool_factory(value: str):
    return value in TRUE_VALUES


def bytes_factory(value: str, encoding: str):
    return value.encode(encoding)


def list_factory(value: str, separator: str, item_factory):
    return list(map(item_factory, value.split(separator)))


def get_int(key: str, default: Optional[int] = None, raise_error=False) -> Optional[int]:
    return process(int, key, default, raise_error)


def get_float(key: str, default: Optional[float] = None, raise_error=False):
    return process(float, key, default, raise_error)


def get_str(key: str, default: Optional[str] = None, raise_error=False):
    return process(str, key, default, raise_error)


def get_bool(key: str, default: Optional[bool] = None, raise_error=False):
    return process(str, key, default, raise_error)


def get_bytes(key: str, default: Optional[int] = None, raise_error=False, encoding='utf-8'):
    return process(lambda x: bytes_factory(x, encoding),
                   key, default, raise_error)


def get_list(key: str, default: Optional[int] = None, raise_error=False, separator=',', item_factory=str):
    return process(lambda x: list_factory(x, separator, item_factory),
                   key, default, raise_error)


def based_on_default(key: str, default: Optional[int] = None,
                     raise_error=False, separator=',', item_factory=str, encoding='utf-8'):
    default_type = type(default)
    if default_type is int:
        return get_int(key, default, raise_error)
    if default_type is float:
        return get_float(key, default, raise_error)
    if default_type is str:
        return get_str(key, default, raise_error)
    if default_type is bool:
        return get_bool(key, default, raise_error)
    if default_type is bytes:
        return get_bytes(key, default, raise_error, encoding)
    if default_type is list:
        return get_list(key, default, raise_error, separator, item_factory)


def get(key: str, default: Optional[Union[int, float, bool, str, bytes, list]] = None,
        raise_error=False, separator=',', item_factory=str, encoding='utf-8'):
    """Autodetect right type based on default."""
    if default is not None:
        return based_on_default(key, default, raise_error, separator, item_factory, encoding)
    return get_str(key, default, raise_error)
