# Gym Tracker
Tracks and logs actions for a human player

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
    --env_id=<id>       Environment ID [default: SpaceInvaders-v4]
    --skip-control=<n>  Use previous control n times. [default: 0]
    --rollout-time=<t>   Amount of time to play the game for [default: 1000]
    --log-dir=<path>    Path to root of logs directory [default: ./logs]
```
