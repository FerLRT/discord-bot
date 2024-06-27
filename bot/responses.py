import os
from dotenv import load_dotenv
from random import choice

# Load bad words from the .env file
load_dotenv()
BAD_WORDS_STR = os.getenv('BAD_WORDS', '')
bad_words = [word.strip() for word in BAD_WORDS_STR.split(',')] if BAD_WORDS_STR else []

def get_response(user_input: str, username: str) -> str:
    lowered = user_input.lower().strip()

    # Check for bad words
    for word in bad_words:
        if word in lowered:
            return detected_bad_word(username)
        
    # Check for the rock-paper-scissors game command
    if lowered in ['piedra', 'papel', 'tijera']:
        return play_rock_paper_scissors(lowered)

def detected_bad_word(message_author: str) -> str:
    return f"Eh {message_author.mention}, cuida tu lenguaje!"

def play_rock_paper_scissors(user_choice: str) -> str:
    choices = ['piedra', 'papel', 'tijera']
    bot_choice = choice(choices)
    result = ''

    if user_choice == bot_choice:
        result = '¡Empate!'
    elif (user_choice == 'piedra' and bot_choice == 'tijera') or (user_choice == 'papel' and bot_choice == 'piedra') or (user_choice == 'tijera' and bot_choice == 'papel'):
        result = '¡Ganaste!'
    else:
        result = '¡Perdiste!'

    return f'Tú escogiste {user_choice}, yo escogí {bot_choice}. **{result}**'
