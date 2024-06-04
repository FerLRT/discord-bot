from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully quiet today'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return choice(['I am doing well, thank you', 'I am doing great, how about you?'])
    elif 'bye' in lowered:
        return 'Goodbye! Have a great day!'
    elif 'roll dice' in lowered:
        return f'You rolled a {randint(1, 6)}!'
    else:
        return choice(['I am not sure what you mean', 
                       'I am not able to respond to that', 
                       'I am sorry, I do not understand that'])