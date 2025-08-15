import pyinputplus as pyip
import time
import sys

response = pyip.inputYesNo(prompt='Do you want to know how to keep an idiot busy for hours: ')
if response == 'no':
    print('Thanks for your time..')
    sys.exit()
elif response == 'yes':
    print("Great! Here's a fun task for you: Count to 10.. slowly!")
    for i in range(1, 21):
        print(f"Counting... {i}")
        time.sleep(1)  # wait 1 second each count to drag it out
    print("Finally i kept you busy for a while! sorry for falling :).")

    
