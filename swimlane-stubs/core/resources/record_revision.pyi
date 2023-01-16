from typing import Any, Dict

from swimlane.core.resources.app import App as App
from swimlane.core.resources.record import Record as Record
from swimlane.core.resources.revision_base import RevisionBase as RevisionBase

class RecordRevision(RevisionBase):
    app_revision_number: float
    def __init__(self, app: App, raw: Dict[str, Any]) -> None: ...
    @property
    def app_version(self) -> str: ...
    @property
    def version(self) -> Record: ...
