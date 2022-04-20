class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        return index % self.MAX

    def __getitem__(self, key):
        index = self.get_hash(key)
        return self.arr[index]

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.arr[index] = value

if __name__ == '__main__':
    h = HashTable()
    h['name'] = "Boluwatife"
    print(h['name'])
