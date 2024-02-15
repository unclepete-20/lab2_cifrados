'''
Nombre: Pedro Arriola
Carnet: 20188
Inciso 4
'''

def base64_to_string(base64_text):
    # Crear tabla de codificación Base64
    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Convertir Base64 a binario
    binary_text = ''.join(format(base64_table.index(char), '06b') for char in base64_text if char != '=')
    
    # Rellenar con ceros a la derecha para que sea múltiplo de 8
    while len(binary_text) % 8 != 0:
        binary_text += '0'
    
    # Dividir el texto binario en grupos de 8 bits
    groups_of_eight = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    
    # Convertir cada grupo de 8 bits a decimal y luego a caracter ASCII
    ascii_text = ''.join(chr(int(group, 2)) for group in groups_of_eight)
    
    return ascii_text

'''
Testing section
'''

print("\n------- INCISO 4 -------\n")

# Ejemplos de conversión de Base64 a texto
base64_text_1 = 'SG9sYSwgbXVuZG8h'  # 'Hola, mundo!'
base64_text_2 = 'UHl0aG9uIGVzIGdlbmlhbA=='  # 'Python es genial'
base64_text_3 = 'QW1vIGEgbG9zIGdhdG9z'  # 'Amo a los gatos'

text_1 = base64_to_string(base64_text_1)
text_2 = base64_to_string(base64_text_2)
text_3 = base64_to_string(base64_text_3)

print(f"Texto correspondiente a '{base64_text_1}': {text_1}")
print(f"Texto correspondiente a '{base64_text_2}': {text_2}")
print(f"Texto correspondiente a '{base64_text_3}': {text_3}\n")