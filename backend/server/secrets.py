import json
from pathlib import Path


__all__ = [
    "get_secret_variable"
]


_SECRET_PATH = Path("/run/secrets/backend_secrets")
_SECRET_LOCAL_PATH = (Path().parent.parent / "backend_secrets").absolute()

_current_path = _SECRET_PATH if _SECRET_PATH.is_file() else _SECRET_LOCAL_PATH

try:
    with open(_current_path, "r") as file:
        _secrets = file.read()
except FileNotFoundError:
    raise FileNotFoundError("secret file not found")

try:
    _ENVS_DICT: dict = json.loads(_secrets)
except ValueError:
    raise ValueError("the secret file must be in json format")


def get_secret_variable(name: str, default=None):
    return _ENVS_DICT.get(name, default)
