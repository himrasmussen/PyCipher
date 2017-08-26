# a homophonic cipher
# needs to have a homophoinic letter substitution table

import copy
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from cryptobase import CryptoBase
from homophonic_table_creator import TableCreator
from letter_distribution import LangData

class HomophonicCipher(CryptoBase):
    def __init__(self, *args, **kwargs):
        self.has_table = None
        self.key_backup = {}
        super(HomophonicCipher, self).__init__(*args, **kwargs)
        
    # check if the user has a homophonic substitution table and act accordingly
    def does_user_have_the_table(self):
        choices = ["no", "yes"]
        print("Do you have a homophonic substitution table?")
        for idx, choice in enumerate(choices):
            print("{}: {}".format(idx, choice))
        self.has_table = choices[int(input("Enter a number please: "))] # yes or no
        
    # if user has table, use it, else make it
    def get_or_make_table(self): 

        # if the user has the table, ask for the absolute path to it
        if self.has_table == "yes":
            
            # create a file explorer windows for user to select the key file
            print("Select your homophonic substitution table")
            Tk().withdraw() # remove excess windows
            self.key_file = askopenfilename() # opens a dialog
        else:
            print("You now select your language word list")
            langdata = LangData()
            langdata.main()            
            TableCreator(langdata.letter_distribution).excecute()
            self.has_table = "yes"
            self.get_or_make_table()

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



