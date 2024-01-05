from getkey import *
import time
from functools import partial

######################################
#
# Don't touch the main loop and related variables
events={}
active_mainloop=True

def mainloop():
    init_mainloop()

    print('Enter mainloop()')
    while active_mainloop:
        k=get_key()
        if k!='':
            if k in events:
                f=events[k]
                f()
        else:
            time.sleep(0.01)
    print('Exit mainloop()')
    clean_mainloop()
######################################

total_sum = 0
numbers_entered = 0

# Yleinen funktio numeroiden käsittelyä varten
def handle_number(num):
    global total_sum, numbers_entered
    total_sum += num
    numbers_entered += 1
    print_total_sum()

# Määrittele numeronäppäimille vastaavat funktiot käyttäen partialia
for i in range(10):
    events[str(i)] = partial(handle_number, i)

def print_total_sum():
    global active_mainloop
    if numbers_entered == 10:
        print("Sum of entered numbers:", total_sum)
        active_mainloop = False
    else:
        print(total_sum)        

######################################
#
#Don't modify lines below
if __name__ == "__main__":
    mainloop()
