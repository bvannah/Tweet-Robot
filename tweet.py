# importing the module 
import tweepy 
import serial
import datetime
import time
#set up twitter stuff  
consumer_key ="6bmjjXgCZekss2tiKB1jHIemV"
consumer_secret ="Bvl8Dr8NIWpEFm2RTUUPNhminbTyJHBe5xgUd4M4gOCZyaxSwh"
access_token ="1069397171320041472-UHKBzoQ2iNzlUsKkjwB225gm2yMers"
access_token_secret ="XRVl4TKbyxagHGOKpJIiWnWsf0Ljr6SRKPTw4ITwqinow"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
ser = serial.Serial('/dev/ttyACM0')  # open serial port
ser.baudrate=9600
print(ser)


while 1:
    if(ser.in_waiting>0):
        tim=str(datetime.datetime.now())[11:19]
        s = ord(ser.read(1))
        if(s==49):
            api.update_status(status= "The time is " + tim + ", and I'm moving a lot.")
        if(s==50):
            api.update_status(status= "The time is " + tim + ", and I'm moving a little.")
        if(s==51):
            api.update_status(status= "The time is " + tim + ", and I'm back on my feet again!")
        if(s==52):
            api.update_status(status= "The time is " + tim + ", and someone is TOTALLY pushing my buttons.")
        time.sleep(1)
ser.close()
