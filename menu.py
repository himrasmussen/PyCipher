# display menu, list ciphers

class Menu:
        def __init__(self, ciphers):
                self.ciphers = ciphers
                self.modes = ["encrypt", "decrypt"] 

        def get_mode(self):
                print("Select one of the methods (enter number)")
                for idx, mode in enumerate(self.modes):
                        print("{0}: {1}".format(idx, mode))
                self.mode = int(input("Enter a number please: "))
                self.mode = self.modes[self.mode]	

        def get_cipher(self):
                print("Select a cipher please (enter number)")
                for idx, encryption in enumerate(self.ciphers):
                        print("{0}: {1}".format(idx, encryption))
                self.cipher = int(input("Enter a number please: "))
                self.cipher = self.ciphers[self.cipher]	

        def get_key(self): # if homophonic: popup file explorer for key file selection
            if self.cipher != "homophonic substitution":
                self.key = input("Enter your key please: ")

        def get_msg(self):
            # legg til mulighet for å velge en fil
            self.msg = input("Enter your message please: ")

        def main(self):
            self.get_mode()
            self.get_cipher()
            self.get_key()
            self.get_msg()
            print("\nMenu done.")

if __name__ == "__main__":
        menu = Menu(["ceasar", "binary", "foo"])
        menu.main() 
