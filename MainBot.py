import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from Response import get_response

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

Checker = 0;

attendees = {
    "user1": {"username": "211777", "password": "hello"},
    "user2": {"username": "user2", "password": "pass2"},
    "5": {"username": "user3", "password": "pass3"},
    "1": {"username": "user3", "password": "pass3"},
    "2": {"username": "user3", "password": "pass3"},
    "4": {"username": "user3", "password": "pass3"},
}

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('AttendLink:'):
        link = message.content.split(',')[0].split(': ')[1].strip()
        member = message.content.split(',')[1].strip()
        
        if member == "All":
            
            for attendee in attendees:
                driver = webdriver.Chrome()
                driver.get(link)
                continue_button = driver.find_element("xpath","//input[@value='Continue']")
                continue_button.click()
                username = attendees[attendee]["username"]
                password = attendees[attendee]["password"]
                username_field = driver.find_element("name",'username')
                password_field = driver.find_element("name",'password')
                username_field.send_keys(username)
                password_field.send_keys(password)
                login_button = driver.find_element("xpath","//input[@value='Log in']")
                login_button.click()
                time.sleep(5)
                driver.close()
            await message.channel.send("Attendance submitted for all members")
            driver.close()         
        else:
            driver = webdriver.Chrome()
            driver.get(link)          
            time.sleep(3)
            #continue_button = driver.find_element("xpath","//input[@value='Continue']")
            #continue_button.click()
            username = attendees[member]["username"]
            password = attendees[member]["password"]
            username_field = driver.find_element("name",'username')
            password_field = driver.find_element("name",'password')
            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button = driver.find_element("xpath","//input[@value='Log in']")
            login_button.click()
            time.sleep(3)
            
            if member == "Mina": 
                member = member + " Wese5"
            
            # IsLogged = driver.find_element("tag", 'present').is_displayed()
            # print(IsLogged)
            
            # if(IsLogged):
            #     message.channel.send("Attendance submitted for " + member)
            # else:
            #     message.channel.send("Couldn't submit attendance for " + member)
            try:
                await message.channel.send("Attendance submitted for " + member)
            except NoSuchElementException:
                await message.channel.send("Couldn't submit attendance for " + member)
            
            driver.close()
    else:
        response = get_response(message.content)
        if response:
            await message.channel.send(response)
        
    
    

client.run('MTA4MDYzMzA3NjMyNzEyMDkyNw.GE60ZU.3q_VO7a1q4CfxBfrpiOraSspmzfbf2uMI0k6w4')