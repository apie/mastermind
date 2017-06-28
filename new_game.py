#!/usr/bin/env python2
from sys import argv
from mastermind import clearSaveGame

if __name__ == '__main__':
  if len(argv) == 2:
    player = argv[1]
    clearSaveGame(player)

