import random as r
import time as t
from art import *
from os import system

def password():
  tprint("hello friend")
  username=input("username >> ")
  password=input("password >> ")
  system('cls')
  if username is None:
    print("you must enter the username")
    break
  elif password == '': #random pw
    print(f'\nwelcome {username}...')
    t.sleep(0.05)
  else:
    exit()
    
password()
