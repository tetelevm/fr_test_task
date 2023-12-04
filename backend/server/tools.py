from enum import Enum
from typing import Tuple, Any, Optional

from django.db.models import CharField
from django.utils.crypto import get_random_string


__all__ = [
    "RandomString",
    "Choices",
]


class RandomString(CharField):
    def __init__(self, **kwargs):
        kwargs["default"] = self.get_value
        super().__init__(**kwargs)

    def get_value(self) -> str:
        # In theory, it needs a check for uniqueness or catching an
        # error from the database.
        return get_random_string(self.max_length)


class Choices(Enum):
    _ignore_ = ["_DEFAULT"]

    @classmethod
    def as_tuple(cls) -> Tuple[Tuple[str, Any]]:
        return tuple((t.name, t.value) for t in cls)

    @classmethod
    def as_reverted_tuple(cls) -> Tuple[Tuple[Any, str]]:
        return tuple((t.value, t.name) for t in cls)

    @classmethod
    def arg_names(cls) -> Tuple[str]:
        return tuple(t.name for t in cls)

    @classmethod
    def DEFAULT(cls) -> Optional[str]:
        if hasattr(cls, "_DEFAULT"):
            return cls._DEFAULT.name
        return None

    @classmethod
    def contains(cls, item: str) -> bool:
        return item in cls.arg_names()

    @classmethod
    def get_(cls, val: str) -> Optional[Any]:
        try:
            return cls[val].value
        except KeyError:
            if hasattr(cls, "_DEFAULT"):
                return cls._DEFAULT.value
        return None
