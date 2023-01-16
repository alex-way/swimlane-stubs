from typing import Any, Dict

from pendulum.datetime import DateTime
from swimlane.core.client import Swimlane
from swimlane.core.resources.base import APIResource as APIResource

class Attachment(APIResource):
    file_id: str
    filename: str
    upload_date: DateTime
    def __init__(self, swimlane: Swimlane, raw: Dict[str, Any]) -> None: ...
    def __hash__(self): ...
    def download(self, chunk_size: int = ...): ...
    def for_json(self): ...
