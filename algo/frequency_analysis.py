a_char_code = 65
z_char_code = 90

"""
Initialisation d'un dictionnaire qui associe 0 a chaque lettre.
dictionnaire = {A:0, B:0, C:0,...., Y:0, Z:0}
"""
def init_letters_dict():
    frequency_dict = {}
    for i in range (a_char_code, z_char_code+1):
        char = chr(i)
        frequency_dict[char] = 0
    return frequency_dict

def frequency(text):
    print(text)
    # Suppression des espaces et mise en majuscule
    text = text.replace(" ", "").upper()
    number_of_letters = 0
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
