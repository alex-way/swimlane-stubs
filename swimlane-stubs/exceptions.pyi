from typing import Dict, List, Optional

from requests import HTTPError
from swimlane.core.client import Swimlane
from swimlane.core.resources.app import App
from swimlane.core.resources.record import Record

class SwimlaneException(Exception): ...

class UnknownField(SwimlaneException, KeyError):
    app: App
    field_name: str
    similar_field_names: List[str]
    def __init__(self, app: App, field_name: str, field_pool: List[str]) -> None: ...

class ValidationError(SwimlaneException, ValueError):
    record: Record
    failure: str
    def __init__(self, record: Record, failure: str) -> None: ...

class _InvalidSwimlaneVersion(SwimlaneException, NotImplementedError):
    swimlane: Swimlane
    min_version: str
    max_version: str
    def __init__(self, swimlane: Swimlane, min_version: str, max_version: str) -> None: ...

class InvalidSwimlaneBuildVersion(_InvalidSwimlaneVersion): ...
class InvalidSwimlaneProductVersion(_InvalidSwimlaneVersion): ...

class SwimlaneHTTP400Error(SwimlaneException, HTTPError):
    codes: Dict[int, str]
    http_error: HTTPError
    code: int
    argument: Optional[str]
    name: str
    def __init__(self, http_error) -> None: ...
