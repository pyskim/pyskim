import os
from os.path import abspath, join
import random

"""
input = a string, the message you want to enter

special_ chars = a dictionary of punctuation marks that is accessed with the query

generate paths = a function that builds dynamic pathing to each character in the query, so that the images can be used in a personalized ransom note
"""

base_punctuation_path = 'app/assets/punctuation_1'

special_chars = {
    '&': f'{base_punctuation_path}/ampersand_1.png',
    '\'': f'{base_punctuation_path}/apostrophe_1.png',
    '*': f'{base_punctuation_path}/asterix_1.png',
    '@': f'{base_punctuation_path}/at_1.png',
    '\"': f'{base_punctuation_path}/doublequote_straight_1.png',
    '!': f'{base_punctuation_path}/exclaimation_1.png',
    '$': f'{base_punctuation_path}/money_1.png',
    '%': f'{base_punctuation_path}/percentage_1.png',
    '.': f'{base_punctuation_path}/period_1.png',
    '#': f'{base_punctuation_path}/pound_1.png',
    '?': f'{base_punctuation_path}/questionmark_1.png',
    ' ': ' ' 
}


def generate_paths(query_string):
    query_string = query_string.lower()
    path_list = []
    for char in query_string:

        rand = random.randint(1, 4)
        base_letter_path = 'app/assets/'
        
        letter = f'{base_letter_path}{char}_{rand}.png'

        if char in special_chars:
            path_list.append(special_chars[char])
            continue

        # error handling - checks if character is alphanumeric or in special characters
        if char.isalnum() == False or char in special_chars:
            raise ValueError(f'Invalid character input: {char}')

        path_list.append(letter)
        
    return path_list

if __name__ == "__main__":       
    query = input('Enter your message here: ')
    try:
        generate_paths(query)

    except ValueError as err:
        print(err)
        
