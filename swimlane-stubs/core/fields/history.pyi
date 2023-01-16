from .base import CursorField as CursorField
from .base import FieldCursor as FieldCursor
from .base import ReadOnly as ReadOnly

class RevisionCursor(FieldCursor):
    def __init__(self, *args, **kwargs) -> None: ...

class HistoryField(ReadOnly, CursorField):
    field_type: str
    cursor_class: RevisionCursor
    bulk_modify_support: bool
