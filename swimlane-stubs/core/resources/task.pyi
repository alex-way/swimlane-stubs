from typing import Any, Dict, Optional

from swimlane.core.client import Swimlane
from swimlane.core.resources.base import APIResource as APIResource

class Task(APIResource):
    app_id: Optional[str]
    id: Optional[str]
    name: Optional[str]
    script: Optional[str]
    def __init__(self, swimlane: Swimlane, raw: Dict[str, Any]) -> None: ...
