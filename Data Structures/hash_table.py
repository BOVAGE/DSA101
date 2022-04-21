class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        return index % self.MAX

    def __getitem__(self, key):
        index = self.get_hash(key)
        for idx, item in enumerate(self.arr[index]):
            if item[0] == key:
                return item[1]

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        for idx, item in enumerate(self.arr[index]):
            if item[0] == key:
                self.arr[index][idx] = (key, value)
                return
        self.arr[index].append((key,value))

    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, item in enumerate(self.arr[index]):
            if item[0] == key:
                del self.arr[index][idx]
                return

if __name__ == '__main__':
    h = HashTable()
    print(h.arr)
    h['march 6'] = 123
    h['march 17'] = 17
    h['march 18'] = 18
    h['laqah 1'] = 1
    h['march 6'] = 33
    h['name'] = "Boluwatife"
    print(h.arr)
    del h['march 6']
    print(h['march 6'])
    print(h['laqah 1'])
    print(h.arr)
