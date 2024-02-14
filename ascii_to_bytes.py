'''
Nombre: Pedro Arriola
Carnet: 20188
'''


def string_to_ascii(text):
    
    ascii = [ord(char) for char in text]
    
    return ascii

def ascii_to_bytes(ascii):
    bytes = []
    
    for char in ascii:
        bytes.append(bin(char)[2:].zfill(8))
    
    return bytes


'''
Testing section
'''

# Test strings
test_string_1 = 'mama'
test_string_2 = 'hola'

print("\n------- INCISO 1 -------\n")

ascii_1 = string_to_ascii(test_string_1)
ascii_2 = string_to_ascii(test_string_2)

print(f"Representacion en ascii de '{test_string_1}': {ascii_1}")
print(f"Representacion en ascii de '{test_string_2}': {ascii_1}\n")

byte_1 = ascii_to_bytes(ascii_1)
byte_2 = ascii_to_bytes(ascii_2)

print(f"Representacion en bytes de '{test_string_1}': {byte_1}")
print(f"Representacion en bytes de '{test_string_2}': {byte_2}\n")