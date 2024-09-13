import math
import os
import string
from datetime import datetime
import random

with open('top_english_nouns_lower_100000.txt', 'r') as file:
    nouns = file.read().splitlines()
class PasswordGenerator:
    def __init__(self, nouns):
        self.nouns = nouns
    
    def gen_mem_password(self, num_words=3, case='lower'):
        try:
            if len(self.nouns) < num_words:
                raise ValueError('Not enough words in the list')
            
            words = random.sample(self.nouns, num_words)
            if case == 'upper':
                words = [word.upper() for word in words]    
            elif case == 'title':
                words = [word.title() for word in words]
            memorable_password = '-'.join(word + str(random.randint(0, 9)) for word in words)
            return memorable_password
        except Exception as e:
            print(f'Error: {e}')
            return None

    def gen_ran_password(self, length=12, include_punctuation=True, exclude_characters=''):
        try:
            characters = string.ascii_letters + string.digits + string.punctuation
            if include_punctuation:
                chars = string.ascii_letters + string.digits + string.punctuation
            else:
                chars = string.ascii_letters + string.digits
            ran_password = ''.join(random.choice(chars) for i in range(length))
            return ran_password
        except Exception as e:
            print(f'Error: {e}')
            return None
    
    def log_password(self, password, password_type):
        try:
            filename = f"Generated_Passwords_{password_type}.txt"
            if not os.path.exists(filename):
                os
            with open(filename, 'a') as file:
                timestamp = datetime.now().strftime('%A, %d %B %Y %H:%M:%S')
                file.write(f"{timestamp} - {password}\n")
        except Exception as e:
            print(f'Error: {e}')

            
        pass_gen = PasswordGenerator(nouns)
    
        mem_password = pass_gen.gen_mem_password(num_words=4, case='title')
        if mem_password:
            print(f'Memorable Password: {mem_password}')
            pass_gen.log_password(mem_password, 'memorable')
        else:
            print('Memorable Password could not be generated')
        
        random_password = pass_gen.gen_ran_password(length=16, include_punctuation=True)
        if random_password:
            print(f'Random Password: {random_password}')
            pass_gen.log_password(random_password, 'random')
        else:
            print('Random Password could not be generated')
        print('Check if passwords are saved in the file')
        for password_type in ['memorable', 'random']:
            filename = f"Generated_Passwords_{password_type}.txt"
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    print(f'Passwords in {filename}:')
                    print(file.read())
            else:
                print(f'No passwords saved in {filename}')
        
        


