from typing import Tuple

from swimlane.core.resources.app import App as App
from swimlane.core.resources.revision_base import RevisionBase as RevisionBase

class AppRevision(RevisionBase):
    SEPARATOR: str
    @staticmethod
    def get_unique_id(app_id: str, revision_number: float): ...
    @staticmethod
    def parse_unique_id(unique_id: str) -> Tuple[str, str]: ...
    @property
    def version(self) -> App: ...
    def get_cache_index_keys(self): ...
