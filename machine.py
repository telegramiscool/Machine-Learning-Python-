import time 
import random 

import sys
from termcolor import colored, cprint


def learn():
    print("Machine learning!!!")

    count = 0
    while count != 11:
        print("Learning"+("."*random.randint(1,3)),10*count,"%")
        time.sleep(random.randint(0,2))
        count = count+1
        
    time.sleep(2)
    
    print("i have learnt alot now")
    print("fun fact: did you know that machine.learn works!!!!!!!")

    time.sleep(1)
    
    with open("IgnoreMachineDotPy.txt","r") as file:

        cprint(file.read(), 'red', attrs=['bold'], file=sys.stderr)




    




