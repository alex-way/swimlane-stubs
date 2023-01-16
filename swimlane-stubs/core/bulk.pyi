from typing import Any, Optional

class _BulkModificationOperation:
    type: Optional[str]
    value: Any
    def __init__(self, value: Any) -> None: ...

class Replace(_BulkModificationOperation):
    type: str

class Clear(_BulkModificationOperation):
    type: str
    def __init__(self) -> None: ...

class Append(_BulkModificationOperation):
    type: str

class Remove(_BulkModificationOperation):
    type: str
