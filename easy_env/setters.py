import os


__all__ = [
    'set_int', 'set_float', 'set_bool', 'set_str', 'set_bytes', 'set_list',
]


def set_int(key: str, value: int):
    os.environ[key] = str(value)


def set_float(key: str, value: float):
    os.environ[key] = str(value)


def set_str(key: str, value: str):
    os.environ[key] = value


def set_bool(key: str, value: bool):
    os.environ[key] = '1' if value else '0'


def set_bytes(key: str, value: bytes, **kwargs):
    encoding = kwargs.pop('encoding', ',')
    os.environ[key] = value.decode(encoding)


def set_list(key: str, value: list, **kwargs):
    separator = kwargs.pop('separator', ',')
    os.environ[key] = separator.join(map(str, value))


FUNC_MAP = {
    int: set_int,
    float: set_float,
    str: set_str,
    bool: set_bool,
    bytes: set_bytes,
    list: set_list,
}


def set(key: str, value, **kwargs):
    value_type = type(value)
    setter = FUNC_MAP.get(value_type, None)
    if setter is None:
        raise ValueError('Unknown value type')
    setter(key, value_type, **kwargs)
