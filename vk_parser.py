import string
from dotenv import load_dotenv
import os
import vk
from datetime import datetime



#Getting senitive info from environment variables
load_dotenv()
token = os.getenv("API_TOKEN")
user = os.getenv("USER_ID")

#Getting friends list from Vk.com for specific user.
#For now user_id have to be int. 
#There is a way in vk api to use domain name, but for me did not work correctly atm ;(
api=vk.API(access_token=token, v=5.131)
data = api.friends.get(user_id = user, offset = 0, fields = "bdate" )
raw_data = data["items"]

#Getting present day and month as string
present_day = datetime.now().strftime("%d")
present_month = datetime.now().strftime("%m")

#Getting users bdate represented same as present day for comparsion
def date_uniform(bdate: string) -> str:
    date_helper = bdate.split(".")
    if len(date_helper) > 2:
        date_helper.pop(2)
    date_done = (f"{date_helper[0].zfill(2)}.{date_helper[1].zfill(2)}")
    return date_done

#Returning cleaned up list of friends, checking if user have confirmed their birthday date
#Global variable "counter" actually doesn't have any use in the bot. Just for statistics 
def get_sorted_list() -> list:
    friends_list_sorted = []
    global counter
    counter = 0
    for friend in raw_data:
        name = friend["first_name"]
        surname = friend["last_name"]
        if "bdate" not in friend.keys(): 
            counter += 1
            continue
        else:
            bdate = date_uniform(friend["bdate"])
        id = friend["id"]
        friends_list_sorted.append({f"{name} {surname}": (bdate, f"vk.com/id{id}")})
    return friends_list_sorted


#Comparing if today is someone's birthday. 
#Returning list cuz it may be multiple dudes 
def is_bdate(present_day: str, present_month: str) -> list:
    bday_party = []
    for friend in get_sorted_list():
        for key in friend:
            bdate = friend[key][0].split(".")
            if present_day == bdate[0] and present_month == bdate[1]:
                bday_party.append(friend)
    return bday_party



#Getting message for bot to send
def get_message(friends_list_sorted: list) -> str:
    bday_party = is_bdate(present_day, present_month)
    if len(bday_party) == 0:
        return ("No one is celebrating birthday today ;(")
    elif len(bday_party) == 1:
        user = "Only one person has a birthday today.\n"
        for friend in bday_party:
            for item in friend:
                user += f"{item} --- {friend[item][1]}\n"   
        return user 
    else:    
        user = f"There is {len(bday_party)} friends celebrating their birthdays today!\n"
        for friend in bday_party:
            for item in friend:
                user += f"{item} --- {friend[item][1]}\n"   
        return user 


friends_list_sorted = get_sorted_list()

#This function just for tracking how many people has/has not specified their birthdays.
#No particular use in the bot 
def print_counter():
        print("-"*47)
        print ("")
        print("Task completed")
        print (f"Specified birth date users: {len(raw_data) - counter}")
        print (f"Unspecified birth date users: {counter}")
        print ("")
        print("-"*47)
        print ("")

#Finally returning prepared message for the bot in to main file.
def result() -> str:
    return f"{get_message(friends_list_sorted)}"











    










