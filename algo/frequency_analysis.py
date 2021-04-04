import numpy as np

char_a_code = 65
char_z_code = 90

# Tableau de lettres trié avec les letres les plus frequentes d'abord
letters_by_descending_frequency = ["E", "A", "I", "S", "T", "N", "R", "U", "L", "O", "D", "M", "P", "C", "V", "Q", "G", "B", "F", "J", "H", "Z", "X", "Y", "K", "W"]

"""
Initialisation d'un dictionnaire qui associe 0 a chaque lettre.
dictionnaire = {A:0, B:0, C:0,...., Y:0, Z:0}
"""
def init_letters_dict():
    frequency_dict = {}
    for i in range (char_a_code, char_z_code+1):
        char = chr(i)
        frequency_dict[char] = 0
    return frequency_dict

def frequency(text):
    number_of_letters = 0
    text = text.replace(" ", "")
    frequency_dict = init_letters_dict()
    # Nombre d'occurences des nombres
    for character in text:
        if character in frequency_dict:
            frequency_dict[character] += 1
            # On ne recupere que les lettres et non les caracteres speciaux
            number_of_letters += 1
    # Ajout des pourcentages
    frequency_with_percentages = []
    for (x,y) in frequency_dict.items():
        if y > 0:
            percentage = (y / number_of_letters) * 100
            t = (x, y, round(percentage,2))
            frequency_with_percentages.append(t)
    # Tri des elements dans l'ordre décroissant
    sorted_list = sorted(frequency_with_percentages, key=lambda x: x[1], reverse=True) 
    return sorted_list

def get_most_probable_decryption(text):
    result = ""
    text = text.upper()
    letters_repartition_descending_order = frequency(text)
    size = len(letters_repartition_descending_order)
    for char in text:
        char_code = ord(char)
        current_char = char
        if char_code >= char_a_code and char_code <= char_z_code:
            probable_letter = find_most_probable_letter(char, letters_repartition_descending_order)
            if probable_letter != None:
                current_char = probable_letter
        result += current_char
    print(result)
    return letters_repartition_descending_order

def find_most_probable_letter(letter_to_decrypt, letters_repartition_descending_order_in_text):
    index = 0
    size = len(letters_repartition_descending_order_in_text)
    for i in range(size):
        (letter, occurrence, proportion) = letters_repartition_descending_order_in_text[i]
        # Index donnant la position dans la liste des occurrences triées
        if letter_to_decrypt == letter:
            return letters_by_descending_frequency[i]
    return None


text = "sdf sdg  dh sgtdfh  jkrtrsviospvh qp yvgzpsy ho qemifgqhewoh qreihogesuhgzqepiqgherghqzmg ohsrhemrghoqelqmsoyy haozaz"
get_most_probable_decryption(text)