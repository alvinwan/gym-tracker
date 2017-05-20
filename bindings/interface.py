"""Interface for key configuration"""

from typing import Dict


class BindingInterface:

    def __init__(self, state: Dict):
        self.state = state

    def key_press(self, key: int, _):
        """Set state actions accordingly on key press.

        :param key: key pressed
        """
        raise NotImplementedError()

    def key_release(self, key: int, _):
        """Set release actions accordingly on key release.

        :param key: key pressed
        """
        raise NotImplementedError()

    def print_instructions(self):
        """Print instructions for user to use."""
        raise NotImplementedError()
