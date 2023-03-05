import random

def get_response(message: str, attendees) -> str:
    
    if message.lower() == 'hello':
        return 'Hey there!'
    
    elif message.lower() == 'list members':
        attend = ', '.join(list(attendees.keys()))
        return attend
    
    elif message.lower() == 'help':
        return "There are 2 ways to set attendance: \n1. Upload the QR code and the Person's name. \n2. Use the 'AL:' (link here) , 'Person'.\n \n if you need an example TYPE: 'Show'."
         
    elif message.lower() == 'mina':
        MinaList = ["Hala","Wese5", "Eltayeb", "نجسسس", "وصخ", "رخيص", "Btk"]
        return MinaList[random.randint(1, 5)]
    
    elif message.lower() == 'show':
        return "There are 2 ways to set attendance: \n1. 'upload Pic' 'Mina'. \n2. AL: https://e-learning.msa.edu.eg/mod/attendance/attendance.php?qrpass=b50zfz&sessid=687603 , Mina."
    
