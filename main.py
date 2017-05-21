"""
Tracks and logs all user actions, in addition to raw screen states.

Adapted from OpenAI Gym's example of human input: https://github.com/openai/gym

Includes more intuitive key bindings for the following games:
    - SpaceInvaders

Usage:
    main.py [options]

Options:
    --env_id=<id>       Environment ID [default: SpaceInvadersNoFrameskip-v4]
    --skip-control=<n>  Use previous control n times. [default: 0]
    --rollout-time=<t>  Max. Amount of time to play the game for [default: 100000]
    --logdir=<path>     Path to root of logs directory [default: ./logs]
    --random            Use a random agent.
"""

import docopt
import sys
import gym
import time
import bindings
import random
import numpy as np
import os
import time

from typing import Dict
from typing import List


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
    episode_reward = 0
    sar = []  # state-action-reward tuples
    for t in range(state['rollout_time']):
        if not skip:
            if state['random']:
                action = random.randint(0, state['actions'] - 1)
            else:
                action = state['action']
            skip = state['skip_control']
        else:
            skip -= 1

        observation, reward, done, info = env.step(action)
        sar.append(np.hstack((np.ravel(observation), action, reward)))
        episode_reward += reward
        if done:
            print('Episode finished after %d timesteps with reward %d' % (
                t, episode_reward))
            write_sar_log(sar, state['logdir'], episode_reward)
            sar = []
            break
        if state['restart']:
            break
        env.render()
        while state['pause']:
            env.render()
            time.sleep(0.1)


def write_sar_log(sars: List, logdir: str, episode_reward: int):
    """Write state-action-rewards to a log file."""
    np.savez_compressed(os.path.join(logdir,
        '%s_%s' % (str(time.time())[-5:], episode_reward)), np.vstack(sars))


def main():
    """Main runnable"""

    arguments = docopt.docopt(__doc__)
    env_id = arguments['--env_id']
    logdir = arguments['--logdir']
    env = gym.make(env_id)
    random.seed(0)

    os.makedirs(logdir, exist_ok=True)
    state = {
        'action': 0,
        'restart': False,
        'pause': False,
        'skip_control': int(arguments['--skip-control']),
        'rollout_time': int(arguments['--rollout-time']),
        'random': arguments['--random'],
        'env': env,
        'logdir': logdir
    }

    if not hasattr(env.action_space, 'n'):
        raise Exception('Keyboard agent only supports discrete action spaces')
    state['actions'] = env.action_space.n

    # Setup custom key configuration if available
    if 'SpaceInvaders' in env_id:
        state['binding'] = bindings.SpaceInvadersBinding(state)
    else:
        state['binding'] = bindings.DefaultBinding(state)

    env.render()

    if arguments['--random']:
        print(' * Using random agent.')
    else:
        env.unwrapped.viewer.window.on_key_press = lambda key, mod: \
            key_press(key, mod, state)
        env.unwrapped.viewer.window.on_key_release = lambda key, mod: \
            key_release(key, mod, state)
        state['binding'].print_instructions()

    while 1:
        rollout(env, state)


if __name__ == '__main__':
    main()
