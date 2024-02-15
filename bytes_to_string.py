'''
Nombre: Pedro Arriola
Carnet: 20188
Inciso 2
'''

def bytes_to_string(bytes_list):
    ascii_list = [int(byte, 2) for byte in bytes_list]
    return ''.join(chr(ascii_char) for ascii_char in ascii_list)

'''
Testing section
'''

print("\n------- INCISO 2 -------\n")

# Example bytes representing Spanish words
test_bytes_1 = ['01101101', '01100001', '01101101', '01100001']  # 'mama'
test_bytes_2 = ['01101000', '01101111', '01101100', '01100001']  # 'hola'
test_bytes_3 = ['01110000', '01100101', '01110010', '01110010', '01101111']  # 'perro'


text_1 = bytes_to_string(test_bytes_1)
text_2 = bytes_to_string(test_bytes_2)
text_3 = bytes_to_string(test_bytes_3)

print(f"Representación de texto de bytes '{test_bytes_1}': {text_1}")
print(f"Representación de texto de bytes '{test_bytes_2}': {text_2}")
print(f"Representación de texto de bytes '{test_bytes_3}': {text_3}\n")