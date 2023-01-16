from typing import Any, Dict, List

from swimlane.core.cursor import PaginatedCursor as PaginatedCursor
from swimlane.core.resources.app import App as App
from swimlane.core.resources.base import APIResource as APIResource
from swimlane.core.resources.record import Record as Record
from swimlane.core.resources.record import record_factory as record_factory
from swimlane.core.search import ASC as ASC
from swimlane.core.search import CONTAINS as CONTAINS
from swimlane.core.search import DESC as DESC
from swimlane.core.search import EQ as EQ
from swimlane.core.search import EXCLUDES as EXCLUDES
from swimlane.core.search import GT as GT
from swimlane.core.search import GTE as GTE
from swimlane.core.search import LT as LT
from swimlane.core.search import LTE as LTE
from swimlane.core.search import NOT_EQ as NOT_EQ
from swimlane.core.search import FilterSearchType, SortSearchType

class Report(APIResource, PaginatedCursor):
    default_limit: int
    name: str
    keywords: List[str]
    def __init__(self, app: App, raw: Dict[str, Any], **kwargs) -> None: ...
    def filter(self, field_name: str, operand: FilterSearchType, value: Any) -> None: ...
    def sort(self, field_name: str, order: SortSearchType) -> None: ...
    def set_columns(self, *field_names: str) -> None: ...

def report_factory(app, report_name: str, **kwargs): ...
