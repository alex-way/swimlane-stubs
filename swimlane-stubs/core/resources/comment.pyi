from typing import Any, Dict, TypedDict

from pendulum.datetime import DateTime
from swimlane.core.client import Swimlane
from swimlane.core.resources.base import APIResource as APIResource
from swimlane.core.resources.usergroup import UserGroup as UserGroup
from swimlane.core.resources.usergroup import UserGroupForJson

class CommentForJson(TypedDict):
    message: str
    createdDate: str
    createdByUser: UserGroupForJson

class Comment(APIResource):
    user: UserGroup
    created_date: DateTime
    message: str
    is_rich_text: bool
    def __init__(self, swimlane: Swimlane, raw: Dict[str, Any]) -> None: ...
    def for_json(self) -> CommentForJson: ...
