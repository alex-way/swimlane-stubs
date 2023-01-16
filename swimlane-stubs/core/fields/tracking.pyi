from typing import Literal, Union

from .base import Field as Field
from .base import ReadOnly as ReadOnly

class TrackingField(ReadOnly, Field):
    field_type: Union[
        Literal["Core.Models.Fields.TrackingField, Core"], Literal["Core.Models.Fields.Tracking.TrackingField, Core"]
    ]
    bulk_modify_support: bool
