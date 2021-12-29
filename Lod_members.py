from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon import types
import sys
import csv
import configparser
import traceback
import time
from telethon.sessions import StringSession

config = configparser.ConfigParser()
config.read("Program_Data/config.ini")
export_phone = config['Telegram']['export_phone']
export_api_id = config['Telegram']['export_api_id']
export_api_hash = config['Telegram']['export_api_hash']
from_group = config['Telegram']['from_channel']


api_id = int(export_api_id)   
api_hash = str(export_api_hash)

phone = int(export_phone)


client = TelegramClient(f"Program_Data/sessions/{phone}", api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print('Fetching Members.........help: youtube.com/MSG_SUPPORT')
all_participants = []

#enter target group or channel
target = from_group

all_participants = client.get_participants(target, aggressive=True)
    

print('Saving In file... ALLDATA.csv')
with open("Program_Data/ALLDATA.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['sr. no.','username', 'user id', 'name', 'group', 'Status'])
    i = 0
    for user in all_participants:
        status = 1

        i += 1
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        if isinstance(user.status, types.UserStatusOnline):
            status = 1
        
        elif isinstance(user.status, types.UserStatusOffline):
            if time.time()-(user.status.was_online).timestamp() <=172800:
                status = 2
            else:
                status = 31634268763763
        
        
        writer.writerow([i,username, user.id, name, target , status])
print('Members Scraped Successfully.')



import csv
import os

print('hello')
lines = list()


def main():
    lines = list()
    with open('Program_Data/ALLDATA.csv', 'r',encoding='UTF-8') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)

            for field in row:

                if field == '':
                    lines.remove(row)
    with open('1.csv', 'w', encoding='UTF-8') as writeFile:
        writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

        writer.writerows(lines)

def main1():
    lines = list()
    with open('1.csv', 'r',encoding='UTF-8') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)

            for field in row:

                if field == 'username':
                    lines.remove(row)
    
    with open('2.csv', 'w', encoding='UTF-8') as writeFile:
        writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")

        writer.writerows(lines)

main()
main1()


with open("2.csv","r",encoding='UTF-8') as source:
    rdr = csv.reader(source)

    with open("Program_Data/data.csv","w",encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])
        i = 0
        for row in rdr:
            i += 1
            writer.writerow((i,row[1], row[2], row[3], row[4], row[5]))
            
            
os.remove("1.csv")
os.remove("2.csv")
#os.remove("unf.csv")
print("Successfully Filtered And Saved In data.csv")