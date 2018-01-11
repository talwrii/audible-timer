# audible-timer

A countdown timer that produces output suitable for a text-to-speech system.

Requires Python3.

# Installation

```
pip3 install git+https://github.com/talwrii/btrgit#egg=audible-timer
```

# Usage

*This must be used together with text to speech program, for example [festival-lines](https://github.com/talwrii/festival-lines).

```
# Count down from 100
audible-interval 100 | festival-lines
```
# Development
We have a basic test for dependencies / syntax errors:

```
python3 setup.py test
```
