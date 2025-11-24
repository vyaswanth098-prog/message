from twilio.rest import Client
from dotenv import load_dotenv
import requests
import os

url=f"https://nse-api-khaki.vercel.app/symbols"
data=requests.get(url).json()
symbols_list=[]
for i in (data["symbols"]):
  symbols_list.append(i["symbol"])
data1=[]
final_data={}
for i in symbols_list:
  if i=="M&M":
    continue
  url=f"https://nse-api-khaki.vercel.app//stock?symbol={i}"
  data2=requests.get(url).json()
  data1.append(data2["data"])
  final_data[i]={"previous_close":data2["data"]["previous_close"]["value"],"last_price":data2["data"]["last_price"]["value"],"company":data2['data']["company_name"]}

message =""

for i in final_data:
  percent=(final_data[i]["last_price"]-final_data[i]["previous_close"])/final_data[i]["previous_close"]*100
  percent=round(percent,2)
  if percent > 0:
      message +=f"{final_data[i]["company"]} is increased by {percent}% and it's current price is {final_data[i]['last_price']}\n"
if message !="":
  load_dotenv()

  account_sid = os.getenv('TWILIO_ACCOUNT_SID')
  auth_token = os.getenv('TWILIO_AUTH_TOKEN')
  from_number = os.getenv('TWILIO_NUMBER')
  to_number = os.getenv('MY_NUMBER')

  client = Client(account_sid, auth_token)

  message = client.messages.create(
     body=message,
     from_=from_number,
     to=to_number
  )

print(f"Message SID: {message.sid}")

