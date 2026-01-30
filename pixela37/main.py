import requests
from datetime import datetime


pixel_enddpoint="https://pixe.la/v1/users"
TOKEN="your_token_anything"
USERNAME="your_username"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

#response=requests.post(url=pixel_enddpoint,json=user_params)
#print(response.text)

graph_endpoint=f"{pixel_enddpoint}/{USERNAME}/graphs"
GRAPHID="graph1"
graph_config={
    "id":"graph1",
    "name":"cycling graph",
    "unit":"km",
    "type":"float",
    "color":"sora"

}
headers={
    "X-USER-TOKEN":TOKEN
}
#response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#print(response.text)

today=datetime.now() # if u forget to add a day then u can manually add it here by specifying datetime(year,month,day)
#print(today.strftime("%Y%m%d"))



pixel_posting1=f"{pixel_enddpoint}/{USERNAME}/graphs/{GRAPHID}"
posting_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many kilometers did u run today??"),
}

response=requests.post(url=pixel_posting1,json=posting_config,headers=headers)
print(response.text)

###Now to update some particular date stuff follow below
DATE_TO_UPDATE="20260103"
update_endpoint=f"{pixel_enddpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE_TO_UPDATE}"

update_config={
    "quantity":"11.1"
}

#response=requests.put(url=update_endpoint,json=update_config,headers=headers)
#print(response.text)

###To delete a pixel now

delete_endpoint=f"{pixel_enddpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE_TO_UPDATE}"

#response=requests.delete(url=delete_endpoint,headers=headers)

#print(response.text)
