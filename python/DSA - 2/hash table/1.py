class Hash_table:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value



a = Hash_table()
a['name'] = 'Nadeem'
a['age'] = 23
a['weight'] = 71
a['name'] = 'Nahala'
a['age'] = 19
a['weight'] = 46
print(a['name'])
print(a['age'])
print(a['weight'])
print(a.arr)