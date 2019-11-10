import discord
import json
import os
import math
from textblob import TextBlob


global users
client = discord.Client()


with open('auth/token.txt', 'r') as file:
    token = file.read().strip('\n\r\s')


def safe_load_json(path):
    if os.path.isfile(path):
        with open(path, 'r') as file:
            data = json.load(file)
            file.close()
            return data
    return dict()

@client.event
async def on_ready():
    global users
    try:
        print(client.user.name)
        print(client.user.id)
        users = safe_load_json('userdata.json')
        for user in client.users:
            print(user.id)
            print(type(user.id))
            print(str(user.id))
            if(str(user.id) not in users):
                print("user id " + str(user.id) + " not in users")
                users[str(user.id)] = {
                    'name': user.name, 
                    'id': user.id, 
                    'score': 0,
                    'total_messages': 0
                    }
        
    except Exception as e:
        print(e)
        return e

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if(message.content.startswith('!score')):
            mention_list = message.mentions
            if(len(mention_list) > 1):
                await message.channel.send('Too many users specified.')
            elif(len(mention_list) == 0):
                await message.channel.send('No user specified')
            else:
                user = mention_list[0]
                score = round(users[str(user.id)]['score'] / users[str(user.id)]['total_messages'] * 100, 2)
                await  message.channel.send(user.name + "'s" + ' behaviour score is: ' + str(score))
        

        else:
            update_score(message)
            return

def update_score(message):
    global users
    # if(message.author.id in users):
    print('user found')
    save_score(message)
    with open('userdata.json', 'wt') as file:
        json.dump(users, file)

            
    return

def save_score(message):
    global users
    message_score = TextBlob(message.content).sentiment.polarity
    users[str(message.author.id)]['total_messages'] += 1
    users[str(message.author.id)]['score'] += message_score
    

def run_bot():
    client.run(token)

if __name__ == '__main__':
    run_bot()