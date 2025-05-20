from utils.hashtable import HashTable
import json

class JsonProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.hash_table = HashTable(10)

    def write_data(self, date_str, value):
        self.hash_table.insert(date_str, value)
        data = {}
        for index in range(self.hash_table.capacity):
            current = self.hash_table.table[index]
            while current:
                data[current.key] = current.value
                current = current.next
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def read_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            for key, value in data.items():
                self.hash_table.insert(key, value)
            return data
        except FileNotFoundError:
            return {}

