import os, sys
print('Pakages Installing Started')
os.system('pkg update && upgrade')
os.system('pip install cpython')
os.system('pip install licensing')
os.system('pip install telethon')
os.system("cls" if os.name=='nt' else 'clear')
print ('All Pakages Installed Successfully')