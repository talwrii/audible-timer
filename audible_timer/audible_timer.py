import argparse
import time
import sys

if sys.version_info[0] != 3:
    # FileNotFoundError does not exist in python 2
    raise Exception('Only works with python 3')


PARSER = argparse.ArgumentParser(description='Countdown with audible alerts')
PARSER.add_argument('seconds', type=int)
PARSER.add_argument(
    '--alert-period', type=int, default=10, metavar='SEC',
    help='Alert every SEC seconds')


def main():
    args = PARSER.parse_args()
    start = time.time()
    end = start + args.seconds

    while True:
        time_left = end - time.time()
        print('{:.0f} seconds left'.format(time_left), flush=True)
        time_until_alarm = min(time_left, time_left -  time_left  // args.alert_period * args.alert_period)
        if time_left <= 0:
            print('Time is up', flush=True)
            return
        else:
            time.sleep(max(time_until_alarm, 0.01)) # paranoia about time loop towards ends
