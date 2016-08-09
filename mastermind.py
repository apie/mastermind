#!/usr/bin/env python
## Mastermind
# By D.J. Murray
# 2016-08-03
# License GPLv3

from random import shuffle

debug=False

print '\
Mastermind - Guess the code\r\n\
Available \'colors\' are: 1,2,3,4,5,6.\r\n\
The code consists of a combination of 4 unique colors.\r\n\
You can guess 10 times before the game is over.\r\n\
Input your guess like this: \'1234\'.\r\n\
After each guess the computer returns how many items were guessed correct (this is indicated by a \'2\')\r\n\
and how many colors were guessed correct but had an incorrect position. (this is indicated by a \'1\').\r\n\
So if you get [2, 2, 2, 2] the guess was correct.\r\n\
If you guess the code within 10 tries, you win!\r\n\
'
allcorrect = [2,2,2,2]

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
  print 'Result:\t',tot
  print
  
  return tot == allcorrect

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

def start_game(code):
  won=False
  tries=0
  while not won and tries <10:
    tries=tries+1  
    print 'Try',tries
    guess = read_guess()
    won = check_code(code, guess)

  if won:
    print 'You won! Tries:',tries
  else:
    print 'You lost!'

  print 'The code was: %s' % ''.join(map(str,code))

def new_game():
  start_game(new_code())

if __name__ == '__main__':
  new_game()

