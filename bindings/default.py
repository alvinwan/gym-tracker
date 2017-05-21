"""Defaults for key configurations."""

from typing import Dict
from .interface import BindingInterface


class DefaultBinding(BindingInterface):

    def key_to_action_index(self, key: int):
        return int( key - ord('0') )

    def key_press(self, key: int, _):
        """Set state actions accordingly on key press.

        :param key: key pressed
        """
        action = self.key_to_action_index(key)
        if action <= 0 or action >= self.state['actions']:
            return
        self.state['action'] = action

    def key_release(self, key: int, _):
        """Set release actions accordingly on key release.

        :param key: key pressed
        """
        action = self.key_to_action_index(key)
        if action <= 0 or action >= self.state['actions']:
            return
        if self.state['action'] == action:
            self.state['action'] = 0

    def print_instructions(self):
        """Print instructions for user to use."""
        print("ACTIONS={}".format(self.state['actions']))
        print("Press keys 1 2 3 ... to take actions 1 2 3 ...")
        print("No keys pressed is taking action 0")
