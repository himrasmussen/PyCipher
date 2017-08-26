# a homophonic cipher
# needs to have a homophoinic letter substitution table
import sys; sys.path.append(".."); sys.path.append("homophonic")

from tkinter import Tk
from tkinter.filedialog import askopenfilename

from homophonic_table_creator import TableCreator
from letter_distribution import LangData

class TableGetter():
        
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
      

if __name__ == "__main__":
    pass
