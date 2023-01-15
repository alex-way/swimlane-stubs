from .field import Field as Field
from _typeshed import Incomplete
from swimlane.core.cursor import Cursor as Cursor
from swimlane.core.resolver import SwimlaneResolver as SwimlaneResolver

class FieldCursor(Cursor, SwimlaneResolver):
    def __init__(self, field, initial_elements: Incomplete | None = ...) -> None: ...
    def __eq__(self, other): ...

class CursorField(Field):
    cursor_class: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def get_initial_elements(self): ...
    @property
    def cursor(self): ...
    def get_python(self): ...
    def for_json(self): ...
