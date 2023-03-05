import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
import cv2
import qrcode
from Response import get_response
import random


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

attendees = {
    "1": {"username": "211777", "password": "ergerg"},
    "2": {"username": "213009", "password": "ergerg"},
    "3": {"username": "210439", "password": "3ergerg"},
    "4": {"username": "user3", "password": "pass3"},
}

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if len(message.attachments) > 0:
        download_path = r"C:\Users\youss\Desktop\My Crap\Geek Mode\Projects\Coding Projects\My Personal Projects\Automation Projects\Auto-Attendance Recorder\QRDumpFile"
        os.makedirs(download_path, exist_ok=True)
        for file_name in os.listdir(download_path):
            file_path = os.path.join(download_path, file_name)
            try:
                if os.path.isfile(file_path):
                    _, ext = os.path.splitext(file_path)
                    if ext.lower() not in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
                        os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print("Failed to delete {file_path}")
        for attachment in message.attachments:
            file_name = attachment.filename
            download_location = os.path.join(download_path, file_name)
            await attachment.save(download_location)
            img = cv2.imread(download_location)
            qr_detector = cv2.QRCodeDetector()
            data, bbox, _ = qr_detector.detectAndDecode(img)
            if bbox is not None:
                link = data
                member = message.content
                if member != "":
                    notify = "Attendance Link: " + link + " For " + member + "\n \nPLEASE CONFIRM IF THE LINK IS CORRECT, If so, you are all set!"
                    await message.channel.send(notify)
                    print("Member: ",member)
                    print("link: " ,link)
                    #AddAttendance(link,member)
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
                        continue_button = driver.find_element("xpath","//input[@value='Continue']")
                        continue_button.click()
                        username = attendees[member]["username"]
                        password = attendees[member]["password"]
                        username_field = driver.find_element("name",'username')
                        password_field = driver.find_element("name",'password')
                        username_field.send_keys(username)
                        password_field.send_keys(password)
                        login_button = driver.find_element("xpath","//input[@value='Log in']")
                        login_button.click()
                        # if driver.find_element("xpath","//i[@title='Error']"):
                        #     await message.channel.send("Couldn't submit attendance for " + member)  
                        time.sleep(3)

                        if member == "Mina": 
                            member = member + " Wese5"
                        if member == "Marzouki":
                            member = member + " 🥚🥚"
                        try:
                            await message.channel.send("Attendance submitted for " + member)
                        except NoSuchElementException:
                            await message.channel.send("Couldn't submit attendance for " + member)
                        
                        driver.close()
                        
                elif member == "" :
                    notify = ["Are you fucking Dumb","Fucking Moron, add the guy","Add the fucking guy u want to submit the attendance for, reupload the image.", "please add the person you want to set attendance for with the image."]
                    await message.channel.send(notify[random.randint(0,3)])
            else:
                await message.channel.send("Attendance Link NOT Detected, need a clear img BITCH") 
                
    elif message.content.startswith('AL:'):
        link = message.content.split(',')[0].split(': ')[1].strip()
        member = message.content.split(',')[1].strip()
        #AddAttendance(link,member)
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
            continue_button = driver.find_element("xpath","//input[@value='Continue']")
            continue_button.click()
            username = attendees[member]["username"]
            password = attendees[member]["password"]
            username_field = driver.find_element("name",'username')
            password_field = driver.find_element("name",'password')
            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button = driver.find_element("xpath","//input[@value='Log in']")
            login_button.click()
            # if driver.find_element("xpath","//i[@title='Error']"):
            #     await message.channel.send("Couldn't submit attendance for " + member)  
            time.sleep(3)

            if member == "Mina": 
                member = member + " Wese5"
            if member == "Marzouki":
                member = member + " 🥚🥚"
            try:
                await message.channel.send("Attendance submitted for " + member)
            except NoSuchElementException:
                await message.channel.send("Couldn't submit attendance for " + member)
            
            driver.close()
            
    else:
        response = get_response(message.content, attendees)
        if response:
            await message.channel.send(response)
          
            
client.run('use ur own')
