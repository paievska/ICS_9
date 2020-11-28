class Words:
    def __init__(self, letters):
        self.letters = letters
 
    def __len__(self):
        return len(self.letters)

        
b = Words('Bob')
print(len(b))



