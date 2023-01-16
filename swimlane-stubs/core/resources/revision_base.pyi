from typing import Any, Dict, Union

from pendulum.date import Date
from pendulum.datetime import DateTime
from pendulum.duration import Duration
from pendulum.time import Time
from swimlane.core.client import Swimlane
from swimlane.core.resources.base import APIResource as APIResource
from swimlane.core.resources.usergroup import User as User
from swimlane.core.resources.usergroup import UserGroup as UserGroup

class RevisionBase(APIResource):
    modified_date: Union[Date, Time, DateTime, Duration]
    revision_number: str
    status: str
    user: User
    def __init__(self, swimlane: Swimlane, raw: Dict[str, Any]) -> None: ...
    @property
    def version(self) -> None: ...
    def for_json(self): ...
