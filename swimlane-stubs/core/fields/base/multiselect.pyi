from .cursor import CursorField as CursorField, FieldCursor as FieldCursor
from _typeshed import Incomplete

class MultiSelectCursor(FieldCursor):
    def __init__(self, *args, **kwargs) -> None: ...
    def select(self, element) -> None: ...
    def deselect(self, element) -> None: ...

class MultiSelectField(CursorField):
    cursor_class: Incomplete
    def get_python(self): ...
    def get_swimlane(self): ...
    def set_python(self, value) -> None: ...
    def set_swimlane(self, value): ...
    def for_json(self): ...
