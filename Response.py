import random

def get_response(message: str) -> str:
    
    if message.lower() == 'hello':
        return 'hi'
    
    elif message.lower() == 'hello':
        return 'Hey there!'
    
    elif message.lower() == 'Mina' or 'mina':
        MinaList = ["Wese5", "Eltayeb", "نجسسس", "وصخ", "رخيص"]
        return MinaList[random.randint(1, 6)]
    
    elif message.lower() == '!help':
        return '`This is a help message that you can modify.`'
    
    else:
        return None
