#!/usr/local/bin/python3
import _thread
import threading
from _thread import start_new_thread
threadId = 1
def factorial(n):
     global threadId 
     if n<1:
          print ("%s: %d:" % ("Thread", threadId))
          threadId +=1
          return 1
     else:
          returnNumber = n * factorial(n-1)
          print(str(n) + '! = ' + str(returnNumber))
          return returnNumber
start_new_thread(factorial,(5, ))
start_new_thread(factorial,(4, ))
c = input("wating for threads to return..\n")
