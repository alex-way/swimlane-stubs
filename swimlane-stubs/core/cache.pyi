from _typeshed import Incomplete
from swimlane.core.resources.base import APIResource as APIResource

logger: Incomplete

class ResourcesCache:
    def __init__(self, per_cache_max_size) -> None: ...
    def __len__(self): ...
    def __contains__(self, item): ...
    def __getitem__(self, item): ...
    def __delitem__(self, resource) -> None: ...
    def cache(self, resource) -> None: ...
    def clear(self, *resource_types) -> None: ...

def get_cache_index_key(resource): ...
def check_cache(resource_type): ...
