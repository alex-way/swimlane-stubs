from swimlane.core.client import Swimlane
from swimlane.core.resources.app import App

class SwimlaneResolver:
    def __init__(self, swimlane: Swimlane) -> None: ...

class AppResolver(SwimlaneResolver):
    def __init__(self, app: App) -> None: ...
