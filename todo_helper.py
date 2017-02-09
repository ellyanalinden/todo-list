#!/usr/bin/env python

import os
import sys
import tty
import termios

def get():
    with open('todos.txt', 'r') as f:
        return [ l.strip() for l in f.readlines() if l.strip() ]

def save(todos):
    with open('todos.txt', 'w') as f:
        for todo in todos:
            f.write(todo + "\n")

def get_ch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
