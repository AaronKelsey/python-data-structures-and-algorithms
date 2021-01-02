class HashTable:

    def __init__(self):
        self.size = 32
        self.map = [None] * self.size

    def __get_hash(self, key):
        hash_value = 0

        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def add(self, key, value):
        key_hash = self.__get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.__get_hash(key)

        if key_hash is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.__get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def __str__(self):
        string = ''

        for item in self.map:
            if item is not None:
                string += str(item) + '\n'
        return string


if __name__ == '__main__':
    hash_table = HashTable()

    hash_table.add('London', 10979000)
    hash_table.add('Manchester', 2727000)
    hash_table.add('Birmingham', 2605000)
    hash_table.add('Bristol', 680000)
    hash_table.add('Liverpool', 905000)

    print('UK City Populations')
    print(hash_table)

    hash_table.delete('Bristol')
    hash_table.delete('Manchester')

    print('UK City Populations - after removal of two')
    print(hash_table)

    print(f'London population: ' + str(hash_table.get('London')))
