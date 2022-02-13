import time
from Adafruit_IO import Client, Feed, Data,RequestError

ADAFRUIT_IO_KEY = 'aio_Zsga40o2pf1lRtwDp5lV6zr6D4Du'
ADAFRUIT_IO_USERNAME = 'shivvamm'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

oldState_event1 = False
newState_event1 = False

oldState_event2 = False
newState_event2 = False

action = aio.feeds('action')
hitaction = aio.feeds('hitaction')


# data = aio.receive(action.key)
# print('Retrieved value from Test has attributes: {0}'.format(data))
# print('Latest value from Test: {0}'.format(data.value))

# # Finally read the most revent value from feed 'Foo'.
# data = aio.receive(hitaction.key)
# print('Retrieved value from Foo has attributes: {0}'.format(data))
# print('Latest value from Foo: {0}'.format(data.value))


while(True):
    newState_event1 = bool(int(aio.receive(action.key).value))
    newState_event2 = bool(int(aio.receive(hitaction.key).value))
    if(oldState_event1!=newState_event1 or oldState_event2!=newState_event2):
        if(newState_event1==True and newState_event2==True):
           print("Moter on")
        else:
            print("Moter off") 
        
    else:
        print("Moter off already")

oldState_event1=newState_event1
oldState_event2=newState_event2
time.sleep(1)