from io import IOBase as IOBase
from typing import Any, Dict, List, Optional, Tuple

from swimlane.core.fields.base import FieldCursor as FieldCursor
from swimlane.core.fields.base import MultiSelectField as MultiSelectField
from swimlane.core.resources.attachment import Attachment as Attachment

class AttachmentCursor(FieldCursor):
    def add(self, filename: str, stream: IOBase, content_type: Optional[str] = ...): ...

class AttachmentsField(MultiSelectField):
    field_type: Tuple[str, str]
    cursor_class: AttachmentCursor
    supported_types: List[Attachment]
    bulk_modify_support: bool
    multiselect: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def get_initial_elements(self): ...
    def get_batch_representation(self): ...
    def cast_to_python(self, value) -> Attachment: ...
    def cast_to_swimlane(self, value) -> Dict[str, Any]: ...
