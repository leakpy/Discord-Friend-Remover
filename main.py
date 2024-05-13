import requests
import time
import fade
import discord
import requests

text = """

  █████▒██▀███   ██▓▓█████  ███▄    █ ▓█████▄     ██▀███  ▓█████  ███▄ ▄███▓ ▒█████   ██▒   █▓▓█████  ██▀███  
▓██   ▒▓██ ▒ ██▒▓██▒▓█   ▀  ██ ▀█   █ ▒██▀ ██▌   ▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒████ ░▓██ ░▄█ ▒▒██▒▒███   ▓██  ▀█ ██▒░██   █▌   ▓██ ░▄█ ▒▒███   ▓██    ▓██░▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█▒  ░▒██▀▀█▄  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌   ▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒█░   ░██▓ ▒██▒░██░░▒████▒▒██░   ▓██░░▒████▓    ░██▓ ▒██▒░▒████▒▒██▒   ░██▒░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ▒ ░   ░ ▒▓ ░▒▓░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒    ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░       ░▒ ░ ▒░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒      ░▒ ░ ▒░ ░ ░  ░░  ░      ░  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
 ░ ░     ░░   ░  ▒ ░   ░      ░   ░ ░  ░ ░  ░      ░░   ░    ░   ░      ░   ░ ░ ░ ▒       ░░     ░     ░░   ░ 
          ░      ░     ░  ░         ░    ░          ░        ░  ░       ░       ░ ░        ░     ░  ░   ░     
                                       ░                                                  ░                   

 """
print(fade.purplepink(text)) 

token = input("Token here: ")

user_token = token

headers = {
    "Authorization": user_token
}

response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)

for friend in response.json():
    # Friend name
    friend_name = friend['user']['username']
    
    response = requests.delete(f"https://discord.com/api/v9/users/@me/relationships/{friend['id']}", headers=headers)

    print(f"Friend : {friend_name}")

# Shows how many friends you have left

response = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
print(f"Friends Left : {len(response.json())}")

print ("https://github.com/truusty")
