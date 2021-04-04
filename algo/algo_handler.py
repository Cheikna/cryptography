import algo.caesar as caesar
import algo.frequency_analysis as frequency
import algo.vigenere as vigenere
from datetime import datetime


def handle(parameters):
    # Recuperation des parametres
    algo = parameters.get("algo")
    shift = parameters.get("decalage")
    clear_text = parameters.get("texte")
    key = parameters.get("cle")
    cryted_text = parameters.get("crypte")
    action = parameters.get("action")
    frequency_list = []
    no_encryption_decryption_time = 0
    # Temps pour calculer la duree d'execution de l'algorithme
    begin_date = datetime.now()
    encryption_decryption_time = 0
    # Debut des cas d'erreur de maniere generale : cas avec des champs de textes vides
    if (action == None or action.strip() == ""):
        return ("Une action doit être définie ou des champs sont manquants.", "", frequency_list, False, action, no_encryption_decryption_time)
    if(algo == "frequence" and action != "analyse"):
        return ("Afin de procéder à l'analyse fréquentielle, veuillez sélectionner l'algorithme 'Analyse fréquentielle' en haut de la page et sélectionner 'Analyse fréquentielle' en bas de la page.", "", frequency_list, False, action, no_encryption_decryption_time)
    if action == "chiffrer" and (clear_text == None or clear_text.strip() == ""):
        return ("Le champ texte en clair ne doit pas être vide. Si vous souhaitez faire une simple analyse sélectionner le radio bouton 'Analyse'", "", frequency_list, False, action, no_encryption_decryption_time)
    if action == "dechiffer" and (cryted_text == None or cryted_text.strip() == ""):
        return ("Le champ texte crypté/chiffré ne doit pas être vide. Si vous souhaitez faire une simple analyse sélectionner le radio bouton 'Analyse'", "", frequency_list, False, action, no_encryption_decryption_time)
    if action == "analyse" and (clear_text == None or clear_text.strip() == ""):
        return ("Pour l'analyse, le champ de texte en clair ne doit pas être vide.", "", frequency_list, False, action)
    # Fin des cas d'erreurs
    ## Algorithme de Cesar
    if algo == "cesar":
        if shift == None or not is_int(shift):
            return ("Dans le cadre du chiffrement de César, le décalage doit être un nombre entier !", "", frequency_list, False, action, no_encryption_decryption_time)
        else:
            is_action_to_encrypt = (action == "chiffrer")
            if is_action_to_encrypt:
                cryted_text = caesar.encrypt_or_decrypt(
                    clear_text, int(shift), True)
            else:
                clear_text = caesar.encrypt_or_decrypt(
                    cryted_text, int(shift), False)
    ## Analyse frequentielle
    elif algo == "frequence":
        frequency_list = frequency.get_most_probable_decryption(clear_text)
     ## Vigenere
    elif algo == "vigenere" or algo == "vigenere-matrice":
        if (key == None or key.strip() == ""):
            return ("Dans le cadre de l'algorithme de Vigenère, la clé doit être renseignée !", "", frequency_list, False, action, no_encryption_decryption_time) 
        is_action_to_encrypt = (action == "chiffrer")
        if algo == "vigenere":
            if is_action_to_encrypt:
                cryted_text = vigenere.encrypt_or_decrypt_mathematically(clear_text, key, True)
            else:
                clear_text = vigenere.encrypt_or_decrypt_mathematically(cryted_text, key, False)
        elif algo == "vigenere-matrice":
            if is_action_to_encrypt:
                cryted_text = vigenere.encrypt_or_decrypt_with_matrix(clear_text, key, True)
            else:
                clear_text = vigenere.encrypt_or_decrypt_with_matrix(cryted_text, key, False)

    end_date = datetime.now()
    encryption_decryption_time = (end_date - begin_date).total_seconds() * 1000
    return (clear_text, cryted_text, frequency_list, True, action, encryption_decryption_time)

# Source : https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False