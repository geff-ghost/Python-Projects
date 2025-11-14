
phone_numbers = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-8765",
    "Diana": "555-4321",
    'Aakash': '555-0001',
    'Siddhanth': '555-0002',
}

data_list = [None] * 4089

def get_index(data_list, a_string):
    result = 0
    for char in a_string:
        a_number = ord(char)
        result += a_number
    return result % len(data_list)


for name, number in phone_numbers.items():
    index = get_index(data_list, name)
    data_list[index] = (name, number)
    print(f"Stored ({name}, {number}) at index {index}")

print("\nRetrieving values from the hash table:")
key, value = data_list[get_index(data_list, 'Alice')]
print(f"Retrieved ({key}, {value}) for 'Alice'")

print("\nAll keys in the hash table:")
keys = [kv[0] for kv in data_list if kv is not None]
print("All keys :", keys)

