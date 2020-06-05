import requests


# create_user
# print("----------------SignUp----------------------\n")
# data = '{"username" : "user11","phone_number": "24354656545687","password":"user11"}'
# url = "http://127.0.0.1:8080/api/lets_ride/sign_up/v1/"
# response = requests.post(url=url, data=data, headers={'Content-Type':"application/json"})
# print(response.content)


# login_user
# print("------------------LoginIn---------------------------\n")
# url = "http://127.0.0.1:8080/api/lets_ride/login/v1/"
# data = '{"phone_number": "1234567890","password":"user1"}'
# response = requests.get(url=url, data=data, headers={'Content-Type':"application/json"})
# print(response.content)


# update_password
# print("-----------------update_password------------------")
# data = '{"new_password": "user111"}'
# url = "http://127.0.0.1:8080/api/lets_ride/update_password/v1/"
# response = requests.post(url=url, data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer uR7qqZVzwc4xo5iawocg4Ia1qDlGRO'})
# print(response.content)


#user_profile
# print("----------------------user_profile------------------------\n")
# url = "http://127.0.0.1:8080/api/lets_ride/user/profile/v1/"
# response = requests.get(url=url, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)

#ride_request
# print("---------------------ride_request_with_flexible_timmings----------------------------\n")
# data = '{"source" : "kurnool", "destination" : "Hyderabad", "travel_date_time": "", "flexible_timings": true, "flexible_from_date_time" : "2020-06-12 05:30 PM", "flexible_to_date_time" : "2020-06-12 05:30 PM", "seats" : 3, "laguage_quantity": 4}'
# url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
# response = requests.post(url=url,data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)


# #ride_request
# print("---------------------ride_request----------------------------\n")
# data = '{"source" : "kurnool", "destination" : "Hyderabad", "travel_date_time": "2020-06-12 05:30 PM", "flexible_timings": false, "flexible_from_date_time" : "", "flexible_to_date_time" : "", "seats" : 3, "laguage_quantity": 4}'
# url = "http://127.0.0.1:8080/api/lets_ride/ride_request/v1/"
# response = requests.post(url=url,data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)



# #Asset Request
# print("--------------------asset_request_with_flexible_timmings-----------------\n")
# data = '{"source" : "kurnool", "destination" : "Hyderabad", "travel_date_time": "", "flexible_timings": true, "flexible_from_date_time" : "2020-04-12 05:30 PM", "flexible_to_date_time" : "2020-06-12 05:30 PM", "asset_quantity" : 3, "asset_type": "BAG", "asset_type_others" : "", "asset_sensitivity": "HIGH", "deliver_to" : "user1", "phone_number":"1234567890"}'
# url = "http://127.0.0.1:8080/api/lets_ride/asset_request/v1/"
# response = requests.post(url=url,data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)



# #Asset Request
# print("--------------------asset_request-----------------\n")
# data = '{"source" : "kurnool", "destination" : "Hyderabad", "travel_date_time": "2020-07-12 05:30 PM", "flexible_timings": false, "flexible_from_date_time" : "", "flexible_to_date_time" : "", "asset_quantity" : 3, "asset_type": "BAG", "asset_type_others" : "", "asset_sensitivity": "HIGH", "deliver_to" : "user1", "phone_number":"1234567890"}'
# url = "http://127.0.0.1:8080/api/lets_ride/asset_request/v1/"
# response = requests.post(url=url,data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)


# #ride_share
# print("-------------ride_share_with_flexible_timmings--------------------\n")
# data = '{"source" : "kurnool", "destination" : "Hyderabad", "travel_date_time": "", "flexible_timings": true, "flexible_from_date_time" : "2020-04-12 05:30 PM", "flexible_to_date_time" : "2020-06-12 05:30 PM", "seats" : 3, "asset_quantity": 4}'
# url = "http://127.0.0.1:8080/api/lets_ride/share_ride/v1/"
# response = requests.post(url=url,data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)


# #ride_share
# print("-------------ride_share--------------------\n")
# data = '{"source" : "kurnool", "destination" : "Hyderabad", "travel_date_time": "2020-06-12 05:30 PM", "flexible_timings": false, "flexible_from_date_time" : "", "flexible_to_date_time" : "", "seats" : 3, "asset_quantity": 4}'
# url = "http://127.0.0.1:8080/api/lets_ride/share_ride/v1/"
# response = requests.post(url=url,data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)



# #share_travel_info
# print("-------------share_travel_info_with_flexible_timings--------------------\n")
# data = '{"source" : "kurnool", "destination" : "Hyderabad", "travel_date_time": "", "flexible_timings": true, "flexible_from_date_time" : "2020-04-12 05:30 PM", "flexible_to_date_time" : "2020-06-12 05:30 PM", "travel_medium" : "BUS", "asset_quantity": 4}'
# url = "http://127.0.0.1:8080/api/lets_ride/share_travel_info/v1/"
# response = requests.post(url=url,data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)


# #share_travel_info
# print("-------------share_travel_info--------------------\n")
# data = '{"source" : "kurnool", "destination" : "Hyderabad", "travel_date_time": "2020-07-12 05:30 PM", "flexible_timings": false, "flexible_from_date_time" : "", "flexible_to_date_time" : "", "travel_medium" : "BUS", "asset_quantity": 4}'
# url = "http://127.0.0.1:8080/api/lets_ride/share_travel_info/v1/"
# response = requests.post(url=url,data=data, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)


# #my_requests
# print("\n---------------offset=3 and limit=1-----------------------------\n")
# url = "http://127.0.0.1:8080/api/lets_ride/my_requests/v1/?offset=3&limit=1"
# response = requests.get(url=url, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)


#my_requests
# print("\n---------------offset=3 and limit=4-----------------------------\n")
# url = "http://127.0.0.1:8080/api/lets_ride/my_requests/v1/?offset=3&limit=4"
# response = requests.get(url=url, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)

# my_ride_requests

# url = "http://127.0.0.1:8080/api/lets_ride/my_requests/rides/v1/?offset=1&limit=10"
# response = requests.get(url=url, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)


# my_asset_requests

url = "http://127.0.0.1:8080/api/lets_ride/my_requests/assets/v1/?offset=-1&limit=9&sort_key=date_time&sort_value=DESC"
response = requests.get(url=url, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
print(response.content)

# matching_results
# url = "http://127.0.0.1:8080/api/lets_ride/matching_results/v1/?offset=-1&limit=3"
# response = requests.get(url=url, headers={'Content-Type':"application/json", 'Authorization': 'Bearer gq8BtgYdBEIpUmvuxA2YGycsI4CUhz'})
# print(response.content)
