char_a_code = 65
char_z_code = 90

def encrypt_or_decrypt(text, shift, is_action_equal_to_encrypt = True):
    # Permet d'utiliser une seule fonction pour le chifrement et dechifrement
    if(not is_action_equal_to_encrypt):
        shift *= (-1)
    result_text = ""
    text = text.upper()
    for character in text:
        # Récupération du nombre ascii
        char_to_code = ord(character)
        new_code_to_char = character
        if char_to_code >= char_a_code and char_to_code <= char_z_code :            
            # Position entre 0 et 25
            char_letter_code = char_to_code - char_a_code
            # Position de la lettre de substitution (entre 0 et 25)
            s_letter_code = (char_letter_code + shift) % 26
            # retour a la position en ascii
            new_char_code = s_letter_code + char_a_code
            # Recuperation de la lettre associee
            new_code_to_char = chr(new_char_code)
        result_text += new_code_to_char
    return result_text
