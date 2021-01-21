# generated by datamodel-codegen:
#   filename:  enum_models.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None
    kind: Optional[Literal['dog', 'cat']] = None
    type: Optional[Literal['animal']] = None


class Pets(BaseModel):
    __root__: List[Pet]


class Animal(BaseModel):
    kind: Optional[Literal['snake', 'rabbit']] = None


class Error(BaseModel):
    code: int
    message: str


class EnumObject(BaseModel):
    type: Optional[Literal['a', 'b']] = None


class EnumRoot(Enum):
    a = 'a'
    b = 'b'


class IntEnum(Enum):
    number_1 = 1
    number_2 = 2


class AliasEnum(Enum):
    a = 1
    b = 2
    c = 3


class MultipleTypeEnum(Enum):
    red = 'red'
    amber = 'amber'
    green = 'green'
    NoneType_None = None
    int_42 = 42


class SingleEnum(Enum):
    pet = 'pet'
