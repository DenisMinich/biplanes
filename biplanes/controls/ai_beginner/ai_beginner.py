"""AI_beginner implementation"""

from biplanes.controls.base.base import BaseControl


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-nested-blocks
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-branches
# pylint: disable=attribute-defined-outside-init
class AIBeginner(BaseControl):
    """Simple ai for a plane"""

    def __init__(self):
        super(AIBeginner, self).__init__()
        self._reset()
        self._reset_traektory()

    def _reset(self):
        """Reset all key points"""
        self._on_traectory = False
        self._start_takeoff_steps = 15
        self._takeoff_steps = 100
        self._finish_takeoff_steps = self._start_takeoff_steps

    def _reset_traektory(self):
        """Reset all key points for traektory flight"""
        self._traectory_flight_steps = 30
        self._falling_steps = 15
        self._ready_to_fire = True
        self._correction_steps = self._falling_steps * 2
        self._post_correction_steps = self._falling_steps

    def update(self):
        """Update all inner controls state"""
        if self._target is not None:
            if self._target.velocity < 5:
                self._target.increase_velocity()
            else:
                if not self._on_traectory:
                    if self._start_takeoff_steps:
                        self._target.rotate_clockwise()
                        self._start_takeoff_steps -= 1
                    else:
                        if self._takeoff_steps:
                            self._takeoff_steps -= 1
                        else:
                            if self._finish_takeoff_steps:
                                self._target.rotate_conterclockwise()
                                self._finish_takeoff_steps -= 1
                            else:
                                self._on_traectory = True
                else:
                    if self._traectory_flight_steps:
                        self._traectory_flight_steps -= 1
                    else:
                        if self._falling_steps:
                            self._target.rotate_conterclockwise()
                            self._falling_steps -= 1
                        else:
                            if self._ready_to_fire:
                                self._target.fire()
                                self._ready_to_fire = False
                            else:
                                if self._correction_steps:
                                    self._target.rotate_clockwise()
                                    self._correction_steps -= 1
                                else:
                                    if self._post_correction_steps:
                                        self._target.rotate_conterclockwise()
                                        self._post_correction_steps -= 1
                                    else:
                                        self._reset_traektory()
