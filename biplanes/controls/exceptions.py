"""Module contains controls exceptions declaration"""


class ControlError(Exception):
    """Base control error"""
    pass


class ControlBuilderError(ControlError):
    """Base control builder error"""
    pass
