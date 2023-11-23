import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
import telethon
import random
from random import choices
import time ;import os
from telethon.tl.functions.messages import GetPeerDialogsRequest
from telethon.sessions import StringSession
from config import *

auction = []

band = []

auction.append("vipjz\n")

@StrPython.on(
events.NewMessage(
outgoing=True, pattern=r".صيد"))
async def StrPychecker(event):
        clicks = 1
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        
        type = str(msg[0])
      
        username = await rando(type)
        await event.reply(f"بدء صيد على هذا النوع : {type}")

        while True:
                clicks += 1
                try:
                	os.remove("clicks.txt")
                except :
                	open("clicks.txt","a").write(str(clicks)+"\n")
                else:
                	open("clicks.txt","a").write(str(clicks)+"\n")
                try:
             	   await StrPython(GetPeerDialogsRequest(peers=[username]))
                except Exception as err:
                    if "No user has" in str(err):
                        try:
                        	await StrPython(functions.account.UpdateUsernameRequest(username=username))           
                        
                        	await StrPython.send_file(event.chat_id, "https://t.me/videoThomasvip/22",caption=f'''
𓆩 We are the strongest @illl0 !'
⎱UserName: ❲ @{username} ❳
⎱ClickS: ❲ {clicks} ❳
⎱Save: ❲ Account ❳
⎱By : ❲ 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™ ❳''')
                        	os.remove("clicks.txt")
                        	break
                        except Exception as USFL:
                        	await StrPython.send_message(event.chat_id,f"User is error : @{username}\nError: {USLF}")
                    else:
                        continue                    
                        
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    	await StrPython.send_message(event.chat_id,f"User is band : {username}")
                    	band.append(username)
                    	
                except telethon.errors.rpcerrorlist.UsernameOccupiedError:
                    	time.sleep(1);continue
                    	
                except telethon.errors.rpcerrorlist.FloodWaitError as ses:
                    	await StrPython.send_message(event.chat.id,f"Flood & {ses.seconds}")
                    	
                    	break
                except telethon.errors.rpcerrorlist.UsernamePurchaseAvailableError: 
                    	
                    	auction.append(username+"\n")
                    	
              
                except Exception as Error:
                   await StrPython.send_message(event.chat.id,f"Error in the check : {Error}\nUser is Err : @{username}") 
                   break
                   
       

ban = open("band.txt","r").read().split()
band.append(ban)

kkkahrf = "qwertyuiopassdfghjklzxcvbnm"
kkkarqam = "1234567890"
kkkrnd="qwertyuiopassdfghjklzxcvbnm1234567890"
async def rando(type):
	if type == "1":
		q = random.choices(kkkarqam)
		w = random.choices(kkkarqam)
		k = random.choices(kkkarqam)
		j = random.choices(kkkarqam)
		user = ["vip",q[0],w[0],k[0],j[0]] #vip1234
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "2":
		q = random.choices(kkkahrf)
		w = random.choices(kkkrnd)
		user = [q[0],q[0],w[0],'_',w[0]] #aab_b
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "3":
		q = random.choices(kkkahrf)
		w = random.choices(kkkrnd)
		user = [q[0],"_",w[0],q[0],w[0]] #a_bab
		username = "".join(user)
		
		
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "4":
		q = random.choices(kkkarqam)
		w = random.choices(kkkarqam)
		k = random.choices(kkkarqam)
		j = random.choices(kkkarqam)
		user = ['id',w[0],k[0],j[0]] #id999
		username = "".join(user)
		return username
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "test":
		q = random.choice(abcd)
		w = random.choice(abcd)
		user = [q[0],"b",q[0],"66",q[0],q[0],w[0]] #test
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "5":
		q = random.choice(kkkahrf)
		w = random.choice(kkkrnd)
		user = [q[0],w[0],'_',q[0],q[0]] #ab_aa
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "6":
		q = random.choices(kkkahrf)
		w = random.choices(kkkrnd)
		b = random.choices(kkkrnd)
		user = [q[0],w[0],b[0]] #abcbot
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "7":
		q = random.choices(kkkahrf)
		w = random.choices(kkkrnd)
		user = [q[0],w[0],w[0],w[0],w[0]]
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username

@StrPython.on(events.NewMessage(outgoing=True, pattern=r".الانواع"))
async def Shhtah(event):
	await event.reply(""" 
الانواع : 
1- vip1234
2- aab_b
3- a_bab
4- id123
5- ab_aa
6- abcbot
7- accccbot
8- تسيت للصيد

للصيد ارسل : 
.صيد 1
* الحجز بالحساب يعني فقط تكتب صيد مع رقم اليوزر
By : @g_4_q  ~ @illl0
""")

@StrPython.on(events.NewMessage(outgoing=True, pattern=r".عدد المحاولات"))
async def Shhtah(event):
	try:
		n = open("clicks.txt","r").read()
		
	except:
		await event.reply("الصيد واكف حب")
	else:
		
		await event.reply(f"عدد محاولات : {n}")
	


for x in StrPython.iter_dialogs():
		if x.is_user and not x.entity.bot:
			
				too = x.id				
				try:
					hh=0
				except BaseException:continue
StrPython.send_file("me","https://t.me/videoThomasvip/22",caption=f"""**
 سورس تشيكر  [Team Zero #0](t.me/illl0)

1- vip1234
2- aab_b
3- a_bab
4- id123
5- ab_aa
6- abcbot
7- accccbot

للصيد ارسل : 
.صيد 1
* الحجز بالحساب يعني فقط تكتب صيد مع رقم اليوزر
By **: @g_4_q  ~ @illl0
""")     		     		     		          		     		     		

# Team Zero #0 ~ 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™     		     		     		