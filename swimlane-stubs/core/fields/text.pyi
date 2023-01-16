from typing import Literal, Tuple, Type

from .base import Field as Field

class TextField(Field):
    field_type: Tuple[Literal["Core.Models.Fields.TextField, Core"], Literal["Core.Models.Fields.Text.TextField, Core"]]
    supported_types: Tuple[Type[str]]
    def set_python(self, value): ...
