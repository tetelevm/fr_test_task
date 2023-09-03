import json


__all__ = [
    "get_secret_variable"
]


_SECRET_PATH = "/run/secrets/backend_secrets"


try:
    with open(_SECRET_PATH, "r") as file:
        _secrets = file.read()
except FileNotFoundError:
    raise FileNotFoundError("secret file not found")

try:
    _ENVS_DICT: dict = json.loads(_secrets)
except ValueError:
    raise ValueError("the secret file must be in json format")


def get_secret_variable(name: str, default = None):
    return _ENVS_DICT.get(name, default)
