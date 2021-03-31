Instagram Automation Bot
Send message and Post on your instagram
!!!!!! Install instabot (pip install instabot)
Give correct credentials of your instagram
REMEMBER>>>>>
1. If you want to run this code over and over again make your yoou have deleted items from config file except log.
If you did not delete the program will not run and show cookie error.
2. After uploading an image make your your visit the program folder to see your log
!!!Warning!!!!
Using this bot often will affect your Instagram Account!
'''

from instabot import Bot

bot = Bot()
bot.login(username="username",password="password") # Put your username & password

bot.upload_photo("img.jpg", caption="your caption")

bot.send_message("your message", ['username']) # Put receiver username
