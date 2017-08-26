# a homophonic cipher
# needs to have a homophoinic letter substitution table
import sys; sys.path.append(".."); sys.path.append("homophonic")

import copy
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from cryptobase import CryptoBase
from homophonic_table_creator import TableCreator
from letter_distribution import LangData

class HomophonicCipher(CryptoBase):
    def __init__(self, key_file, *args, **kwargs):
        self.key_file = key_file
        super(HomophonicCipher, self).__init__(*args, **kwargs)
        
    # import the homophonic letter substitution table
    def import_substitution_table(self):
        with open(self.key_file) as f:
            self.key = {} 
            table_data_lines = f.read().splitlines()

            # seperate the letter from the numbers on each line
            for line in table_data_lines:
                cur_letter = line[0]       # extract letter
                numbers = line[2:].split() # extract numbers
                self.key[cur_letter] = numbers
            
            # make a backup key for use later
            self.key_backup = copy.deepcopy(self.key)
    # encrypt the message 
    def encrypt(self):

        print(self.msg)
        # encrypt every character in the message
        for char in self.msg:
            if char in self.alphabet: 
                    self.new_msg += self.key[char].pop() if char in self.alphabet else char
                    # if all the numbers for the letter have been used, reinitialize the numbers
                    if not self.key[char]: 
                        self.key[char] = self.key_backup[char]

            self.new_msg += " "
    # decrypt the message 
    def decrypt(self):
        for number in self.msg.split():
            for letter, numbers in self.key.items(): # optimer?
                if number in numbers:
                    self.new_msg += letter 

    # excecute the operation
    def excecute(self, mode):
        if mode == "encrypt":
            self.encrypt()
        elif mode == "decrypt":
            self.decrypt()        
        
        print(self.new_msg)        
        self.done()

if __name__ == "__main__":
    cipher = HomophonicCipher(key="foo", msg="bla bla bla", mode="encrypt")
    cipher.does_user_have_the_table()
    cipher.get_or_make_table()
    cipher.import_substitution_table()
    cipher.excecute(cipher.mode) 


    cipher = HomophonicCipher(key="foo", msg=cipher.new_msg, mode="decrypt")
    cipher.does_user_have_the_table()
    cipher.get_or_make_table()
    cipher.import_substitution_table()
    cipher.excecute(cipher.mode) 



