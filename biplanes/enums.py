"""Enums used in multiple entities"""


# pylint: disable=too-few-public-methods
class Direction(object):
    """Direction for some oriented objects as planes or guns"""
    RIGHT = 'right'
    LEFT = 'left'


class BlueTeam(object):
    """Blue team instance"""
    name = 'blue team'
    color = '0000ff'


class RedTeam(object):
    """Red team instance"""
    name = 'red team'
    color = 'ff0000'
