#Last assignment Tech Academy Python Class
'''
    File name: ascii-mountains.py
    Author: James Ward
    Date created: 3/21/2017
    Date last modified: 3/21/2017
    Python Version: 2.7
	Purpose: Prompt user for inputs into ascii mountain generation.
'''

import random
import time

def printMountain(peak_chars, nummountains):
    #peak size in *
    c="*"
    for x in range(0,nummountains):
        random.seed(x)
        hoffset = float(peak_chars)*.5
        woffset = random.randint(1,10)
        max = int(peak_chars + hoffset)
        min = int(peak_chars - hoffset)
        msize = random.randint(min,max)
        for i in range(0,msize,+woffset):
            time.sleep(.0025)
            print c * i
        for i in range(msize,0,-woffset):
            time.sleep(.0025)
            print c * i

def start(n):
    #vars
    maxmountains = 10
    maxpeak = 80
    mountains = 0
    peak = 0

    while (mountains < 2) or (mountains > maxmountains):
        mountains = raw_input ('Enter the number of mountains you want. Between 1-' + str(maxmountains) + ': ')
        mountains = int(mountains)

    while (peak < 11) or (peak > maxpeak):
        peak = raw_input ('Enter approximate mountain size between 11-' + str(maxpeak) + ': ')
        peak = int(peak)

    print("Generating your mountains, " + n + "!")
    time.sleep(2)
    print("-" * 80)
    printMountain(peak, mountains)
    print("-" * 80)
    doover(n)

def doover(n):
    Doover = raw_input("Do you want to play again, " + n + "? (Y)es or (N)o: ")
    if Doover.lower() == 'no' or Doover.lower() == 'n':
        quit()
    elif Doover.lower() == 'yes' or Doover.lower() == 'y':
        start(n)
    else:
        doover(n)

def quit():
     print("Peace Out!")


#Main Logic
print "This will print ascii mountains along the side of the screen"
print ""
name = raw_input ('Your name: ')
start(name)






