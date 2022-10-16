import string
from dotenv import load_dotenv
import os
import vk
import csv
import json
load_dotenv()
token = os.getenv("TOKEN")
user = os.getenv("USER_ID")

api=vk.API(access_token=token, v=5.131)
data = api.friends.get(user_id = user, offset = 0, fields = "bdate" )

friends_list = data["items"]
friends_dict = []


def date_uniform(bdate: string):
    date_helper = bdate.split(".")
    if len(date_helper) > 2:
        date_helper.pop(2)
    date_done = (f"{date_helper[0].zfill(2)}.{date_helper[1].zfill(2)}")
    return date_done


with open ("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["First name", "Last name", "Date of Birth", "Link"])

    not_specified_counter = 0

    for friend in friends_list:
        name = friend["first_name"]
        surname = friend["last_name"]
        if "bdate" not in friend.keys(): 
            not_specified_counter += 1
            continue
        else:
            bdate = date_uniform(friend["bdate"])

            print (bdate)
        id = friend["id"]
        writer.writerow([name, surname, bdate, f"vk.com/id{id}"])
        friends_dict.append({f"{name} {surname}": (bdate, f"vk.com/id{id}")})


with open ("data.json", "w") as file:
    json.dump(friends_dict, file)
        

print("--------------")
print("Taks completed")
print (f"Specified birth date users: {len(friends_list) - not_specified_counter}")
print (f"Unspecified birth date users: {not_specified_counter}")
print("--------------")






    








