import telebot
import os
tok="6011914153:AAHUdtuEM6Spdh5yHB2SrKtI8Ms-YNtGj9o" 
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start']) 
def welcome(message) :
    bot.send_message(message.chat.id, "welcome  File decryption sks nm ") 

@bot.message_handler(content_types=['document']) 

def post(message):
    print(message) 
    name=message.document.file_name 
    
    id=message.document.file_id
    file_info = bot.get_file(id)
    print(file_info)
    downloaded_file = bot.download_file(file_info.file_path)
    jj=open(name,"wb") 
    jj.write(downloaded_file)
    jj.close()
    os.system('python entrykey.py "'+name+'" > test.txt') 
    jh=open("test.txt").read()
    xx="" 
    bot.reply_to(message, jh+xx) 
    
    
@bot.message_handler(func=lambda message: True) 
def wel(message) :
   if message.forward_from == None :
      if message.reply_to_message == None:
         bot.forward_message("@group1private", message.chat.id,message.id)
      else :
         id = message.json["from"]["id"]
         
         bot.send_message(id,message.text)
         
         
   else :
       pass
   
   
   
  
bot.polling() 

