# creates a table for using a homophonic cipher

from random import randint
from letter_distribution import LangData

class TableCreator:
    def __init__(self, letter_distribution_percentage, total_percent_in_letter_distribution):
        self.letter_distribution_percentage = letter_distribution_percentage
        self.total_percent_in_letter_distribution = total_percent_in_letter_distribution
        self.homophonic_table = {letter: [] for letter in self.letter_distribution_percentage}

    def create_table(self):
        # create a list with numbers from 0 the sum of percentages in letter_distribution_percentage
        number_list = list(range(self.total_percent_in_letter_distribution))
        number_list = [str(x) for x in number_list] # make the numbers strings strings

        # tilegn hver bokstav ett eller flere tall
        for letter, percentage in self.letter_distribution_percentage.items():
            for i in range(percentage):
                self.homophonic_table[letter].append(number_list.pop(randint(0, len(number_list) - 1))) 
        assert len(number_list) == 0, "list not empty" # sjekk at alle tallene har blitt brukt

    # skriv forholdet mellom bokstavene og tallene til en fil
    def write_table(self):
        with open("mytable.txt", "w") as f:
            for letter, numbers in self.homophonic_table.items():
                f.write("{}:{}\n".format(letter, ' '.join(numbers)))

    # create a new homophonic substitution table
    def excecute(self):
        self.create_table()
        self.write_table()
        print("\nTable Creator done.")


if __name__ == "__main__":
        langdata = LangData()
        langdata.find_letter_distribution_percentage()

        tableCreator = TableCreator(langdata.letter_distribution_percentage, langdata.total_percent_in_letter_distribution)
        tableCreator.excecute()        
