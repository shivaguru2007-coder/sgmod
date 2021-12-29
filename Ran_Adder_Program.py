from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon import types, utils, errors
import configparser
import sys
import csv
from csv import reader
import traceback
import time
import random
print("    ")
print("AutoConnecting_To_the_Sarver....... <<< Script by MSG SUPPORT >>>    ")
print("     ")
memory_data = []
with open('Program_Data/memory.csv', 'r') as hash_obj:
    csv_reader = reader(hash_obj)
    list_of_rows = list(csv_reader)
    memory_data = list_of_rows[0]
    
delta = int(memory_data[0])

startfrom = int(memory_data[1])
nextstart = startfrom+50

endto = int(memory_data[2])
nextend = endto+50

with open('Program_Data/api.csv', 'r') as api_obj_id:
    csv_reader = reader(api_obj_id)
    data_list_of_rows = list(csv_reader)
    deltaop = data_list_of_rows[delta - 1]
  
    
api_id = int(deltaop[0])
api_hash = str(deltaop[1])


config = configparser.ConfigParser()
config.read("Program_Data/config.ini")
to_group = config['Telegram']['to_channel']

input_file = 'Program_Data/data.csv'
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['srno'] = row[0]
        user['username'] = row[1]
        user['id'] = int(row[2])
    #user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)



    
def autos(mobile_number, startfrom, endto):

    
    
    channel_username = to_group
    phone = utils.parse_phone(mobile_number)

    client = TelegramClient(f"Program_Data/sessions/{phone}", api_id, api_hash)

    client.connect()
    if not client.is_user_authorized():
        print('some thing has changed')
        client.send_code_request(phone)
        client.sign_in(phone, input    ('Enter the code: '))

   
    usernames = []
    for user in users:
        if (int(startfrom) <= int    (user['srno'])) and (int(user['srno']) <= int(endto)):
            status = 'delta'
            if user['username'] == "":
                print("no username, moving to next")
                continue
            else:
                usernames.append(user['username'])
            
                    
    
    for i in range(0, len(usernames)-10, 10):    
        try:
            client(InviteToChannelRequest(channel=channel_username,users=usernames[i:i+10]))    
            status = 'DONE'
            print(status, usernames[i:i+10] )
        
            #print("Waiting for 60-180 Seconds...")
        # time.sleep(random.randrange(1,3))
        
        except UserPrivacyRestrictedError:
            status = 'PrivacyRestrictedError'
            print(status )
            break
            
        
        except UserAlreadyParticipantError:
            status = 'ALREADY'
            print(status )
            break
            
        
        except PeerFloodError as g:
            status = 'PeerFloodError :('
            print('Script Is Stopping Now, Dont Use This Account For The Next 24 Hours')
            time.sleep(86400)
 
        except ChatWriteForbiddenError as cwfe:
            client(JoinChannelRequest(channel_username))
            print("Self Number Joined")
            continue
            
        except errors.RPCError as e:
            status = e.__class__.__name__
            print(status)
            continue


        except Exception as d:
            status = d
            print(d)
            break

        except:
            traceback.print_exc()
            print("Unexpected Error")
            continue
        
        
    # channel_connect = client.get_entity(channel_username)
    # channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
    # countt = int(channel_full_info.full_chat.participants_count)

    # print(f"ADDING {user['name']} TO {channel_username} TOTAL: {countt} - {status}")
    '''
    elif int(user['srno']) > int(endto):
        print("Members Added Successfully!")
        stat = input('Done! more help:https://telegrammemberadder.com      telegram @anooppatel1234 ')
        if stat == '1':
            autos()
        else:
            quit()
    '''
       
    
with open('Program_Data/phone.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    number_list_of_rows = list(csv_reader)   

nextdelta = delta + 1
for i in range(delta,len(number_list_of_rows)):
    phone_number = number_list_of_rows[i-1][0]
    print(phone_number)
    autos(phone_number, startfrom, endto) 
    
    startfrom = startfrom+50
    endto = endto + 50
    nextdelta = i + 1

    with open("Program_Data/memory.csv","w",encoding='UTF-8') as df:#Enter your file name.
        writer = csv.writer(df, delimiter=",", lineterminator="\n")
        writer.writerow([nextdelta,nextstart,nextend])

