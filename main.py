import os
import requests
import dotenv
import datetime as dt
#CONSTANTS
dotenv.load_dotenv()
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USER")
GRAPH_ID = os.getenv("GRAPH_ID")

# {"message":"Success. Let's visit https://pixe.la/@rahim9python3pixela ,
# it is your profile page!","isSuccess":true}



# termsofservice = "yes"
# notminor = "yes"

pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": termsofservice,
#     "notMinor": notminor
#
# }
# resp = requests.post(url=pixela_endpoint,json=user_params)
# print(resp.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_name = "GuitarPractice"
unit = "hours"
type_measured = "float"
color = "ajisai"
graph_headers = {"X-USER-TOKEN": TOKEN}
# graph_params = {
#     "id": GRAPH_ID,
#     "name": graph_name,
#     "unit": unit,
#     "type": type_measured,
#     "color": color
#
# }
# graph_resp = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# graph_resp.raise_for_status()
# print(graph_resp.text)

pixel_posting_endpoint = f"{graph_endpoint}/{GRAPH_ID}"


todays_date = str(dt.datetime.today().date().strftime("%Y%m%d"))
quantity = str(1)

pixel_posting_params = {
    "date" : todays_date,
    "quantity":quantity
}

# post_pixel_resp = requests.post(url=pixel_posting_endpoint, headers=graph_headers,json=pixel_posting_params)
# #post_pixel_resp.raise_for_status()
# print(post_pixel_resp.text)

update_endpt = f"{pixel_posting_endpoint}/{todays_date}"

update_params = {
    "quantity":"4"
}
# update_resp = requests.put(url=update_endpt, headers=graph_headers,json=update_params)

delete_resp = requests.delete(url=update_endpt, headers=graph_headers,json=update_params)
print(delete_resp.text)