import tweepy
import time
import serial

# change this according to your own parameters
auth = tweepy.OAuthHandler("ofrEsnlPYgwtRW3QN6Mc9fxzW", "9P05QEYGG4W5JfI4cqvXMlPKdboA7JyHlsc7SOJXY3FdWcQDMr")
auth.set_access_token("788808390000701440-rjvxfwmJn7kEz5FMxrjPK23fi5bnVip", "UTnLSBLECeA0nnVI2IPew08HnwiTCVXxmz8nSlaZcV4ut")

api = tweepy.API(auth)

ctr = 0
ser = serial.Serial("/dev/cu.usbmodemFD131", 9600)
while(1):
    sequence = ser.read().decode()
    print(sequence == '1')
    if (sequence == '1'):
        api.update_status(status="Button pressed! #arduino #mcs "
                      +time.strftime("%d/%m/%Y") + " " + time.strftime("%H:%M:%S"))

    # if(ctr > 0):
    #     ctr = 0
    # if(sequence > 0 and ctr==0):
    #     auth = tweepy.OAuthHandler("ofrEsnlPYgwtRW3QN6Mc9fxzW", "9P05QEYGG4W5JfI4cqvXMlPKdboA7JyHlsc7SOJXY3FdWcQDMr")
    #     auth.set_access_token("788808390000701440-rjvxfwmJn7kEz5FMxrjPK23fi5bnVip", "UTnLSBLECeA0nnVI2IPew08HnwiTCVXxmz8nSlaZcV4ut")
    #     api = tweepy.API(auth)
    #
    #     if(sequence=='1'):
    #         api.update_status(status="Hi friends I'm home! (Sent by Python script) #yo "
    #                       +time.strftime("%d/%m/%Y") + " " + time.strftime("%H:%M:%S"))
    #     else:
    #         api.update_status(status="I'm busy right now. (Sent by Python script) #busy "
    #                       +time.strftime("%d/%m/%Y") + " " + time.strftime("%H:%M:%S"))
    #     print ("Status tweeted!")
    #     print ("Sequence: " + str(sequence))
    #     print (time.strftime("%d/%m/%Y"))
    #     ## 12 hour format ##
    #     print (time.strftime("%I:%M:%S"))
    #     ## 24 hour format ##
    #     print (time.strftime("%H:%M:%S"))
    #     ctr = ctr + 1
ser.close
