'''
Nombre: Pedro Arriola
Carnet: 20188
Inciso 3
'''

def string_to_base64(text):
    # Convertir texto a binario
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    
    # Rellenar con ceros a la derecha para que sea múltiplo de 6
    while len(binary_text) % 6 != 0:
        binary_text += '0'
    
    # Dividir el texto binario en grupos de 6 bits
    groups_of_six = [binary_text[i:i+6] for i in range(0, len(binary_text), 6)]
    
    # Convertir cada grupo de 6 bits a decimal y luego a Base64 según la tabla de codificación
    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_text = ''.join(base64_table[int(group, 2)] for group in groups_of_six)
    
    # Agregar padding de '=' si es necesario
    while len(base64_text) % 4 != 0:
        base64_text += '='
    
    return base64_text

'''
Testing section
'''

print("\n------- INCISO 3 -------\n")

# Ejemplos de conversión a Base64
test_string_1 = 'Hola, mundo!'
test_string_2 = 'Python es genial'
test_string_3 = 'Amo a los gatos'

base64_1 = string_to_base64(test_string_1)
base64_2 = string_to_base64(test_string_2)
base64_3 = string_to_base64(test_string_3)

print(f"Base64 de '{test_string_1}': {base64_1}")
print(f"Base64 de '{test_string_2}': {base64_2}")
print(f"Base64 de '{test_string_3}': {base64_3}\n")