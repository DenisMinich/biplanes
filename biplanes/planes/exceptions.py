"""Contains planes exceptions"""


class PlaneError(Exception):
    """Base plane error"""
    pass


class PlaneBuilderError(PlaneError):
    """Base plane builder error"""
    pass
