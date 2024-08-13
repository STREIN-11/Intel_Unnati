from twilio.rest import Client


acc_sid = "AC708aaa8c9555929c7d9bc937e8d2dd47"
auth_token = "baeffbc9a4b94b5f6656cb8b30f14ad1"


client = Client(acc_sid,auth_token)

msg = client.messages.create(body="!!!Soil Moisture is Critivally Low and Water sources are dried up!!!",
     from_= "+19499903573",
     to="+919800866506"
)


print(msg.sid)