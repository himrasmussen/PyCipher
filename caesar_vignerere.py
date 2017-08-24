import operator
from cryptobase import CryptoBase


class Caesar_Vignerere(CryptoBase):
        def __init__(self, *args, **kwargs):
                super(Caesar_Vignerere, self).__init__(*args, **kwargs)

        def excecute(self):
                if self.mode == "encrypt":
                    self.operator = operator.add
                elif self.mode == "decrypt":
                    self.operator = operator.sub

                self.key_idx = 0
                for char in self.msg:
                        if char in self.alphabet:
                                char_value = self.alphabet.index(char)
                                key_value = self.alphabet.index(self.key[self.key_idx % len(self.key)])
                                new_char_value = self.operator((self.alphalen + char_value), key_value) % self.alphalen
                                self.new_msg += self.alphabet[new_char_value]
                                self.key_idx += 1
                        else:
                                 self.new_msg += char
                self.done()

if __name__ == "__main__":
        thekey = "longstring"
        encrypt = Caesar_Vignerere(msg="it's a nice day for a walk", key=thekey, mode="encrypt")

        encrypt.excecute()
        print(encrypt.new_msg)

        decrypt = Caesar_Vignerere(msg=encrypt.new_msg, key=thekey, mode="decrypt")
        decrypt.excecute()
        print(decrypt.new_msg)
