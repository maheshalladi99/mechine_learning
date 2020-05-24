from twilio.rest import Client
b=['+918328666506']
for i in b: 
    account_sid = 'AC6e5a4bf309adb313157e38b0a8081e59' 
    auth_token = '79e457ab54aefb32c43dbcad9f7b8899' 
    client = Client(account_sid, auth_token) 
    a="hai how are you ra"
    
    message = client.messages.create( 
                                  from_='+12059906541',  
                                  body=a,      
                                  to=i 
                              )
    print(message.sid)
