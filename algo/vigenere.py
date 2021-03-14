import math
import numpy as np

char_a_code = 65
char_z_code = 90
number_of_letters = 26

def create_vigenere_matrix():
    matrix = np.zeros((number_of_letters, number_of_letters))
    number_of_rows = number_of_letters
    number_of_cols = number_of_letters
    for i in range (number_of_rows):
        for j in range (number_of_cols):
            matrix[i][j] = (i + j) % number_of_letters
    return matrix

vigenere_matrix = create_vigenere_matrix()

"""
Allongement de la cle afin d'obtenir une cle avec une taille egale a celle du texte
"""
def elongate_key(text, key):
    text_len = len(text)
    key_len = len(key)
    elongated_key = ""
    result_key = ""
    key_duplications = 1
    if key_len < text_len:
        key_duplications = math.ceil((text_len - key_len) / key_len) + 1
    for i in range (key_duplications):
        elongated_key += key    
    # Ajout des espaces dans la cle s'il y a des espaces dans le texte + Permet de reduire les lettres en trop de la cle
    char_index_in_elongated_key = 0
    for char in text:
        char_code = ord(char)
        if char_code >= char_a_code and char_code <= char_z_code:
            # Cas ou on a une lettre
            result_key += elongated_key[char_index_in_elongated_key]
            char_index_in_elongated_key += 1
        else:
            # Cas ou on a un espace ou un caractere special qui ne sera pas crypte
            result_key += ' '
    return result_key



def encrypt_or_decrypt_with_matrix(text, key, is_action_to_encrypt=True):
    result = ""
    vigenere_operation = get_crypted_value_from_matrix
    if not is_action_to_encrypt:
        vigenere_operation = get_clear_value_from_matrix
    elongated_key = elongate_key(text, key)
    for i in range (len(text)):
        char_code = ord(text[i])
        if char_code >= char_a_code and char_code <= char_z_code:
            text_char_code = char_code - char_a_code
            key_char_code = ord(elongated_key[i]) - char_a_code
            new_char_code = math.floor(vigenere_operation(vigenere_matrix, text_char_code, key_char_code))
            new_char = chr(new_char_code + char_a_code)
            result += new_char
        else:
            result += text[i]
    return result

def get_crypted_value_from_matrix(matrix, text_char_code, key_char_code):
    return matrix[key_char_code][text_char_code]

def get_clear_value_from_matrix(matrix, text_char_code, key_char_code):
    line = matrix[key_char_code]
    char_code = char_a_code
    line_len = len(line)
    for i in range (line_len):
        current_char_code = line[i]
        if(current_char_code == text_char_code):
            char_code = i
            break
    return char_code

"""
Cree une matrice de taille 26x26 avec les positions des lettres de l'alphabet
Les positions sont entre 0 et 25
"""

def encrypt_or_decrypt_mathematically(text, key, is_action_to_encrypt=True):
    text = text.upper()
    text_len = len(text)
    key = key.replace(" ", "").upper()
    vigenere_operation = -1
    if is_action_to_encrypt:
        vigenere_operation = 1
    elongated_key = elongate_key(text, key)
    result = ""
    for i in range(text_len):
        char_code = ord(text[i])
        if char_code >= char_a_code and char_code <= char_z_code:
            text_char_code = char_code - char_a_code
            key_char_code = ord(elongated_key[i]) - char_a_code
            key_char_code *= vigenere_operation
            new_char_code = (text_char_code + key_char_code) % number_of_letters
            #new_char = vigenere_operation(text_char_code, key_char_code)
            new_char = chr(new_char_code + char_a_code)
            result += new_char
        else:
            result += text[i]
    return result

text = "abcdsc sdcsd"
#print(text)
#print(elongate_key(text, "azertyuiopqsdfghjkllmwxcvbn"))
"""
text = "CHIFFRE DE VIGENERE"
key = "BACHELIER"
result = "DHKMJCM HV WIILRPZI".upper()
x = encrypt_or_decrypt_mathematically(text, key)
print(x)
print(x == result)

print("==============================================")
hidden_text = "KE O HTAMPCF CJLMVVE UBNUVOZ MX ABI XPRRB HVVX CUW"
new_key = "BACHELIER"
clear_text = "JE M APPELLE CHEIKNA DANSOKO ET JAI VINGT DEUX ANS"
y = encrypt_or_decrypt_mathematically(hidden_text, new_key, False)
print(y)
print(y == clear_text)

#print(vigenere("abcdscsdcsd", "ad"))


text = "CHIFFRE DE VIGENERE"
key = "BACHELIER"
result = "DHKMJCM HV WIILRPZI".upper()
x = encrypt_or_decrypt_with_matrix(text, key)
print(text)
print(x)
print(x == result)

print("==============================================")
hidden_text = "KE O'HTAMPCF CJLMVVE UBNUVOZ MX ABI XPRRB HVVX CUW"
new_key = "BACHELIER"
clear_text = "JE M'APPELLE CHEIKNA DANSOKO ET JAI VINGT DEUX ANS"
y = encrypt_or_decrypt_with_matrix(hidden_text, new_key, False)
print(y)
print(y == clear_text)
"""