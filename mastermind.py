#!/usr/bin/env python2
## Mastermind
# By D.J. Murray
# 2016-08-03
# License GPLv3

from random import shuffle
import pickle
from os import remove
from sys import argv
from json import dumps

debug=False
allcorrect = [2]*4
savefile = "mastermind_status.pickle"

def check_code( code, guess ):
  if debug:
    print 'code:\t\t',code
    print 'guess:\t\t',guess      
  tot=[0]*4
  #correct
  correct=[0]*4
  c=0
  for i in guess:
    if i == code[c]:
      correct[c] = i
      tot[c] = 2
    c=c+1

  #items
  item=[0]*4
  c=0
  for i in guess:
    if i in code and not correct[c]==i:
      item[c] = i
      tot[c] = 1
    c=c+1
      
  shuffle(tot)

  if debug:
    print 'correct items:\t',item
    print 'correct it+pos:\t',correct
    print
  
  return (tot,tot == allcorrect)

def read_guess():
  guessr = ''
  while guessr == '' or len(guessr)<>4:
    guess = []
    guessr = raw_input('Guess: ')
    if guessr == '':
      if raw_input('Quit? (y to quit): ') == 'y':
        exit()

    for character in guessr:
      if character.isdigit() and int(character) not in guess:
        guess.append(int(character))
      else:
        guessr = '' #faulty input, try again.
    if debug:
      print guess
  return guess

def new_code():
  code=range(7)[1:]#remove 0
  shuffle(code)
  return code[:4] #return 4 items

def run_game(gamestatus, suppliedguess='', save=False):
  tries, code = gamestatus
  if debug:
    print tries
    print code
    print suppliedguess
    print save

  won=False
  result=[0]*4
  while not won and tries <10:
    tries=tries+1  
    if suppliedguess == '':
      print 'Try',tries
      guess = read_guess() # todo add guess argument
    else:
      # todo create generic function wich returns if guess was valid
      guess = []
      #Only allow the first 4 characters, they must be unique and of integer type
      for character in suppliedguess[:4]:
        if character.isdigit() and int(character) not in guess:
          guess.append(int(character))
    result, won = check_code(code, guess)
    if suppliedguess == '':
      print 'Result:\t',result
      print
    if save:
      try:
        pickle.dump( (tries,code), open(savefile,"wb"))
      except:
        print 'Could not write savegame file.'
      if not won and tries<10:
        return (tries,result,won)#only allow one try every time

  if save and (won or tries>=10):
    try:
      remove(savefile)
    except:
      print 'Could not remove savegame file.'
  return (tries,result,won)

def newgamestatus():
  return (0,new_code())

def new_game():
  print '\
  Mastermind - Guess the code\r\n\
  Available \'colors\' are: 1,2,3,4,5,6.\r\n\
  The code consists of a combination of 4 unique colors.\r\n\
  You can guess 10 times before the game is over.\r\n\
  Input your guess like this: \'1234\'.\r\n\
  After each guess the computer returns how many items were guessed correct (this is indicated by a \'2\')\r\n\
  and how many colors were guessed correct but had an incorrect position. (this is indicated by a \'1\').\r\n\
  So if you get %s the guess was correct.\r\n\
  If you guess the code within 10 tries, you win!\r\n\
  ' % ','.join(map(str,allcorrect))

  gamestatus = newgamestatus()
  tries,code = gamestatus;
  tries,result,won = run_game(gamestatus)
  if won:
    print 'You won! Tries:',tries
  else:
    print 'You lost!'

  print 'The code was: %s' % ''.join(map(str,code))

def resume_game(guess):
  try:
    gamestatus = pickle.load(open(savefile,"rb"))
  except:
    gamestatus = newgamestatus()
  if debug:
    print 'gamestatus: ',gamestatus
  return run_game(gamestatus,guess,True)


if __name__ == '__main__':
  if len(argv) == 1:
    new_game()
  else:
    tries,result,won = resume_game(argv[1])
    lost = tries>=10
    print dumps( {'tries':tries, 'result':'%s' % ''.join(map(str,result)), 'won':won, 'lost':lost})
