from telethon.sync import TelegramClient
from telethon import utils
import csv
from csv import reader
import configparser
import subprocess,requests,time,os

print("                                  ################# MY SUPER GUIDE ##################          ")
with open('Program_Data/phone.csv','r')as f:
 str_list=[row[0]for row in csv.reader(f)]
 po=0
 for pphone in str_list:
  phone=utils.parse_phone(pphone)
  po+=1
  with open('Program_Data/api.csv','r')as api_obj_id:
   csv_reader=csv.reader(api_obj_id)
   list_of_rows=list(csv_reader)
   row_number=int(po)
   col_number=1
   deltaop=list_of_rows[row_number-1][col_number-1]
  with open('Program_Data/api.csv','r')as hash_obj:
   csv_reader=csv.reader(hash_obj)
   list_of_rows=list(csv_reader)
   row_number=int(po)
   col_number=2
   deltaxd=list_of_rows[row_number-1][col_number-1]
  api_id=int(deltaop)
  api_hash=str(deltaxd)
  print(f"Login {phone}")
  client=TelegramClient(f"Program_Data/sessions/{phone}",api_id,api_hash)
  client.start(phone)
  client.disconnect()
  print()
 done=True
input("Done All Mobile Number Login Successfully!" if done else "Error!")

