import string


class CryptoBase:
    def __init__(self, msg, key, mode):
        self.msg = msg.lower()
        self.new_msg = ''
        self.key = key.lower()
        self.key_idx = -1
        self.alphabet = string.ascii_lowercase + "æøå"
        self.alphalen = len(self.alphabet)
        self.operator = -1
        self.mode = mode 
        assert mode in ["encrypt", "decrypt"], "invalid mode"
    
    def done(self):
        print("The message is: {}".format(self.new_msg))

