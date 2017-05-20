"""
Tracks and logs all user actions, in addition to raw screen states.

Adapted from OpenAI Gym's example of human input: https://github.com/openai/gym

Includes more intuitive key bindings for the following games:
    - SpaceInvaders

Usage:
    main.py [options]

Options:
    --env_id=<id>       Environment ID [default: SpaceInvaders-v4]
    --skip-control=<n>  Use previous control n times. [default: 0]
    --rollout-time=<t>   Amount of time to rollout with each action [default: 1000]
"""

import docopt
import sys
import gym
import time
import bindings

from typing import Dict


def key_press(key: str, _, state: Dict):
    """Set state actions accordingly on key press.

    :param key: key pressed
    """
    if key == 0xff0d:
        state['restart'] = True
    if key == 32:
        state['pause'] = not state['pause']
    state['binding'].key_press(key, _)


def key_release(key: str, _, state: Dict):
    """Set release actions accordingly on key release.

    :param key: key pressed
    """
    state['binding'].key_release(key, _)


def rollout(env, state: Dict):
    """Advance game accordingly and update state actions.

    :param env: gym environment
    :param state: game state
    """
    state['restart'] = False
    obser = env.reset()
    skip = 0
    for t in range(state['rollout_time']):
        if not skip:
            action, skip = state['action'], state['skip_control']
        else:
            skip -= 1

        obser, r, done, info = env.step(action)
        env.render()
        if done:
            break
        if state['restart']:
            break
        while state['pause']:
            env.render()
            time.sleep(0.1)


def main():
    """Main runnable"""

    arguments = docopt.docopt(__doc__)

    state = {
        'action': 0,
        'restart': False,
        'pause': False,
        'skip_control': int(arguments['--skip-control']),
        'rollout_time': int(arguments['--rollout-time']),
    }

    env_id = arguments['--env_id']
    env = gym.make(env_id)

    if not hasattr(env.action_space, 'n'):
        raise Exception('Keyboard agent only supports discrete action spaces')
    state['actions'] = env.action_space.n

    # Setup custom key configuration if available
    state['binding'] = bindings.DefaultBinding(state)

    env.render()
    env.unwrapped.viewer.window.on_key_press = lambda key, mod: \
        key_press(key, mod, state)
    env.unwrapped.viewer.window.on_key_release = lambda key, mod: \
        key_release(key, mod, state)

    state['binding'].print_instructions()

    while 1:
        rollout(env, state)

if __name__ == '__main__':
    main()
