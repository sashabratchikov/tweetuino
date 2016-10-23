import tweepy
import time
import serial

auth = tweepy.OAuthHandler("ofrEsnlPYgwtRW3QN6Mc9fxzW", "9P05QEYGG4W5JfI4cqvXMlPKdboA7JyHlsc7SOJXY3FdWcQDMr")
auth.set_access_token("788808390000701440-rjvxfwmJn7kEz5FMxrjPK23fi5bnVip", "UTnLSBLECeA0nnVI2IPew08HnwiTCVXxmz8nSlaZcV4ut")

api = tweepy.API(auth)

ctr = 0
ser = serial.Serial("/dev/cu.usbmodemFD131", 9600)
while(1):
    message = ser.read().decode()
    print(message == '1')
    if (message == '1'):
        api.update_status(status="Button pressed! #arduino #mcs ")
ser.close
