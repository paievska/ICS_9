class Number:
    def __init__(self, *args):
        self.value = list(args)
    def __repr__(self):
        return str(self.value)
    def __getitem__(self, item):
        if 0<=item<len(self.value):
            return self.value[item]
        else:
            raise IndexError ("Індекс за межами заданої множини")
    def __setitem__(self, key, value):
        if 0<=key<len(self.value):
            self.value[key] = value
        else:
            raise IndexError ("Індекс за межами заданої множини")

    def __delitem__(self,key):
        if 0<=key<len(self.value):
            del self.value[key]
        else:
            raise IndexError ("Індекс за межами заданої множини")    



        
b = Number(1, 2, 3, 4, 6)
del b[2]
print(b)



