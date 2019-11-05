#!/usr/bin/env python
from __future__ import division
import RPi.GPIO as GPIO
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pin", type=int, help="GPIO BCM Pin number", required=True)
parser.add_argument("-d", "--duration", type=int, help="Duration of toggle", required=True)

args = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setup(args.pin, GPIO.OUT)

GPIO.output(args.pin, GPIO.LOW)
time.sleep(args.duration / 1000)
GPIO.output(args.pin, GPIO.HIGH)
GPIO.cleanup()