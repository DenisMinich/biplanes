"""Module contains scenes exceptions declaration"""


class SceneError(Exception):
    """Base scene error"""
    pass


class SceneBuilderError(SceneError):
    """Base scene builder error"""
    pass
