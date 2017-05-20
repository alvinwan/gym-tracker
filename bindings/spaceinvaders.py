"""Key configurations for Space Invaders"""

from .default import DefaultBinding


class SpaceInvadersBinding(DefaultBinding):

    def key_to_action_index(self, key: int) -> int:
        """Converts WASD and arrow keys to corresponding action indices.

        :param key: system key ID
        :return: corresponding game action index
        """
        if key in (119, 65362): # W, up
            return 0
        elif key in (97, 65361): # A, left
            return 3
        elif key in (115, 65364): # S, down
            return 0
        elif key in (100, 65363): # D, right
            return 2
        elif key == 99: # C
            return 1
        else:
            return 0

    def print_instructions(self):
        """Print instructions for user to use."""
        print('Use WASD or arrow keys to move left and right.')
        print('Use C to shoot.')
