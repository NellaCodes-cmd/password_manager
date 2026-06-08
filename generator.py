import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_symbols=True, use_numbers=True):
        self.length = length
        self.use_symbols = use_symbols
        self.use_numbers = use_numbers

    def generate(self):
        characters = string.ascii_letters  # a-z and A-Z always included

        if self.use_numbers:
            characters += string.digits  # adds 0-9

        if self.use_symbols:
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        #Make sure at least one of each required type is included
        password = []

        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.ascii_lowercase))

        if self.use_numbers:
            password.append(random.choice(string.digits))

        if self.use_symbols:
            password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))

        #Fill the rest randomly
        while len(password) < self.length:
            password.append(random.choice(characters))

        #Shuffle so the guaranteed characters aren't always at the start
        random.shuffle(password)

        return "".join(password)