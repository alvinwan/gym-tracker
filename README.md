# OpenAI Gym Tracker
Tracks and logs actions for a human player. This repository also includes
~70,000 timesteps of human gameplay across 16 episodes, with an average of ~710
points. (The random agent scores an average of ~150 points.)

> Disclaimer: I was the human player, and my gameplay isn't the best. If you're
a SpaceInvader master or have logged data for other games, I would be more than
happy to include your logs.

# Logs

The logs are written to `.npz` - Numpy's compressed data file extension - and
can be read using numpy utilities.

# Install

The project is written in Python 3 and is not guaranteed to successfully backport to Python 2.

(Optional) We recommend setting up a virtual environment.

```
virtualenv gymt --python=python3
source activate gymt/bin/activate
```

Say `$GYMT_ROOT` is the root of your repository. Navigate to your root repository.

```
cd $GYMT_ROOT
```

We need to setup our Python dependencies.

```
pip install -r requirements.txt
```

# Run

To run with the default game (SpaceInvaders), use the following

```
python main.py
```

Here are full usage instructions:

```
Usage:
    main.py [options]

Options:
    --env_id=<id>       Environment ID [default: SpaceInvadersNoFrameskip-v4]
    --skip-control=<n>  Use previous control n times. [default: 0]
    --rollout-time=<t>  Max. Amount of time to play the game for [default: 100000]
    --logdir=<path>     Path to root of logs directory [default: ./logs]
    --random            Use a random agent.
```
