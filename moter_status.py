import time
from Adafruit_IO import Client, Feed, Data,RequestError

ADAFRUIT_IO_KEY = 'aio_Zsga40o2pf1lRtwDp5lV6zr6D4Du'
ADAFRUIT_IO_USERNAME = 'shivvamm'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

hum_threshold = 60
hum_val = 0

temp_threshold1 = 15
temp_threshold2 = 23
temp_val = 0

rain = aio.feeds('rain')
humidity = aio.feeds('soil')
temperature = aio.feeds('temperature1')


# data = aio.receive(action.key)
# print('Retrieved value from Test has attributes: {0}'.format(data))
# print('Latest value from Test: {0}'.format(data.value))

# # Finally read the most revent value from feed 'Foo'.
# data = aio.receive(hitaction.key)
# print('Retrieved value from Foo has attributes: {0}'.format(data))
# print('Latest value from Foo: {0}'.format(data.value))

a=0
while(True):

    if(int(aio.receive(rain.key).value)==0):

         hum_val = int(aio.receive(humidity.key).value)
         temp_val = int(aio.receive(temperature.key).value)

         if(hum_val<hum_threshold):
            
            if(a==0):
                time.sleep(0.1)
                aio.send_data('moter',1)
                a=1
                time.sleep(10)
                print("nooooooo")
            print("moter on")
            
            if(temp_val<temp_threshold1):
                hum_threshold = 75
            if(temp_val>temp_threshold2):
                hum_threshold = 80
         else:
            time.sleep(0.1)
            aio.send_data('moter',0)
            a=0
            print("moter off")
            hum_threshold = 60
            time.sleep(10)
    else:
        time.sleep(0.1)
        aio.send_data('moter',0)
        a=0
        print("moter off due to rain")
        hum_threshold = 60
        time.sleep(10)
    
    
    