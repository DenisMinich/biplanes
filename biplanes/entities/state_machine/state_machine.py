from kivy.properties import NumericProperty
from parabox.base_object import BaseObject


class StateMachine(BaseObject):
    """
    Assign states behaviour to object
    """

    @property
    def current_state(self):
        return self.state

    @current_state.setter
    def current_state(self, value):
        self.change_state(value)

    state = NumericProperty(None)

    def __init__(self, *args, states=None, initial=None, **kwargs):
        """
        Class constructor

        :param states: list of states
        :type states: list of State or None
        :param initial: initial state to be selected
        :type initial: State or None
        """
        super(StateMachine, self).__init__(*args, **kwargs)
        self.states = [] if states is None else states
        if initial is not None:
            self.change_state(initial)

    def change_state(self, state_name):
        """
        Change current state of object

        :param state_id: id of new state
        :type states: Any
        """
        for state in self.states:
            if state.name == state_name:
                state.on_apply(self)
                self.state = state.name
                break
