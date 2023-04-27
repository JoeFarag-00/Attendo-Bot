import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options  
import time
import os
import cv2
import qrcode
from Response import get_response
import random

chrome_options = Options()  
chrome_options.add_argument("--headless")  

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

attendees = {
    "Joe": {"username": "234234", "password": "REGEERG"},
    "user2": {"username": "2344423", "password": "ERGERG9"},
    "helo": {"username": "234342", "password": "3GERGEGaRG!"},
    # "dmada": {"username": "23423423", "password": "pass3"},
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
                    notify = "Attendance Link: " + link + " For " + member + "\n \nPLEASE CHECK IF THE LINK GENERATED IS CORRECT, If so, please wait, Im adding your attendance..."
                    await message.channel.send(notify)
                    print("Member: ",member)
                    print("link: " ,link)
                    #AddAttendance(link,member)
                    attendct = 0
                    NaughtyList = []
                    ConfirmList = []
                    AllList = []

                    for CAttendee in attendees.keys():
                       AllList.append(CAttendee)
                    
                    ConfirmAll = ', '.join(AllList)

                    if member == "All" or member == "all":
                        for attendee in attendees:
                            try:
                                driver = webdriver.Chrome()
                                driver.get(link)
                                try:
                                    continue_button = driver.find_element("xpath","//input[@value='Continue']")
                                    continue_button.click()
                                except NoSuchElementException:
                                    print("Continue Exception Handled")
                                username = attendees[attendee]["username"]
                                password = attendees[attendee]["password"]
                                username_field = driver.find_element("name",'username')
                                password_field = driver.find_element("name",'password')
                                username_field.send_keys(username)
                                password_field.send_keys(password)
                                login_button = driver.find_element("xpath","//input[@value='Log in']")
                                login_button.click()
                                time.sleep(3)
                                if not driver.find_elements(By.ID, "loginerrormessage"):
                                    attendct+=1
                                    ConfirmList.append(attendee)
                                else:
                                    NaughtyList.append(attendee)
                                
                                driver.close()  

                            except NoSuchElementException:
                                pass
                            
                        if(len(attendees) == attendct):
                            await message.channel.send("Attendance submitted for All Members: " + ConfirmAll)
                        else:
                            await message.channel.send("Attendance submitted for ONLY:" + str(ConfirmList))
                            await message.channel.send("Couldn't Submit Attendance For " + str(NaughtyList))                           
                                
                    elif member in attendees:
                        try:
                            driver = webdriver.Chrome()
                            driver.get(link)          
                            # time.sleep(3)
                            try:
                                continue_button = driver.find_element("xpath","//input[@value='Continue']")
                                continue_button.click()
                            except NoSuchElementException:
                                print("Continue Exception Handled")
                             
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

                            if not driver.find_elements(By.ID, "loginerrormessage"):    # verify = driver.find_element("name",'This session is not currently available for self-marking')
                                await message.channel.send("Attendance submitted for " + member + ", Thank You ❤️")
                            else:
                                await message.channel.send("Couldn't Submit Attendance For " + member)
                                
                        except NoSuchElementException:
                            await message.channel.send("Couldn't submit attendance for " + member)
                        
                        driver.close()
                    else:
                        notify = ["Are you fucking Dumb? enter the correct name, use 'List Members' if you forgot.","Fucking Moron, add the correct guy, use 'List Members' if you forgot your friend's name.","Add the correct name of the guy u want to submit the attendance for, use 'List Members' ", "please add the correct person you want to set attendance, use 'List Members'"]
                        await message.channel.send(member + " Does Not Exist")
                        await message.channel.send(notify[random.randint(0,3)])
                        
                elif member == "" :
                    notify = ["Are you fucking Dumb","Fucking Moron, add the guy","Add the fucking guy u want to submit the attendance for, reupload the image.", "please add the person you want to set attendance for with the image."]
                    await message.channel.send(notify[random.randint(0,3)])
                    
            else:
                await message.channel.send("Attendance Link NOT Detected or wrong, need a CLEAR IMAGE BITCH")
               
    elif message.content.startswith('AL:'):
        link = message.content.split(',')[0].split(': ')[1].strip()
        member = message.content.split(',')[1].strip()
        #AddAttendance(link,member)
        attendct = 0
        NaughtyList = []
        ConfirmList = []
        AllList = []
        for CAttendee in attendees.keys():
            AllList.append(CAttendee)
        ConfirmAll = ', '.join(AllList)

        if member == "All" or member == "all":
            for attendee in attendees:
                try:
                    driver = webdriver.Chrome()
                    driver.get(link)
                    try:
                        continue_button = driver.find_element("xpath","//input[@value='Continue']")
                        continue_button.click()
                    except NoSuchElementException:
                        print("Continue Exception Handled")
                    username = attendees[attendee]["username"]
                    password = attendees[attendee]["password"]
                    username_field = driver.find_element("name",'username')
                    password_field = driver.find_element("name",'password')
                    username_field.send_keys(username)
                    password_field.send_keys(password)
                    login_button = driver.find_element("xpath","//input[@value='Log in']")
                    login_button.click()
                    time.sleep(3)
                     
                    if not driver.find_elements(By.ID, "loginerrormessage"):
                        attendct+=1
                        ConfirmList.append(attendee)
                    else:
                        NaughtyList.append(attendee)
                    
                    driver.close()  

                except NoSuchElementException:
                    pass
                
            if(len(attendees) == attendct):
                await message.channel.send("Attendance submitted for All Members: " + ConfirmAll)
            else:
                await message.channel.send("Attendance submitted for ONLY:" + str(ConfirmList))
                await message.channel.send("Couldn't Submit Attendance For " + str(NaughtyList))                        
                                
        elif member in attendees:
            try:
                driver = webdriver.Chrome()
                driver.get(link)          
                try:
                    continue_button = driver.find_element("xpath","//input[@value='Continue']")
                    continue_button.click()
                except NoSuchElementException:
                    print("Continue Exception Handled")
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
                    member = member + "🥚🥚"
                if member == "Pola":
                    member = member + "🚲"
            
                if not driver.find_elements(By.ID, "loginerrormessage"):    # verify = driver.find_element("name",'This session is not currently available for self-marking')
                    await message.channel.send("Attendance submitted for " + member + ", Thank You ❤️")
                else:
                    await message.channel.send("Couldn't Submit Attendance For " + member)
                    
            except NoSuchElementException:
                await message.channel.send("Couldn't Submit Attendance For " + member)
            driver.close()  
            
        elif member == "" :
            notify = ["Are you fucking Dumb? resend the command with the name of the person.","Fucking Moron, add the guy. ","Add the fucking guy u want to submit the attendance for, then resend the message, use 'List Members' if you forgot your friend's name.", "Please add the person you want to set attendance for with the link, use use 'List Members'."]
            await message.channel.send(notify[random.randint(0,3)])
        else:
            notify = ["Are you fucking Dumb? enter the correct name, use 'List Members' if you forgot.","Fucking Moron, add the correct guy, use 'List Members' if you forgot your friend's name.","Add the correct name of the guy u want to submit the attendance for, use 'List Members' ", "please add the correct person you want to set attendance, use 'List Members'"]
            await message.channel.send(member + " Does Not Exist")
            await message.channel.send(notify[random.randint(0,3)])
    
    else:
        response = get_response(message.content, attendees)
        if response:
            await message.channel.send(response)
           
client.run('use ur own API')
