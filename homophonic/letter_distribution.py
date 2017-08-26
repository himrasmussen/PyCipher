from string import ascii_lowercase
from math import ceil
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#finner fremkomstprosenten av hver bokstav i et språk

class LangData:

        # get word list
        def get_word_list(self):
            print("select your word list (stored in the 'word list' folder")
            Tk().withdraw()
            self.word_list = askopenfilename()

        # find alphabet
        def find_alphabet(self):
            with open(self.word_list) as f:
                return ''.join(list(set(list(filter(lambda x: x.isalpha(), f.read().lower())))))

        # finds the letter distribution in the language
        def find_letter_distribution(self):
                self.alphabet = self.find_alphabet()
                letter_count = {letter:0 for letter in self.alphabet}
                with open(self.word_list) as f:
                    stream = f.read().lower()
                    for letter in self.alphabet: 
                        letter_count[letter] = stream.count(letter)
                num_occurences = sum([x for x in letter_count.values()]) #antall bokstaver i ordlisten

                self.letter_distribution = {letter:0 for letter in self.alphabet}
                self.letter_distribution = {letter:0 for letter in self.alphabet}
                for letter in self.alphabet:
                    self.letter_distribution[letter] = letter_count[letter] / num_occurences * 100
                    self.letter_distribution[letter] = ceil(self.letter_distribution[letter])

                # pga unøyaktighet blir det ikke 100% fremkomst, det blir enten mer eller mindre
                self.total_percent_in_letter_distribution = sum([x for x in self.letter_distribution.values()])

        # main function
        def main(self):
            self.get_word_list()
            self.find_letter_distribution()
            print("Done with distribution analysis")

if __name__ == "__main__":
    langdata = LangData()
    langdata.get_word_list()
    langdata.find_letter_distribution()
    print(langdata.letter_distribution, langdata.total_percent_in_letter_distribution)

